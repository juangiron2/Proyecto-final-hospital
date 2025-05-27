from interfaces.crud_interface import CRUD
from model.doctor import Doctor
from utils.json_handler import guardar_json, cargar_json

class DoctorController(CRUD):
    def __init__(self, ruta_json="data/doctores.json"):
        self.ruta = ruta_json
        self.doctores = self._cargar()

    def _cargar(self):
        datos = cargar_json(self.ruta)
        return {int(k): Doctor(**v) for k, v in datos.items()}

    def _guardar(self):
        serializable = {str(k): vars(v) for k, v in self.doctores.items()}
        guardar_json(self.ruta, serializable)

    def crear(self, doctor):
        self.doctores[doctor.id] = doctor
        self._guardar()

    def obtener_por_id(self, id):
        return self.doctores.get(id)

    def actualizar(self, doctor):
        if doctor.id in self.doctores:
            self.doctores[doctor.id] = doctor
            self._guardar()

    def eliminar(self, id):
        if id in self.doctores:
            del self.doctores[id]
            self._guardar()

    def listar(self):
        return list(self.doctores.values())
