from interfaces.crud_interface import CRUD
from model.hospital import Hospital
from model.doctor import Doctor
from utils.json_handler import guardar_json, cargar_json

class HospitalController(CRUD):
    def __init__(self, ruta_json="data/hospitales.json"):
        self.ruta = ruta_json
        self.hospitales = self._cargar()

    def _cargar(self):
        datos = cargar_json(self.ruta)
        hospitales = {}
        for nombre, info in datos.items():
            hosp = Hospital(info["nombre"], info["direccion"])
            hosp.doctores = [Doctor(**doc) for doc in info["doctores"]]
            hospitales[nombre] = hosp
        return hospitales

    def _guardar(self):
        serializable = {
            nombre: {
                "nombre": hosp.nombre,
                "direccion": hosp.direccion,
                "doctores": [vars(doc) for doc in hosp.doctores]
            }
            for nombre, hosp in self.hospitales.items()
        }
        guardar_json(self.ruta, serializable)

    def crear(self, hospital):
        self.hospitales[hospital.nombre] = hospital
        self._guardar()

    def obtener_por_id(self, nombre):
        return self.hospitales.get(nombre)

    def actualizar(self, hospital):
        if hospital.nombre in self.hospitales:
            self.hospitales[hospital.nombre] = hospital
            self._guardar()

    def eliminar(self, nombre):
        if nombre in self.hospitales:
            del self.hospitales[nombre]
            self._guardar()

    def listar(self):
        return list(self.hospitales.values())
