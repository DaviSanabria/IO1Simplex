from fractions import Fraction

class Matriz:
    def __init__(self,matriz,pivote):
        self.matriz = matriz
        self.pivotec = pivote[0]
        self.pivotef = pivote[1]
        self.pivote = matriz[pivote[1]][pivote[0]]

    def filasale(self):
        for i in range(2):
            self.matriz[self.pivotef][i] = self.matriz[i][self.pivotec]
        if self.pivote!=1:
            print("------filae-----------------")
            for i in range(2,len(self.matriz[0])):
                print(self.matriz[self.pivotef][i],self.pivote)
                self.matriz[self.pivotef][i] = Fraction(self.matriz[self.pivotef][i],self.pivote)

    def demasfilas(self):
        for i in range(2,len(self.matriz)-2):
            aux = self.matriz[i][self.pivotec]
            if(i!=self.pivotef):
                for j in range(2,len(self.matriz[0])):
                    self.matriz[i][j] = self.matriz[i][j] - (aux*self.matriz[self.pivotef][j])

    def solucion(self):
        fila = len(self.matriz)-2
        suma = 0
        for i in range(2,len(self.matriz[0])):
            for j in range(2,fila):
                suma += self.matriz[j][0]*self.matriz[j][i]

            self.matriz[fila][i] = suma
            suma = 0

    def cj(self):
        fila = len(self.matriz) - 1
        for i in range(3,len(self.matriz[0])):
            self.matriz[fila][i] = self.matriz[0][i]-self.matriz[fila-1][i]

    def convinar(self):
        self.filasale()
        self.demasfilas()
        self.solucion()
        self.cj()

        return self.matriz