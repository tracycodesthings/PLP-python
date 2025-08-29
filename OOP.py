class celebrity:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def introduce(self):
        return f"Hello, I'm {self.name}, a {self.age}-year-old {self.profession}."
    
    class actor:
        def __init__(self, name, age, profession, movies):
            super().__init__(name, age, profession)
            self.movies = movies

        def introduce(self):
            base_intro = super().introduce()
            return f"{base_intro} I've acted in {', '.join(self.movies)}."
        
    class musician:
        def __init__(self, name, age, profession, albums):
            super().__init__(name, age, profession)
            self.albums = albums

        def introduce(self):
            base_intro = super().introduce()
            return f"{base_intro} I've released the albums: {', '.join(self.albums)}."
        
    class athlete:
        def __init__(self, name, age, profession, sport):
            super().__init__(name, age, profession)
            self.sport = sport

        def introduce(self):
            base_intro = super().introduce()
            return f"{base_intro} I play {self.sport} professionally."
        
        celebrities = [
    Actor("Zendaya", 28, ["Dune", "Spider-Man"]),
    Athlete("Serena Williams", 42, "Tennis")
]

for celeb in celebrities:
    print(celeb.introduce())
    print(celeb.perform())

class Celebrity:
    def __init__(self, name, profession, age, net_worth):
        self.name = name
        self.profession = profession
        self.age = age
        self.__net_worth = net_worth  # private attribute

    def introduce(self):
        return f"I'm {self.name}, a {self.profession}."

    def get_net_worth(self):
        return f"{self.name}'s net worth is ${self.__net_worth} million."

    def add_income(self, amount):
        self.__net_worth += amount
class Vehicle:
    def start_engine(self):
        print("Starting engine of generic vehicle...")

class Car(Vehicle):
    def start_engine(self):
        print("Starting engine of the car... Vroom!")

class Bike(Vehicle):
    def start_engine(self):
        print("Starting engine of the bike... Brrrm!")

# Function that uses polymorphism
def start_vehicle(vehicle):
    vehicle.start_engine()

# Create objects
my_car = Car()
my_bike = Bike()

# Use polymorphism
start_vehicle(my_car)   # Output: Starting engine of the car... Vroom!
start_vehicle(my_bike)  # Output: Starting engine of the bike... Brrrm!

    
    
    
