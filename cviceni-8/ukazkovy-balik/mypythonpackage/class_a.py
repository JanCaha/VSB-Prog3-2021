class A:

    def __init__(self, value: float):
        self.value = value

    def add_one(self):

        self.value += 1

    def __repr__(self):
        return str(self.value)
