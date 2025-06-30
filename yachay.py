import tkinter as tk
from tkinter import messagebox

# Diccionario Kichwa → Español
diccionario_kichwa = {
    "alli": "Bueno / Bien",
    "kawsay": "Vida",
    "yachay": "Aprender / Saber",
    "sumak": "Hermoso / Bonito",
    "urku": "Montaña",
    "intí": "Sol",
    "mayu": "Río",
    "wasi": "Casa",
    "runakunapak": "Para las personas",
}

# Inverso: Español → Kichwa
diccionario_espanol = {v.lower(): k for k, v in diccionario_kichwa.items()}

# Textos para la interfaz en cada modo
textos = {
    True: {  # Kichwa → Español
        "ventana_titulo": "YachayApp - Aprende Kichwa",
        "titulo": "📚 YachayApp - Aprende Kichwa",
        "modo": "🌐 Modo actual: Kichwa → Español",
        "buscar": "🔍 Buscar palabra en Kichwa",
        "ver": "📖 Ver palabras en Kichwa",
        "cambiar": "🇪🇨 Cambiar a Español",
        "salir": "🚪 Salir",
        "no_encontrado": "❌ Palabra no encontrada en Kichwa.",
        "resultado_antes": "{} significa:\n{}",
        "ver_titulo": "Palabras en Kichwa",
        "bg_color": "#e6f2e6",
    },
    False: {  # Español → Kichwa
        "ventana_titulo": "YachayApp - Aprende desde Español",
        "titulo": "📘 YachayApp - Aprende desde Español",
        "modo": "🌐 Modo actual: Español → Kichwa",
        "buscar": "🔍 Buscar palabra en Español",
        "ver": "📖 Ver palabras en Español",
        "cambiar": "🇪🇸 Cambiar a Kichwa",
        "salir": "🚪 Salir",
        "no_encontrado": "❌ Palabra no encontrada en Español.",
        "resultado_antes": "{} en Kichwa es:\n{}",
        "ver_titulo": "Palabras en Español",
        "bg_color": "#fce4ec",
    }
}

modo_kichwa_a_espanol = True

def actualizar_interfaz():
    # Actualiza todos los textos, colores y título de ventana según modo actual
    t = textos[modo_kichwa_a_espanol]
    ventana.config(bg=t["bg_color"])
    ventana.title(t["ventana_titulo"])  # Aquí cambia el título de la ventana
    titulo.config(text=t["titulo"], bg=t["bg_color"])
    label_modo.config(text=t["modo"], bg=t["bg_color"])
    btn_buscar.config(text=t["buscar"])
    btn_ver.config(text=t["ver"])
    btn_cambiar.config(text=t["cambiar"])
    btn_salir.config(text=t["salir"])

def ver_palabras():
    if modo_kichwa_a_espanol:
        palabras = "\n".join([f"{k} → {v}" for k, v in diccionario_kichwa.items()])
    else:
        palabras = "\n".join([f"{v} → {k}" for k, v in diccionario_kichwa.items()])
    messagebox.showinfo(textos[modo_kichwa_a_espanol]["ver_titulo"], palabras)

def buscar_palabra():
    palabra = entrada.get().lower()
    if modo_kichwa_a_espanol:
        significado = diccionario_kichwa.get(palabra)
    else:
        significado = diccionario_espanol.get(palabra)
    if significado:
        messagebox.showinfo("Resultado", textos[modo_kichwa_a_espanol]["resultado_antes"].format(palabra.capitalize(), significado))
    else:
        messagebox.showwarning("No encontrado", textos[modo_kichwa_a_espanol]["no_encontrado"])

def cambiar_modo():
    global modo_kichwa_a_espanol
    modo_kichwa_a_espanol = not modo_kichwa_a_espanol
    actualizar_interfaz()

# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.geometry("420x350")

# Componentes
titulo = tk.Label(ventana, font=("Arial", 14, "bold"))
titulo.pack(pady=10)

label_modo = tk.Label(ventana, font=("Arial", 10, "italic"))
label_modo.pack(pady=5)

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

btn_buscar = tk.Button(ventana, width=30, command=buscar_palabra)
btn_buscar.pack(pady=5)

btn_ver = tk.Button(ventana, width=30, command=ver_palabras)
btn_ver.pack(pady=5)

btn_cambiar = tk.Button(ventana, width=30, command=cambiar_modo)
btn_cambiar.pack(pady=5)

btn_salir = tk.Button(ventana, width=30, command=ventana.quit)
btn_salir.pack(pady=15)

# Inicializamos textos y colores
actualizar_interfaz()

ventana.mainloop()
