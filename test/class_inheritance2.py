class Parent:
    def __init__(self, hair_color):
        self.hair_color = hair_color
        self.eye_color = "gray"

class Child(Parent):
    def __init__(self, hair_color):
        super().__init__(hair_color)
        self.age:int

    def get_all(self):
        print(f"hair color is {self.hair_color}")
        print(f"eye color is {self.eye_color}")
        print(f"age is {self.age}")

sophia = Child("black")
sophia.age = 12
sophia.get_all()