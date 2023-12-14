class Plantilla:
    def __init__(self):
        self.plantilla = {73523: {"Nombre": "Ivan", "Ocupacion":"Ingeniero"}} # Que la matricula se asocie a un obj usuario(doc, sec, etc,)
        self.MATRICULA = 73523

    def agregar_empleado(self, nombre, ocupacion):
        self.MATRICULA += 1
        self.plantilla[self.MATRICULA] = {"Nombre": nombre, "Ocupacion": ocupacion}
    
    def es_empleado(self, matricula):
        return matricula in self.plantilla
    

