
class Animal:
    def __init__(self, name):
        self.name = name
        self.animal_voice = ""
        self.weight = 0

    def feed_the_animal(self):
        print(f'{self.name} кушает.')

    def voice(self):
        print(f'{self.name} говорит "{self.animal_voice}"')


class DairyAnimal(Animal):
    def milking(self):
        print(f'{self.name}  подоена.')


class Cow(DairyAnimal):
    def __init__(self, name):
        super().__init__(name)
        self.animal_voice = "Муууу"


class Goat(DairyAnimal):
    def __init__(self, name):
        super().__init__(name)
        self.animal_voice = "Мееее"


class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.animal_voice = "Бееее"

    def shearing(self):
        print(f'{self.name} острижена.')


class Bird(Animal):
    def get_the_egg(self):
        print(f'У {self.name} собраны яйца.')


class Goose(Bird):
    def __init__(self, name):
        super().__init__(name)
        self.animal_voice = "Га-га-га"


class Hen(Bird):
    def __init__(self, name):
        super().__init__(name)
        self.animal_voice = "Ко-ко-ко"


class Duck(Bird):
    def __init__(self, name):
        super().__init__(name)
        self.animal_voice = "Кря-кря-кря"


if __name__ == '__main__':
    Seriy = Goose("Серый")
    Seriy.feed_the_animal()
    Seriy.get_the_egg()

    Beliy = Goose("Серый")
    Beliy.feed_the_animal()
    Beliy.get_the_egg()

    Mania = Cow("Маня")
    Mania.feed_the_animal()
    Mania.milking()
    
    Barashek = Sheep("Барашек")
    Barashek.feed_the_animal()
    Barashek.shearing()
    
    Kydriaviy = Sheep("Кудрявый")
    Kydriaviy.feed_the_animal()
    Kydriaviy.shearing()
    
    Koko = Hen("Ко-Ко")
    Koko.feed_the_animal()
    Koko.get_the_egg()

    Kukareky = Hen("Кукареку")
    Kukareky.feed_the_animal()
    Kukareky.get_the_egg()

    Roga = Goat("Рога")
    Roga.feed_the_animal()
    Roga.milking()

    Kopyta = Goat("Копыта")
    Kopyta.feed_the_animal()
    Kopyta.milking()
    
    Kruakva = Duck("Кряква")
    Kruakva.feed_the_animal()
    Kruakva.get_the_egg()
