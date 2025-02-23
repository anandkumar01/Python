from abc import ABC, abstractmethod

# Define an abstract base class (ABC) for Car
class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def play_music(self):
        pass


# Maruti class implementing the Car interface
class Maruti(Car):

    def __init__(self, model_name, year):
        self.model_name = model_name
        self.year = year

    def start(self):
        print(f"{self.model_name} is starting with a key ignition.")

    def stop(self):
        print(f"{self.model_name} is stopping with manual brakes.")

    def accelerate(self):
        print(f"{self.model_name} is accelerating manually.")

    def display_info(self):
        print(f"Maruti Model: {self.model_name}, Year: {self.year}")

    def play_music(self):
        print(f"{self.model_name} is playing music.")


# Volvo class implementing the Car interface
class Volvo(Car):

    def __init__(self, model_name, year):
        self.model_name = model_name
        self.year = year

    def start(self):
        print(f"{self.model_name} is starting with a button.")

    def stop(self):
        print(f"{self.model_name} is stopping with automatic brakes.")

    def accelerate(self):
        print(f"{self.model_name} is accelerating automatically.")

    def display_info(self):
        print(f"Volvo Model: {self.model_name}, Year: {self.year}")

    def play_music(self):
        print(f"{self.model_name} is playing music.")


# Main function to demonstrate polymorphism
if __name__ == "__main__":
    maruti = Maruti("Maruti 800", 2018)
    maruti.start()
    maruti.accelerate()
    maruti.play_music()
    maruti.display_info()
    maruti.stop()

    print("\n")

    volvo = Volvo("Volvo XC90", 2023)
    volvo.start()
    volvo.accelerate()
    volvo.play_music()
    volvo.display_info()
    volvo.stop()
