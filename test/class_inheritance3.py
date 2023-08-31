class a():
    def __init__(self):
        self.num = 3
        self.total = 10


class b(a):
    def __init__(self):
        super().__init__()
        self.shape = 'circle'

object_b = b()
print(object_b.num)