class Empleado:

    def __init__(self,nombre,apellidos,dni,direccion,telefono,salario,supervisor,puesto):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.salario = salario
        self.supervisor = supervisor
        self.puesto = puesto

    def mostrarEmpleado(self):
        print("Nombre : " + self.nombre + " | Apellidos : " + self.apellidos + " | DNI : " + self.dni + " | Direccion : "
              + self.direccion + " | Telefono : " + str(self.telefono) + " | Salario : " + str(self.salario) + " | Supervisor : "
              + self.supervisor + " | Puesto : " + self.puesto)

    def cambiarSupervisor(self,supervisor):
        self.supervisor = supervisor

    def incrementarSalario(self,incremento):
        self.salario = (self.salario * incremento)/100 + self.salario

print("----------EMPLEADO----------")
empleado1 = Empleado("Rosa","Jimenez Ramirez","12345678A","Calle abc 1",654321987,15000,"Pepe","Empleado")
empleado1.incrementarSalario(10)
empleado1.cambiarSupervisor("Luis")
empleado1.mostrarEmpleado()
print("------------------------------")

class Secretario(Empleado):

    def __init__(self,nombre,apellidos,dni,direccion,telefono,salario,supervisor,puesto,fax,despacho):
        super().__init__(nombre,apellidos,dni,direccion,telefono,salario,supervisor,puesto)
        self.fax = fax
        self.despacho = despacho

    def mostrarSecretario(self):
        super().mostrarEmpleado()
        print("Puesto : " + self.puesto)

    def incrementarSalarioSecretario(self):
        self.incrementarSalario(5)

print("----------SECRETARIO----------")
secretario1 = Secretario("Rafael","Escudero Ortega","23456789B","Calle b 2","687594231",16000,"Juanlu","Secretario","DA1","Direccion")
secretario1.incrementarSalarioSecretario()
secretario1.mostrarSecretario()
secretario2 = Secretario("Manuel","Tejada Ortega","84536718G","Calle d 4","681549728",16500,"Juanlu","Secretario","DA1","Direccion")
print("------------------------------")

class Coche():

    def __init__(self,matricula,marca,modelo):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo

coche1 = Coche("5218HDJ","BMW","I8")
coche2 = Coche("8459JET","Audi","A4")
coche3 = Coche("2534GTS","Aston Martin","Victor")
coche4 = Coche("7915IUT","Peugeot","206")

class Cliente():

    def __init__(self,nombre):
        self.nombre = nombre

class Vendedor(Empleado):

    def __init__(self,nombre,apellidos,dni,direccion,telefono,salario,supervisor,movil,area,lista,comision,coche,puesto):

        super().__init__(nombre,apellidos,dni,direccion,telefono,salario,supervisor,puesto)
        self.movil=movil
        self.area=area
        self.lista=lista
        self.comision=comision
        self.coche = coche

    def mostrarVendedor(self):

        super().mostrarEmpleado()
        print("Movil : " + str(self.movil) + " | Area : " + self.area + " | Comision Venta : " + str(self.comision) + "%")
        print("Lista de Clientes : " + str(self.lista))
        print("Coche : " + str(self.coche.matricula))

    def altaCliente(self,nombre):
        self.lista.append(nombre)

    def bajaCliente(self,nombre):
        self.lista.remove(nombre)

    def cambiarCoche(self,coche):
        self.coche = coche

    def incrementarSalarioVendedor(self):
        self.incrementarSalario(10)

print("----------VENDEDOR----------")
listaClientes1 = ("Juan","Jose","María","Manuel")
lista1=list(listaClientes1)
listaClientes2 = ("Manel","Paqui","Ivan")
lista2=list(listaClientes2)
vendedor1 = Vendedor("Luis","Clares Segura","34567890C","Calle c 3","625135480",18000,"Minerva",687125489,"Roquetas",lista1,8,coche1,"Vendedor")
vendedor2 = Vendedor("Manuel","Sopena Sanchez","528425457E","Calle e 5","625135480",15000,"Minerva",687125489,"Guadix",lista2,6,coche4,"Vendedor")
vendedor1.incrementarSalarioVendedor()
vendedor1.altaCliente("Rocío")
vendedor1.bajaCliente("Juan")
vendedor1.cambiarCoche(coche2)
vendedor1.mostrarVendedor()
print("------------------------------")

class Jefe(Empleado):

    def __init__(self,nombre,apellidos,dni,direccion,telefono,salario,supervisor,despacho,secretario,vendedores,coche,puesto):
        super().__init__(nombre,apellidos,dni,direccion,telefono,salario,supervisor,puesto)
        self.despacho = despacho
        self.secretario = secretario
        self.vendedores = vendedores
        self.coche = coche

    def mostrarJefe(self):
        super().mostrarEmpleado()
        print("Despacho : " + self.despacho + " | Secretario : " + self.secretario.nombre)

        print("Vendedores:")
        for Vendedor in self.vendedores:
            print(Vendedor.nombre)
        print("Coche : " + str(self.coche.matricula))

    def cambiarSecretario(self,secretario):
        self.secretario = secretario

    def cambiarCoche(self,coche):
        self.coche = coche

    def altaVendedor(self,nombre,apellidos,dni,direccion,telefono,salario,supervisor,movil,area,lista,comision,coche):

        vendedor = Vendedor(nombre,apellidos,dni,direccion,telefono,salario,supervisor,movil,area,lista,comision,coche)

        self.vendedores.append(vendedor)

    def bajaVendedor(self,posicion):

        self.vendedores.pop(posicion)

    def incrementarSalarioJefe(self):
        self.incrementarSalario(20)

print("----------JEFE----------")

listaVendedores=(vendedor1,vendedor2)

listavendedores1=list(listaVendedores)

jefe1 = Jefe("Oscar","Ramirez Gomez","58421687U","Calle f 6",681038490,25000,"Marco","Jefe",secretario1,listavendedores1,coche3,"Jefe")

jefe1.bajaVendedor(1)
jefe1.incrementarSalarioJefe()
jefe1.cambiarSecretario(secretario2)

jefe1.mostrarJefe()
print("------------------------------")






