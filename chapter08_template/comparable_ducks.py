class ComparableDuck:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'{self.name} weight: {self.weight}'

    def __lt__(self, other):
        if self.weight == other.weight:
            return self.name < other.name
        return self.weight < other.weight

    # def __le__(self, other):
    #     return self.weight <= other.weight


if __name__ == '__main__':
    ducks = [
        ComparableDuck('Daffy', 8),
        ComparableDuck('Dewey', 2),
        ComparableDuck('Howard', 7),
        ComparableDuck('Louie', 2),
        ComparableDuck('Donald', 10),
        ComparableDuck('Huey', 2),
    ]
    print(ducks)

    ducks.sort()
    print(ducks)
