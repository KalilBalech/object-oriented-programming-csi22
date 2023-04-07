

class Animal:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'im an animal'

class LandAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def breath(self):
        print(self.name + ' is breathing air')


class WaterAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def breath(self):
        print(self.name + ' is breathing under water')


class Frog(LandAnimal, WaterAnimal):
    def __init__(self, name):
        super().__init__(name)

class Tartaruga(WaterAnimal, LandAnimal):
    def __init__(self, name):
        super().__init__(name)

cachorro = Animal('Uber')

sapoArabe = Frog('Vinicius')
sapoArabe.breath()

tartarugaRussa = Tartaruga('Angelo')
tartarugaRussa.breath()

print('\n-----------------------------\n')

print(cachorro.__class__.mro())
print('\n')
print(sapoArabe.__class__.mro())
print('\n')
print(tartarugaRussa.__class__.mro())