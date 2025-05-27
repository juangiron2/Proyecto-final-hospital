import unittest
import os
from controller.hospital_controller import HospitalController
from model.hospital import Hospital
from model.doctor import Doctor

class TestHospitalController(unittest.TestCase):
    def setUp(self):
        self.path = "test/temp_hospitales.json"
        self.ctrl = HospitalController(self.path)

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_crear_y_obtener_hospital(self):
        hosp = Hospital("San Jorge", "Calle Falsa 123")
        self.ctrl.crear(hosp)
        resultado = self.ctrl.obtener_por_id("San Jorge")
        self.assertEqual(resultado.direccion, "Calle Falsa 123")

    def test_agregar_doctor_al_hospital(self):
        hosp = Hospital("San Lucas", "Carrera 9")
        doctor = Doctor(2, "Dr. Strange", "Cirugía")
        hosp.agregar_doctor(doctor)
        self.ctrl.crear(hosp)
        resultado = self.ctrl.obtener_por_id("San Lucas")
        self.assertEqual(len(resultado.doctores), 1)
        self.assertEqual(resultado.doctores[0].nombre, "Dr. Strange")

    def test_eliminar_hospital(self):
        hosp = Hospital("Santa Fe", "Avenida X")
        self.ctrl.crear(hosp)
        self.ctrl.eliminar("Santa Fe")
        self.assertIsNone(self.ctrl.obtener_por_id("Santa Fe"))

if __name__ == '__main__':
    unittest.main()
