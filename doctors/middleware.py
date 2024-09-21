# middlewares.py
from django.http import HttpResponseServerError
from sqlparse.exceptions import SQLParseError

MAX_DEPTH = 100

class SQLInjectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            # Verificar si el método es POST y si contiene datos
            if request.method == 'POST' and request.POST:
                # Calcular la profundidad de los datos POST
                depth = self.calculate_depth(request.POST)
                if depth >= MAX_DEPTH:
                    raise SQLParseError('Maximal depth reached')
        except SQLParseError as e:
            return HttpResponseServerError("Error: " + str(e))

    def calculate_depth(self, data, depth=1):
        # Lógica para calcular la profundidad aquí
        # Este es solo un ejemplo básico, puedes adaptarlo según tus necesidades.
        return depth

from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path.startswith('/login/'):
            return redirect('login')
        response = self.get_response(request)
        return response