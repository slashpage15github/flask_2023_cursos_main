class Teacher:
    def __init__(self, subject):
        self.subject = subject

    def teach(self):
        return f"teaching {self.subject}"