import tkinter as tk
from tkinter import messagebox
from model.doctor import Doctor
from model.hospital import Hospital
from controller.doctor_controller import DoctorController
from controller.hospital_controller import HospitalController

def ejecutar_gui():
    doc_ctrl = DoctorController()
    hos_ctrl = HospitalController()

    def registrar_doctor():
        try:
            id_doc = int(id_entry.get())
            nombre_doc = nombre_entry.get()
            esp_doc = especialidad_entry.get()
            nombre_hosp = hospital_entry.get()

            doctor = Doctor(id_doc, nombre_doc, esp_doc)
            doc_ctrl.crear(doctor)

            hospital = hos_ctrl.obtener_por_id(nombre_hosp)
            if hospital:
                hospital.agregar_doctor(doctor)
            else:
                hospital = Hospital(nombre_hosp, "Sin dirección")
                hospital.agregar_doctor(doctor)
                hos_ctrl.crear(hospital)

            messagebox.showinfo("Éxito", f"Doctor {nombre_doc} registrado en {nombre_hosp}.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def consultar_hospital():
        nombre_hosp = consulta_entry.get()
        hospital = hos_ctrl.obtener_por_id(nombre_hosp)
        if hospital:
            resultado.config(text=str(hospital))
        else:
            resultado.config(text="Hospital no encontrado.")

    # UI
    ventana = tk.Tk()
    ventana.title("Sistema Hospitalario")

    tk.Label(ventana, text="Registrar Doctor").grid(row=0, columnspan=2)

    tk.Label(ventana, text="ID Doctor").grid(row=1, column=0)
    id_entry = tk.Entry(ventana)
    id_entry.grid(row=1, column=1)

    tk.Label(ventana, text="Nombre").grid(row=2, column=0)
    nombre_entry = tk.Entry(ventana)
    nombre_entry.grid(row=2, column=1)

    tk.Label(ventana, text="Especialidad").grid(row=3, column=0)
    especialidad_entry = tk.Entry(ventana)
    especialidad_entry.grid(row=3, column=1)

    tk.Label(ventana, text="Hospital").grid(row=4, column=0)
    hospital_entry = tk.Entry(ventana)
    hospital_entry.grid(row=4, column=1)

    tk.Button(ventana, text="Registrar", command=registrar_doctor).grid(row=5, columnspan=2)

    tk.Label(ventana, text="Consultar Hospital").grid(row=6, columnspan=2)
    consulta_entry = tk.Entry(ventana)
    consulta_entry.grid(row=7, column=0)
    tk.Button(ventana, text="Consultar", command=consultar_hospital).grid(row=7, column=1)

    resultado = tk.Label(ventana, text="", justify="left", wraplength=400)
    resultado.grid(row=8, columnspan=2)

    ventana.mainloop()
