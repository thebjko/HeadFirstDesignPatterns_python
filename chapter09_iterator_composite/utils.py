class MockArray(list):
    def __init__(self, max_items: int):
        super().__init__()
        self.MAX_ITEMS = max_items
        self.length = 0

    def append(self, item):
        if len(self) < self.MAX_ITEMS:
            super().append(item)
            self.length += 1
        else:
            raise Exception("Capacity exceded. Can't add more item.")

    def pop(self, idx = None):
        if idx is None:
            x = super().pop()
        else:
            x = super().pop(idx)
        self.length -= 1
        return x
