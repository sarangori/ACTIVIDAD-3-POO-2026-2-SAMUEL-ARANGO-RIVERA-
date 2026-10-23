import tkinter as tk
from tkinter import messagebox
import math


class Notas:
    def __init__(self, notas):
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def desviacion_estandar(self):
        prom = self.promedio()
        suma = 0

        for nota in self.notas:
            suma += (nota - prom) ** 2

        varianza = suma / len(self.notas)
        return math.sqrt(varianza)

    def nota_mayor(self):
        return max(self.notas)

    def nota_menor(self):
        return min(self.notas)


class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Notas del estudiante")
        self.ventana.geometry("500x430")

        tk.Label(
            ventana,
            text="Ingrese las cinco notas (0 a 5)",
            font=("Arial", 13, "bold")
        ).pack(pady=10)

        self.entradas = []

        for i in range(5):
            tk.Label(ventana, text=f"Nota {i + 1}:").pack()

            entrada = tk.Entry(ventana, justify="center")
            entrada.pack(pady=3)

            self.entradas.append(entrada)

        tk.Button(
            ventana,
            text="Calcular",
            command=self.calcular
        ).pack(pady=12)

        self.resultado = tk.Label(
            ventana,
            text="",
            justify="left",
            font=("Arial", 10)
        )
        self.resultado.pack(pady=5)

    def calcular(self):
        notas = []

        for entrada in self.entradas:
            texto = entrada.get().strip()

            
            if texto == "":
                messagebox.showwarning(
                    "Advertencia",
                    "Debes ingresar las cinco notas."
                )
                return

            
            try:
                nota = float(texto)
            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Las notas deben ser numéricas."
                )
                return

            
            if nota < 0 or nota > 5:
                messagebox.showerror(
                    "Error",
                    "Las notas deben estar entre 0 y 5."
                )
                return

            notas.append(nota)

        
        estudiante = Notas(notas)

        promedio = estudiante.promedio()
        desviacion = estudiante.desviacion_estandar()
        mayor = estudiante.nota_mayor()
        menor = estudiante.nota_menor()

        
        self.resultado.config(
            text=f"Promedio: {promedio:.2f}\n"
                 f"Desviación estándar: {desviacion:.2f}\n"
                 f"Nota mayor: {mayor:g}\n"
                 f"Nota menor: {menor:g}"
        )


ventana = tk.Tk()
app = Interfaz(ventana)
ventana.mainloop()
