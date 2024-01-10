import random

class Pou:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = 0
        self.energy = 0
        self.happiness = 0
        self.health = 100  # Establecer salud inicial en 100
        self.alive = True

    def status(self):
        print("Nombre:", self.name)
        print("Edad:", self.age)
        print("Hambre:", self.hunger)
        print("Energía:", self.energy)
        print("Felicidad:", self.happiness)
        print("Salud:", self.health)

    def __str__(self):
        return f"Nombre: {self.name}\nEdad: {self.age}\nHambre: {self.hunger}\nEnergía: {self.energy}\nFelicidad: {self.happiness}\nSalud: {self.health}"

    def minmax(self, valor, valor_minimo, valor_maximo):
        return max(min(valor, valor_maximo), valor_minimo)

    def jugar(self):
        if self.energy >= 5 and self.hunger >= 3:
            print(f"{self.name} está jugando.")
            self.hunger = self.minmax(self.hunger - 3, 0, 100)
            self.energy = self.minmax(self.energy - 5, 0, 100)
            self.happiness = self.minmax(self.happiness + 7, 0, 100)
            self.health = self.minmax(self.health + 2, 0, 100)
        else:
            print(f"{self.name} no tiene suficiente energía o está demasiado hambriento para jugar.")

    def comer(self):
        comida = random.randint(5, 15)
        print(f"{self.name} está comiendo.")
        self.hunger = self.minmax(self.hunger - comida, 0, 100)
        self.energy = self.minmax(self.energy + 3, 0, 100)
        self.health = self.minmax(self.health + 2, 0, 100)

    def dormir(self):
        print(f"{self.name} está durmiendo.")
        self.energy = self.minmax(self.energy + 10, 0, 100)
        self.health = self.minmax(self.health + 5, 0, 100)

toto = Pou("Toto")

while toto.alive:
    toto.status()
    opcion = input("¿Qué quieres hacer? (jugar, comer, dormir, salir): ").lower()

    if opcion == "jugar":
        toto.jugar()
    elif opcion == "comer":
        toto.comer()
    elif opcion == "dormir":
        toto.dormir()
    elif opcion == "salir":
        break
    else:
        print("Opción inválida. Por favor, elige jugar, comer, dormir o salir.")

    # Lógica de envejecimiento (puedes personalizarla según tus necesidades)
    toto.age += 1
    toto.hunger = toto.minmax(toto.hunger + 2, 0, 100)
    toto.energy = toto.minmax(toto.energy - 2, 0, 100)
    toto.happiness = toto.minmax(toto.happiness - 1, 0, 100)
    toto.health = toto.minmax(toto.health - 1, 0, 100)

    # Verificar si Pou sigue vivo
    if toto.health <= 0:
        toto.alive = False
        print(f"{toto.name} ya no está vivo. ¡Fin del juego!")
