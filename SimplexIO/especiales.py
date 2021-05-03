import sympy
from tkinter import messagebox
from fractions import Fraction

class CEspeciales:
    def __init__(self,Matriz,funcion):
        self.Matriz = Matriz
        self.funcion = funcion
        self.pivotefc = []
        self.degenerado = False
        self.mult = False
        self.abierto = False
        self.nacotada = False
        self.solucion = False

    def pivoteE(self):
        pos = 3                                  #posicion
        M = sympy.symbols('M')                   #simbolo
        f = len(self.Matriz)-1  #Ultima fila
        a = str(type(self.Matriz[f][len(self.Matriz[0])-1]))
        if self.funcion == "Max z":
            aux1 = -10000000  # M*0
            if (a.find("sympy") != -1):                                #si tienen M
                for i in range(3,len(self.Matriz[0])):
                    aux1 = M*0 + aux1
                    self.Matriz[f][i] = M*0 + self.Matriz[f][i]
                    poly1 = sympy.Poly(aux1, M)
                    poly2 = sympy.Poly(self.Matriz[f][i], M)
                    if aux1.coeff(M) < self.Matriz[f][i].coeff(M):
                        aux1 = self.Matriz[f][i]
                        pos = i
                    elif aux1.coeff(M) == self.Matriz[f][i].coeff(M):
                        if poly1.coeffs() < poly2.coeffs():
                            aux1 = self.Matriz[f][i]
                            pos = i
                if aux1.coeff(M) == 0:
                    poly3 = sympy.Poly(aux1, M)
                    if poly3.coeffs() <= [0] : self.solucion = True
            else:                                                      #si no tiene
                for i in range(3, len(self.Matriz[0])):
                    if aux1 < self.Matriz[f][i]:
                        aux1 = self.Matriz[f][i]
                        pos = i
                if aux1<=0 :
                    self.solucion = True

        else:
            aux1 = 1000000  # M*0
            if (a.find("sympy") != -1):
                for i in range(3,len(self.Matriz[0])):
                    aux1 = M * 0 + aux1
                    self.Matriz[f][i] = M * 0 + self.Matriz[f][i]
                    poly1 = sympy.Poly(aux1, M)
                    poly2 = sympy.Poly(self.Matriz[f][i], M)
                    if aux1.coeff(M) > self.Matriz[f][i].coeff(M):
                        aux1 = self.Matriz[f][i]
                        pos = i
                    elif aux1.coeff(M) == self.Matriz[f][i].coeff(M):
                        if poly1.coeffs() > poly2.coeffs():
                            aux1 = self.Matriz[f][i]
                            pos = i
                if aux1.coeff(M) == 0:
                    poly3 = sympy.Poly(aux1, M)
                    if poly3.coeffs() >= [0] : self.solucion = True
            else:                                                      #si no tiene
                for i in range(3, len(self.Matriz[0])):
                    if aux1 > self.Matriz[f][i]:
                        aux1 = self.Matriz[f][i]
                        pos = i
                if aux1>=0 :
                    self.solucion = True
        #if(aux1 == 0):
           # messagebox.showwarning("Advertencia", "Soluciones optimas multiples")
            #self.mult=True
        self.pivotefc.append(pos)

    def pivoteS(self):
        lista = []
        minomax = -1
        print("--------------------b/a--------------------------------")
        for i in range(2, len(self.Matriz) - 2):
            if self.Matriz[i][self.pivotefc[0]]!=0:
                print(Fraction(self.Matriz[i][2], self.Matriz[i][self.pivotefc[0]]))
                lista.append(Fraction(self.Matriz[i][2],self.Matriz[i][self.pivotefc[0]]))
            else:
                lista.append(-1)

        if self.funcion == "Min z":
            try:
                minomax = min(i for i in lista if i >= 0)
                if minomax == 0:
                    try:
                        minomax = min(i for i in lista if i > 0)
                    except:
                        print("Holas")
                pos = lista.index(minomax)
                self.pivotefc.append(pos+2)
            except:
                messagebox.showwarning("Advertencia", "No hay variables de salida")
                self.abierto = True
        else:
            try:
                minomax = min(i for i in lista if i >= 0)
                if minomax == 0:
                    try:
                        minomax = min(i for i in lista if i > 0)
                    except:
                        print("Hola")
                pos = lista.index(minomax)
                self.pivotefc.append(pos + 2)
            except:
                messagebox.showwarning("Advertencia", "No hay variables de salida")
                self.abierto = True

        repit = lista.count(minomax)
        if(repit>1):
            for i in range(len(lista)):
                if(lista[i]==minomax):
                    self.pivotefc[1]=(i+2)
            messagebox.showwarning("Advertencia", "Caso degenerado")
            self.degenerado=True




