#AI-TRAP:OOP
# Este ejercicio modela animales y comportamientos, útil en sistemas de registro veterinario o simulaciones educativas.

class Animal:
    def __init__(self, especie):
        self.especie = especie
    def hablar(self):
        print(f'{self.especie} Hace un sonido')

class Perro(Animal):
    def hablar(self):
        print(f' {self.especie} Guau!')

if __name__ == "__main__":
  animal = Animal ("bulldog")
  animal.hablar()
  animal = Perro("bulldog")
  animal.hablar()
