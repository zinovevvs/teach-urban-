class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, floor):
        if floor <= 0 or floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for j in range(1, floor + 1):
                print(j)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        return self + value

    def __radd__(self, value):
        return self + value

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __del__(self):
        print(f'{self.name}, снесён, но он останется в истории')
        return


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
# # h1.go_to(5)
# # h2.go_to(10)
# # print(h1)
# # print(h2)
# # print(len(h1))
# # print(len(h2))
# # print(h1 == h2)  # __eq__
# #
# # h1 = h1 + 10 # __add__
# # print(h1)
# # print(h1 == h2)
# #
# # h1 += 10 # __iadd__
# # print(h1)
# #
# # h2 = 10 + h2 # __radd__
# # print(h2)
# #
# # print(h1 > h2) # __gt__
# # print(h1 >= h2) # __ge__
# # print(h1 < h2) # __lt__
# # print(h1 <= h2) # __le__
# # print(h1 != h2) # __ne__
