class Cost():
    def __init__(self):
        self.total = 0
    def Add(self, value):
        self.total += value
    def ToString(self):
        return f"{self.total}"

