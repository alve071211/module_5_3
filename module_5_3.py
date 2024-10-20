class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f"Название: {self.name}, количество этажей: {self.number_of_floors}")

    def __eq__(self, other):

        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        new_number_of_floors = self.number_of_floors + value
        return House(self.name, new_number_of_floors)

    def __radd__(self, value):
        new_number_of_floors = self.number_of_floors + value
        return House(self.name, new_number_of_floors)
    def __iadd__(self, value):
        new_number_of_floors = self.number_of_floors + value
        return House(self.name, new_number_of_floors)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10
print(h1)

print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 !=h2)



#     def __len__(self):
#         return self.number_of_floors
#     def __str__(self):
#         return (f"Название: {self.name}, количество этажей: {self.number_of_floors}")
#
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# print(h1)
# print(h2)
# print(len(h1))
# print(len(h2))

#     def go_to(new_floor):
#
#         if new_floor >= number_of_floors or new_floor <= 1:
#             print("Такого этажа не существует")
#         for i in range(1, number_of_floors + 1):
#             print(i)
#             if i == new_floor:
#                 break
#
# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
#
# h1.go_to(5)
# h2.go_to(10)



