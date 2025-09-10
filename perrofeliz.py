# hacerperrofeliz
class Perro:
    def __init__(self, edad, nombre, color_ojos):
        self.edad = edad
        self.nombre = nombre
        self.color_ojos = color_ojos

     
        self.acariciado = False
        self.alimentado = False
        self.paseado = False

    def acariciar(self):
        self.acariciado = True
        print(f"Acariciando a {self.nombre}")

    def pasear(self):
        self.paseado = True
        print(f"{self.nombre} está paseando!")

    def alimentar(self):
        self.alimentado = True
        print(f"Alimentando a {self.nombre}")

    def hacer_feliz(self):
        if self.acariciado and self.alimentado and self.ladrado:
            print(f"{self.nombre} está feliz!")
        else:
            print(f"{self.nombre} no está feliz aún.")
mi_perro = Perro(5, "Rex", "marrón")
x=True
while x== True:
    opcion = int(input("Ingrese la que actividad quiere que haga su perro: 1. Acariciar, 2. Alimentar, 3. Pasear, 4. Hacer feliz, 5. Salir: "))
    match opcion:
        case 1:
            mi_perro.acariciar()
        case 2:
            mi_perro.alimentar()
        case 3:
            mi_perro.pasear()
        case 4:
            mi_perro.hacer_feliz()
        case 5:
            x=False
