import tkinter as tk
from tkinter import messagebox
import threading
import time

def iniciar_sesion():
    boton_iniciar.config(state="disabled")
    mensaje.config(text="Meditación en curso...", fg="#16482C")
    cuenta_regresiva(15)  # segundos

def cuenta_regresiva(segundos):
    def meditar():
        for i in range(segundos, 0, -1):
            temporizador.config(text=f"Tiempo restante: {i} segundos")
            time.sleep(1)
        temporizador.config(text="")
        mensaje.config(text="¡Sesión finalizada!", fg="#A40808")
        boton_iniciar.config(state="normal")
        messagebox.showinfo("Completado", "Tu sesión de meditación ha terminado.")
    threading.Thread(target=meditar).start()

# Configuración de la ventana
root = tk.Tk()
root.title("MindEase")
root.geometry("350x350")
root.configure(bg="#DDEFF6")

# Widgets
etiqueta = tk.Label(root, text="Bienvenido a MindEase", bg="#DDEFF6", font=("Helvetica", 16, "bold"))
etiqueta.pack(pady=10)

mensaje = tk.Label(root, text="Presiona el botón para iniciar tu meditación.", bg="#DDEFF6", font=("Helvetica", 12))
mensaje.pack(pady=10)

temporizador = tk.Label(root, text="", bg="#DDEFF6", font=("Helvetica", 12, "italic"))
temporizador.pack(pady=5)

boton_iniciar = tk.Button(root, text="Iniciar meditación", command=iniciar_sesion, bg="#1D4842", fg="white", font=("Helvetica", 12))
boton_iniciar.pack(pady=10)

boton_salir = tk.Button(root, text="Salir", command=root.quit, bg="#F08080", fg="white", font=("Helvetica", 10))
boton_salir.pack(side="bottom", pady=10)

# Ejecutar interfaz
root.mainloop()
