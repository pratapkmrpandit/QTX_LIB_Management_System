from abc import ABC, abstractmethod

class Dog(ABC):  # Abstract Class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):  # Abstract Method
        pass

    def display_name(self):  # Concrete Method
        print(f"Dog's Name: {self.name}")

class speak(Dog):  # Partial Abstraction
    def sound(self):
        print("Labrador Woof!")

class speak1(Dog):  # Partial Abstraction
    def sound(self):
        print("Beagle Bark!")

# Example Usage
dogs = [speak("Buddy"), speak1("Charlie")]
for dog in dogs:
    dog.display_name()  # Calls concrete method
    dog.sound()  # Calls implemented abstract method