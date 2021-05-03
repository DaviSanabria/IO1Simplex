import re
import tkinter as tk
from tkinter import messagebox
from Pregunta import Pregunta


class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.ventana()
        self.numvariables = None
        self.numvarestricciones = None

    def userText(self,even):
        self.numvariables.delete(0, tk.END)
        self.numvariables.config(fg="#0A0A0A")

    def userText1(self, even):
        self.numvarestricciones.delete(0, tk.END)
        self.numvarestricciones.config(fg="#0A0A0A")

    def ventana(self):
        self.window.title("Metodo simplex")
        self.window.resizable(0,0)  #No redimension
        inicio = tk.Frame()
        inicio.pack(fill="both", expand="true")
        inicio.config(bg="#51D1F6", width = "500", height = "300")

        #numero de variables
        tk.Label(inicio,text="Cantidad de variables: ",fg="#ecf0f1", bg="#51D1F6", font = ("Comic Sans MS",18)).place(x=10, y = 10)
        self.numvariables = tk.Entry(inicio,fg="#0A0A0A",font = ("Comic Sans MS",18), justify = tk.CENTER, width = 10)
        self.numvariables.place(x=270, y = 10)
        self.numvariables.bind("<Button>",self.userText)

        #numero de restricciones
        tk.Label(inicio, text="Cantidad de restricciones: ",  bg="#51D1F6", fg="#ecf0f1", font=("Comic Sans MS", 18)).place(x=10, y=80)
        self.numvarestricciones = tk.Entry(inicio,font = ("Comic Sans MS",18), justify = tk.CENTER, width = 10)
        self.numvarestricciones.place(x=320, y=80)
        self.numvarestricciones.bind("<Button>",self.userText1)

        #Boton
        tk.Button(inicio,text="Continuar", fg = "#51D1F6", font=("Comic Sans MS", 19), cursor = "hand2", command=self.validar).place(x=350,y=200)

        self.window.mainloop()

    def validar(self):
        estructuraentero = re.compile('^\d{1,2}$')
        if (re.search(estructuraentero, self.numvarestricciones.get()) is None) or (re.search(estructuraentero, self.numvariables.get()) is None):
            messagebox.showwarning("Cuidado", "Ingrese maximo 2 numeros enteros")
        else:
            rest = self.numvariables.get()
            var = self.numvarestricciones.get()
            self.window.destroy()
            Pregunta(rest,var)




if __name__== '__main__':
    aplication = Main()