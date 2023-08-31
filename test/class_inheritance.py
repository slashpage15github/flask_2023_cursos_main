class Parent:
    def __init__(self):
        self.eye_color = "black"

class Child(Parent):
    pass

sophia = Child()
print(sophia.eye_color)