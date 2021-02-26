class Cliente:
    """
        # Cliente (Clase)
        Clientes registrados en la tienda
        - Atributos:
            - dni -> str
            - nombre -> str
            - apellidos -> str
    """
    clientes = {}   # Patrón Active record

    def __init__(self, dni, nombre, apellidos):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        Cliente.clientes[dni] = self

    @staticmethod
    def get_cliente(numero):
        return Cliente.clientes.get(numero)

    def dni(self):
        return self.__dni

    def nombre(self):
        return self.__nombre

    def apellidos(self):
        return self.__apellidos

    def __repr__(self):
        return f'Cliente ({self.__nombre} {self.__apellidos}, DNI: {self.__dni})'






"""class Alumno(Cliente):
    def __init__(self, dni, nombre, apellidos, curso):
        super().__init__(dni, nombre, apellidos)
        self.__curso = curso

    def descripcion(self):
        return super().descripcion() + f' y estoy cursando {self.__curso}'

lucia = Alumno ('98765432T', 'Lucía', 'Terraria', 'Prevencion de riesgos laborales')"""
