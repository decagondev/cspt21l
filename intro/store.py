class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories
    
    def __str__(self):
        output = f"{self.name}\n"
        for i, cat in enumerate(self.categories):
            output += f"   [{i + 1}] {cat}\n"
        
        output += f"   [{i + 2}] Exit\n"
        return output




my_store = Store("My Store", ["Clothes", "Baseball", "Hockey"])
selection = 0
while selection != len(my_store.categories) + 1:
    print(my_store)
    try:
        selection = int(input("Select a the number of the department you would like to enter "))
        if selection == len(my_store.categories) + 1:
            print("Thanks for shopping!")
        elif selection > 0 and selection <= len(my_store.categories):
            print(my_store.categories[selection - 1])
        else:
            print("Please select a valid number")
    except ValueError:
        print("please enter you choice as a number.")