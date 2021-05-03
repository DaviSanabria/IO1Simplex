import sympy
class Tabla:
    def __init__(self,funcion,variables,restricciones,desig,result):
        self.funcion = funcion
        self.variables = variables
        self.restricciones = restricciones
        self.desig = desig
        self.result = result
        self.matriz = []

    def matrizlol(self):
        cont = 0
        M = sympy.symbols('M')
        fila1 = []
        fila2 = []
        fila3 = []
        fila1.append("")
        fila1.append("Cj")
        fila1.append("")
        fila2.append("Cb")
        fila2.append("VS")
        fila2.append("Sol")
        for i in range(len(self.variables)):
            fila1.append(int(self.variables[i]))
            fila2.append("X%d" % (i + 1))
        for i in range(len(self.desig)):
            if self.desig[i] == "≤":
                fila1.append(0)
                fila2.append("S%d" % (i + 1))
            elif self.desig[i] == "≥":
                fila1.append(0)
                fila2.append("S%d" % (i + 1))
                cont += 1
            else:
                cont += 1
        for i in range(cont):
            if(self.funcion == "Min z"):
                fila1.append(M)
            else: fila1.append(M*-1)
            fila2.append("A%d" % (i + 1))

        self.matriz.append(fila1)
        self.matriz.append(fila2)

        cont = 0
        auxva = 0
        auxvari = ""
        auxA = ""
        for i in range(len(self.desig)):
            if self.desig[i] == "≤":
                auxvari = "S%d" % (i+1)
                auxva = 1
                fila3.append(0)
                fila3.append(auxvari)
            elif self.desig[i] == "≥":
                auxvari = "S%d" % (i+1)
                auxva = -1
                auxA = "A%d"%(cont+1)
                if (self.funcion == "Min z"):
                    fila3.append(M)
                else:
                    fila3.append(M * -1)
                fila3.append(auxA)
                cont += 1
            else:
                if (self.funcion == "Min z"):
                    fila3.append(M)
                else:
                    fila3.append(M * -1)
                fila3.append("A%d" % (cont + 1))
                auxA = "A%d" % (cont + 1)
                cont += 1

            fila3.append(int(self.result[i]))

            for j in range(len(fila2)-3):
                if(fila2[j+3][0] == "X"):
                    fila3.append(int(self.restricciones[i][j]))
                elif(fila2[j+3] == auxvari):
                    fila3.append(auxva)
                elif(fila2[j+3] == auxA):
                    fila3.append(1)
                else: fila3.append(0)
            auxva = 0
            auxvari = ""
            auxA = ""
            self.matriz.append(fila3.copy())
            fila3 = []

        self.solucion(M)
        self.cj(M)

        return self.matriz

    def solucion(self,M):
        fila4 = []
        sum = 0
        fila4.append("")
        fila4.append("Zj")
        for i in range(len(self.matriz[0])-2):
            for j in range(len(self.result)):
                sum += self.matriz[j+2][0] * self.matriz[j+2][i+2]
            fila4.append(sum)
            sum=0
        self.matriz.append(fila4)

    def cj(self,M):
        fila5 = []
        fila5.append("")
        fila5.append("Cj-Zj")
        fila5.append("")
        for i in range(len(self.matriz[0]) - 3):
            fila5.append(self.matriz[0][i+3]-self.matriz[len(self.matriz)-1][i+3])
        self.matriz.append(fila5)