class Hospital:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.doctores = []

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def __str__(self):
        doctores_str = "\n  ".join(str(d) for d in self.doctores)
        return f"Hospital: {self.nombre}, Dirección: {self.direccion}\n  Doctores:\n  {doctores_str}"
