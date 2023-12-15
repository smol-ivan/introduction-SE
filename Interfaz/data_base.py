from paciente import Paciente
class DataBase:
    def __init__(self):
        self.plantilla = {"Pacientes": []} # Que la matricula se asocie a un obj usuario(doc, sec, etc,)
        self.MATRICULA = 73523

    def agregar_paciente(self, nombre):
        paciente = Paciente(nombre, self.MATRICULA)
        self.plantilla["Pacientes"].append(paciente)
        self.MATRICULA += 1
        print(paciente.get_matricula())

    def esta_registrado(self, matricula):
        registrado = False
        for i in self.plantilla["Pacientes"]:
            if int(matricula) == i.get_matricula():
                registrado = True
                break
        return registrado
    

