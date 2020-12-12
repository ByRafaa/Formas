import math
class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Forma(Punto):
    def __init__(self,x,y,color,nombre):
        super().__init__(x,y)
        self.color = color
        self.nombre = nombre

    def imprimir(self):
        print("Coordenadas x = " + str(self.x) + " | Coordenadas y = " + str(self.y) + " | Color = " + self.color + " | Nombre = " + self.nombre)

    def obtenerColor(self):
        return self.color

    def cambiarColor(self,color):
        self.color = color

    def cambiarPosicion(self,x,y):
        self.x=x
        self.y=y

#Forma1 = Forma(5,10,"Rojo","Circulo")
#Forma1.imprimir()
#Forma1.cambiar(3,1)
#print(Forma1.obtenerColor())
#Forma1.cambiarColor("Amarillo")
#Forma1.imprimir()

class Rectangulo(Forma):

    def __init__(self,x,y,color,ladoMenor,ladoMayor,nombre):
        super().__init__(x,y,color,nombre)
        self.ladoMenor = ladoMenor
        self.ladoMayor = ladoMayor

    def imprimirRectangulo(self):
        super().imprimir()
        print("Lado Menor = " + str(self.ladoMenor) + " | Lado Mayor = " + str(self.ladoMayor))

    def calcularArea(self):
        area=self.ladoMenor*self.ladoMayor
        print("Area = " + str(area))

    def calcularPerimetro(self):
        perimetro=(self.ladoMayor*2)+(self.ladoMenor*2)
        print("Perimetro = " + str(perimetro))

    def cambiarTamaño(self,escala):
        self.ladoMenor=self.ladoMenor*escala
        self.ladoMayor=self.ladoMayor*escala


#Rectangulo1 = Rectangulo(10,5,"Verde",6,8,"Rectangulo")

#Rectangulo1.imprimirRectangulo()
#Rectangulo1.calcularArea()
#Rectangulo1.calcularPerimetro()
#Rectangulo1.cambiarTamaño(2)
#Rectangulo1.calcularPerimetro()

class Elipse(Forma):

    def __init__(self,x,y,color,radioMayor,radioMenor,nombre):
        super().__init__(x,y,color,nombre)
        self.radioMayor = radioMayor
        self.radioMenor = radioMenor

    def imprimirElipse(self):
        super().imprimir()
        print("Radio Mayor = " + str(self.radioMayor) + " | Radio Menor = " + str(self.radioMenor))

    def calcularAreaElipse(self):
        area=math.pi*(self.radioMayor*self.radioMenor)
        print("Area = " + str(area))

#Elipse1 = Elipse(10,5,"Rosa",10,7,"Elipse")
#Elipse1.imprimirElipse()
#Elipse1.calcularAreaElipse()

class Cuadrado(Rectangulo):

    def __init__(self,x,y,color,lado,nombre):
        super().__init__(x,y,color,lado,lado,nombre)

    def imprimirCuadrado(self):
        super().imprimirRectangulo()

#Cuadrado1 = Cuadrado(10,5,"Azul",6,"Cuadrado")
#Cuadrado1.imprimirCuadrado()

class Circulo(Elipse):

    def __init__(self,x,y,color,radio,nombre):
        super().__init__(x,y,color,radio,radio,nombre)

    def imprimirCirculo(self):
        super().imprimirElipse()

#Circulo1 = Circulo(10,5,"Blanco",6,"Circulo")
#Circulo1.imprimirCirculo()
#Circulo1.calcularAreaElipse()

Rectangulo2 = Rectangulo(10,5,"Verde",5,23,"Rectangulo")
Elipse2 = Elipse(7,4,"Rojo",15,6,"Elipse")
Cuadrado2 = Cuadrado(50,29,"Azul",10,"Cuadrado")
Circulo2 = Circulo(10,53,"Blanco",7,"Circulo")

lista=(Rectangulo2,Elipse2,Cuadrado2,Circulo2)

for Forma in lista:
    Forma.cambiarColor("Negro")
    Forma.cambiarPosicion(30,25)

print(" ")
print("Color y Posición cambiados")
print(" ")
Rectangulo2.imprimirRectangulo()
Elipse2.imprimirElipse()
Cuadrado2.imprimirCuadrado()
Circulo2.imprimirCirculo()

