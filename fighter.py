# Object class for a fighter

class Fighter:
    def __init__(self, name, description, tecnique_name, stamina, punchforce, guts, tecnique, nimble, tough, books):
        self.name = name
        self.description = description
        self.tecnique_name = tecnique_name
        self.stamina = stamina
        self.punchforce = punchforce
        self.guts = guts
        self.tecnique = tecnique
        self.nimble = nimble
        self.tough = tough
        self.books = books

    def __str__(self):
        return self.name + ': ' + self.description

    def announce(self):
        print(f'{self.__str__()}')