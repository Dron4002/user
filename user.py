class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self, age, city, pole, family_status):
        self.age = age
        self.city = city
        self.pole = pole
        self.family_status = family_status
        if city == 'Ryazan' and pole == 'woman':

            print(f"Hello, my name is {self.first_name} {self.last_name}, I'm {age}. I'm {pole}, I'm from {city} and {family_status}")
        else:
            print(f"Hello, my name is {self.first_name} {self.last_name}, I'm {age}. I'm {pole}, I'm from {city} and {family_status}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")
user1 = User("Andrew", "Bylenok")
user2 = User("Artem", "Oshchepkov")
user3 = User("Alina", "Makarova")
user1.greet_user()
user1.describe_user("17 years old", "Bryansk", "man", "not married")
user2.greet_user()
user2.describe_user("16 years old", "Bryansk", "man", "not married")
user3.greet_user()
user3.describe_user("22 years old", "Ryazan", "woman", "not married")
