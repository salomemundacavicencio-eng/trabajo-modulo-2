class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def actualizar(self, telefono=None, correo=None, direccion=None):
        if telefono:
            self.telefono = telefono
        if correo:
            self.correo = correo
        if direccion:
            self.direccion = direccion

    def __str__(self):
        return f"{self.nombre} | {self.telefono} | {self.correo} | {self.direccion}"
