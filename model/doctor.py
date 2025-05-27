class Doctor:
    def __init__(self, id_doctor, nombre, especialidad):
        self.id = id_doctor
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Doctor(ID: {self.id}, Nombre: {self.nombre}, Especialidad: {self.especialidad})"
