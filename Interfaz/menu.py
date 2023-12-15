from data_base import DataBase

class Menu:
    def __init__(self):
        self.plantilla = DataBase()

    def selec_opcion(self, opciones):
        valido = False
        while not valido:
            opcion = int(input("Ingrese una opcion: "))
            if opcion > 0 and opcion <= opciones:
                return opcion
            else:
                print("Opcion invalida, intente de nuevo")

    def principal(self):
        print("Menu principal\n")
        print("1. Admin")
        print("2. Paciente")
        opcion = self.selec_opcion(2)
        if opcion == 1:
            self.admin()
        else:
            self.login()

    def admin(self):
        print("~ MENU ADMINISTRADOR ~\n")
        print("1. Agregar paciente")
        print("2. Eliminar paciente")
        print("3. Regresar")
        opcion = self.selec_opcion(3)
        if opcion == 1:
            self.agregar_paciente()
            self.admin()
        elif opcion == 2:
            pass
        else:
            self.principal()

    def agregar_paciente(self):
        nombre = input("Ingrese el nombre del paciente: ")
        self.plantilla.agregar_paciente(nombre)


    def citas(self):
        print("Bienvenido!!")
        print("~ Menu Principal de Citas ~\n")   # Dependiendo que tipo de usuario entre, deberia de aparecer 
                                        # un menu con acciones especificas de su labor

    def verificar_login(self):
        exito = False
        while not exito:  
            matricula = input("Ingrese su matricula de paciente: ")
            if self.plantilla.esta_registrado(matricula): # Falta verificar que solo se acepte un numero valido
                exito = True
            else:
                print("Matricula no encontrada, intente de nuevo o comuniquese con el encargado\n")


    def login(self):
        print("S I S T E M A  D E  C I T A S\n")
        print("~ Inicio de sesion ~\n")
        self.verificar_login()
        self.citas()

    def iniciar_sistema(self):
        self.principal()