import unittest
from animals import *

class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.animal = Animal()
        self.animal.legs = 2
        self.dog = Dog(self.animal)
        self.dog.legs = 4

    def test_AnimalMustHaveName(self):
        random_animal = Animal("Reilly")
        self.assertEqual(random_animal.name, "Reilly")

    def test_AnimalMustHaveSpecies(self):
        random_animal = Animal("Reilly", "Cairn")
        self.assertEqual(random_animal.species, "Cairn")

    def test_InvokingWalkMethodSetsCorrectSpeedOnAnimalAndDog(self):
        animal_start_speed = self.animal.speed
        dog_start_speed = self.dog.speed
        self.animal.walk()
        self.dog.walk()
        self.assertEqual(self.animal.speed, animal_start_speed + (0.1 * self.animal.legs))
        self.assertEqual(self.dog.speed, dog_start_speed + (0.2 * self.dog.legs))

    def test_animalIsAnInstanceOfAnimal(self):
        self.assertIsInstance(self.animal, Animal)

    def test_dogIsAnInstanceOfDog(self):
        self.assertIsInstance(self.dog, Dog)


if __name__ == '__main__':
    unittest.main()


