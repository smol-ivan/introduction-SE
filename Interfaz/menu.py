from plantilla import Plantilla

class Menu:
    def __init__(self):
        self.plantilla = Plantilla()

    def principal(self):
        print("S I S T E M A")
        print("~ Menu Principal ~/n")   # Dependiendo que tipo de usuario entre, deberia de aparecer 
                                        # un menu con acciones especificas de su labor

    def verificar_login(self):
        exito = False
        while not exito:  
            matricula = input("Ingrese su matricula: ")
            if self.plantilla.es_empleado(int(matricula)): # Falta verificar que solo se acepte un numero valido
                exito = True
            else:
                print("Matricula no encontrada, intente de nuevo o comuniquese con el encargado/n")


    def login(self):
        print("S I S T E M A")
        print("~ Inicio de sesion ~/n")
        self.verificar_login()
        self.principal()

    def iniciar_sistema(self):
        self.login()
        