
#Función complementaria del UserPassesTestMixin
def test_func(self):
    item = self.get_object()
    # Para ver si el que quiere editar es el autor
    if self.request.user == item.user:
        return True
    return False
