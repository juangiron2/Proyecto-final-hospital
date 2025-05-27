import unittest
import os
from controller.doctor_controller import DoctorController
from model.doctor import Doctor

class TestDoctorController(unittest.TestCase):
    def setUp(self):
        self.path = "test/temp_doctores.json"
        self.ctrl = DoctorController(self.path)

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_crear_y_obtener(self):
        doc = Doctor(1, "Dr. House", "Diagnóstico")
        self.ctrl.crear(doc)
        resultado = self.ctrl.obtener_por_id(1)
        self.assertEqual(resultado.nombre, "Dr. House")

    def test_actualizar(self):
        doc = Doctor(1, "Dr. Original", "Cardiología")
        self.ctrl.crear(doc)
        doc_actualizado = Doctor(1, "Dr. Actualizado", "Neurología")
        self.ctrl.actualizar(doc_actualizado)
        self.assertEqual(self.ctrl.obtener_por_id(1).especialidad, "Neurología")

    def test_eliminar(self):
        doc = Doctor(1, "Dr. X", "Oncología")
        self.ctrl.crear(doc)
        self.ctrl.eliminar(1)
        self.assertIsNone(self.ctrl.obtener_por_id(1))

if __name__ == '__main__':
    unittest.main()
