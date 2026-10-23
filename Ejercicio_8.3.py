import tkinter as tk
from tkinter import ttk, messagebox
import math


class Figura:
    def volumen(self):
        pass

    def superficie(self):
        pass


class Cilindro(Figura):
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def volumen(self):
        return math.pi * self.r**2 * self.h

    def superficie(self):
        return 2 * math.pi * self.r * (self.r + self.h)


class Esfera(Figura):
    def __init__(self, r):
        self.r = r

    def volumen(self):
        return 4 * math.pi * self.r**3 / 3

    def superficie(self):
        return 4 * math.pi * self.r**2


class Piramide(Figura):
    def __init__(self, b, h, a):
        self.b = b
        self.h = h
        self.a = a

    def volumen(self):
        return self.b**2 * self.h / 3

    def superficie(self):
        return self.b**2 + 2 * self.b * self.a


class Cubo(Figura):
    def __init__(self, l):
        self.l = l

    def volumen(self):
        return self.l**3

    def superficie(self):
        return 6 * self.l**2


class Prisma(Figura):
    def __init__(self, l, a, h):
        self.l = l
        self.a = a
        self.h = h

    def volumen(self):
        return self.l * self.a * self.h

    def superficie(self):
        return 2 * (self.l*self.a + self.l*self.h + self.a*self.h)


campos = {
    "Cilindro": ["Radio", "Altura"],
    "Esfera": ["Radio"],
    "Pirámide": ["Lado de la base", "Altura", "Apotema"],
    "Cubo": ["Lado"],
    "Prisma": ["Largo", "Ancho", "Altura"]
}

ventana = tk.Tk()
ventana.title("Figuras geométricas")
ventana.geometry("360x500")

tk.Label(ventana, text="Calculadora de figuras",
         font=("Arial", 16)).pack(pady=10)

tipo = tk.StringVar(value="Cilindro")
lista = ttk.Combobox(ventana, textvariable=tipo,
                     values=list(campos.keys()), state="readonly")
lista.pack()
entradas = {}

dibujo = tk.Canvas(ventana, width=180, height=100, bg="white")
dibujo.pack(pady=8)


def mostrar_dibujo(event=None):
    dibujo.delete("all")
    figura = tipo.get()

    if figura == "Cilindro":
        dibujo.create_rectangle(55, 25, 125, 75, outline="black", width=2)
        dibujo.create_oval(55, 15, 125, 35, outline="black", width=2)
        dibujo.create_arc(55, 65, 125, 85, start=180, extent=180,
                          style="arc", outline="black", width=2)
    elif figura == "Esfera":
        dibujo.create_oval(45, 10, 135, 95, outline="black", width=2)
    elif figura == "Pirámide":
        dibujo.create_polygon(90, 10, 35, 85, 145, 85,
                              outline="black", fill="", width=2)
    elif figura == "Cubo":
        dibujo.create_rectangle(50, 25, 110, 80, outline="black", width=2)
        dibujo.create_polygon(50, 25, 75, 10, 135, 10, 110, 25,
                              outline="black", fill="", width=2)
        dibujo.create_polygon(110, 25, 135, 10, 135, 65, 110, 80,
                              outline="black", fill="", width=2)
    else:
        dibujo.create_rectangle(35, 25, 125, 75, outline="black", width=2)
        dibujo.create_polygon(35, 25, 55, 10, 145, 10, 125, 25,
                              outline="black", fill="", width=2)
        dibujo.create_polygon(125, 25, 145, 10, 145, 60, 125, 75,
                              outline="black", fill="", width=2)


panel = tk.Frame(ventana)
panel.pack()
resultado = tk.Label(ventana, text="", font=("Arial", 11))
resultado.pack(pady=10)


def actualizar(event=None):
    for elemento in panel.winfo_children():
        elemento.destroy()
    entradas.clear()
    resultado.config(text="")

    for campo in campos[tipo.get()]:
        tk.Label(panel, text=campo + ":").pack()
        entrada = tk.Entry(panel, justify="center")
        entrada.pack()
        entradas[campo] = entrada

    mostrar_dibujo()


def calcular():
    try:
        valores = []

        for campo in campos[tipo.get()]:
            numero = float(entradas[campo].get())

            if numero <= 0:
                messagebox.showerror(
                    "Error", "Usa números mayores que cero."
                )
                return

            valores.append(numero)

    except ValueError:
        messagebox.showerror("Error", "Ingresa números válidos.")
        return

    if tipo.get() == "Cilindro":
        figura = Cilindro(*valores)
    elif tipo.get() == "Esfera":
        figura = Esfera(*valores)
    elif tipo.get() == "Pirámide":
        figura = Piramide(*valores)
    elif tipo.get() == "Cubo":
        figura = Cubo(*valores)
    else:
        figura = Prisma(*valores)

    resultado.config(
        text=f"Volumen: {figura.volumen():.2f} cm³\n"
             f"Superficie: {figura.superficie():.2f} cm²"
    )


lista.bind("<<ComboboxSelected>>", actualizar)
tk.Button(ventana, text="Calcular", command=calcular).pack(pady=8)

actualizar()
ventana.mainloop()
