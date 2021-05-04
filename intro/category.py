class Category:
    def __init__(self, name): # TODO: , products):
        self.name = name

    def __str__(self):
        return f"There are no products in {self.name}"