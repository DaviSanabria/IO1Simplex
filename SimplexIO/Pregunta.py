from tkinter import *
from tkinter import ttk
from Resolver import Resolver

class Pregunta:
    def __init__(self,MaxVar,MaxRest):
        self.MaxVar = MaxVar
        self.MaxRest = MaxRest
        self.numvar = []
        self.numrest = []
        self.window = Tk()
        self.ventana()
        self.inicio = None

    def ventana(self):
        self.window.title("Metodo simplex")
        #self.window.resizable(0,0)  #No redimension
        w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d+0+0" % (w, h))
        scrollbar = Scrollbar(self.window, orient="horizontal")
        scrollbar2 = Scrollbar(self.window)
        c = Canvas(self.window,xscrollcommand=scrollbar.set,yscrollcommand=scrollbar2.set,bg="#51D1F6", width = "1000", height = "768")
        scrollbar.config(command=c.xview)
        scrollbar2.config(command=c.yview)
        scrollbar2.pack(side=RIGHT,fill=Y)
        scrollbar.pack(side=BOTTOM, fill=X)
        self.inicio = Frame(c,bg="#51D1F6") #el frame
        self.inicio.columnconfigure(0, weight=1)
        self.inicio.rowconfigure(0, weight=1)
        c.pack(side="left", fill="both", expand=True)
        c.create_window(0, 0, window=self.inicio, anchor="nw")


        #Maximizar o min
        labelF = Label(self.inicio, text="Funcion:", bg="#51D1F6", fg="#ecf0f1", font=("Comic Sans MS", 18))
        labelF.grid(row=0,column=0,pady=30)

        funcion = ttk.Combobox(self.inicio,state="readonly", width = 5, values=["Max z", "Min z"],font = ("Comic Sans MS",18))
        funcion.set("Max z")
        funcion.grid(row=1, column=0)

        Label(self.inicio, text="=", fg="#ecf0f1", bg="#51D1F6", font=("Comic Sans MS", 18)).grid(row=1, column=1)

        for i in range(int(self.MaxVar)):
            self.crearT(i)
            if i == 0: texto = "X"+str(i+1)
            else: texto += ",X"+str(i+1)
        Label(self.inicio, text=texto+"≥0", fg="#ecf0f1", bg="#51D1F6", font=("Comic Sans MS", 18)).grid(row=int(self.MaxRest)+5,column=0,pady=30)

        Label(self.inicio, text="Restricciones:", fg="#ecf0f1", bg="#51D1F6", font=("Comic Sans MS", 18)).grid(row=2,column=0,pady=30,padx=20)

        desig = []
        result = []
        for i in range(int(self.MaxRest)):
            for j in range(int(self.MaxVar)):
                self.crearR(i,j)
            desig.append(ttk.Combobox(self.inicio,state="readonly", width = 2, values=["≤", "≥","="],font = ("Comic Sans MS",18)))
            desig[i].set("≤")
            desig[i].grid(row=3+i, column = int(self.MaxVar)*4,padx=20)
            result.append(Entry(self.inicio, bg="#ecf0f1", font=("Comic Sans MS", 18), fg="#0A0A0A",justify=CENTER, width=10, borderwidth=0))
            result[i].grid(row=3+i, column = int(self.MaxVar)*5,padx=20)

        self.window.update()
        c.config(scrollregion=c.bbox("all"))

        boton = Button(self.inicio, text="Continuar", fg="#51D1F6", bg="#ecf0f1", font=("Comic Sans MS", 19),cursor="hand2", command= lambda : self.pasar(funcion.get(), desig, result))
        boton.grid(row=int(self.MaxRest) + 6, column=1)
        self.window.mainloop()

    def pasar(self,funcion,desig1,result):
        numvar = []
        numrest = []
        desig = []
        result1 = []
        for i in range(len(self.numvar)):
            numvar.append(self.numvar[i].get())

        for i in range(int(self.MaxRest)):
            numrest.append([])
            for j in range(int(self.MaxVar)):
                numrest[i].append(self.numrest[i][j].get())

        for i in range(len(desig1)):
            desig.append(desig1[i].get())

        for i in range(len(result)):
            result1.append(result[i].get())
        self.window.destroy()
        Resolver(funcion, numvar, numrest, desig, result1)
#---------------------------------------------
    def crearT(self,i):
        if(i==0):
            self.numvar.append(Entry(self.inicio, bg="#ecf0f1", font=("Comic Sans MS", 18), fg="#0A0A0A", justify=CENTER, width=10, borderwidth=0))
            self.numvar[i].grid(row=1, column=2)
            Label(self.inicio, text="X"+str(i+1), fg="#ecf0f1", bg="#51D1F6", font=("Comic Sans MS", 18)).grid(row=1, column=3)
        else:
            Label(self.inicio, text="+", fg="#ecf0f1", bg="#51D1F6", font=("Comic Sans MS", 18)).grid(row=1, column=i*3+1)
            self.numvar.append(Entry(self.inicio, bg="#ecf0f1", font=("Comic Sans MS", 18), fg="#0A0A0A",justify=CENTER, width=10, borderwidth=0))
            self.numvar[i].grid(row=1, column=i*3+2)
            Label(self.inicio, text="X" + str(i+1), fg="#ecf0f1", bg="#51D1F6", font=("Comic Sans MS", 18)).grid(row=1, column=i*3+3)

    def crearR(self, i,j):
        self.numrest.append([])
        if(j==0):
            self.numrest[i].append(Entry(self.inicio, bg="#ecf0f1", font=("Comic Sans MS", 18), fg="#0A0A0A", justify=CENTER, width=10,borderwidth=0))
            self.numrest[i][j].grid(row=3+i, column=2, pady = 10)
            Label(self.inicio, text="X" + str(j + 1), fg="#ecf0f1", bg="#51D1F6", font=("Comic Sans MS", 18)).grid(row=3+i, column=3)
        else:
            Label(self.inicio, text="+", fg="#ecf0f1", bg="#51D1F6", font=("Comic Sans MS", 18)).grid(row=3+i, column=j*3+1)
            self.numrest[i].append(Entry(self.inicio, bg="#ecf0f1", font=("Comic Sans MS", 18), fg="#0A0A0A",justify=CENTER, width=10, borderwidth=0))
            self.numrest[i][j].grid(row=3+i,column=j*3+2)
            Label(self.inicio, text="X" + str(j + 1), fg="#ecf0f1", bg="#51D1F6", font=("Comic Sans MS", 18)).grid(row=3+i, column=j*3+3)