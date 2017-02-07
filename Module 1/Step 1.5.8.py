class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.content = 0

    def can_add(self, v):
        return v <= (self.capacity - self.content)

    def add(self, v):
        self.content += v
