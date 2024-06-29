class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, floor):
        if floor <= 0 or floor > self.number_of_floors:
                print("Такого этажа не существует")
        else:
            for j in range(1, floor + 1):
                print(j)




h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

