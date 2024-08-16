# class Hat:
#     def __init__(self, kind, color, material):
#         self.kind = kind
#         self.color = color
#         self.material = material
# myobject = Hat("tophat", "brown", "leather")

# class Fruit:
#     def __init__(self, shape, kind, size):
#         self.shape = shape
#         self.kind = kind
#         self.size = size
# f1 = Fruit("round", "apple", "4")
# f2 = Fruit("round", "watermelon", "12")
# f3 = Fruit("round", "orange", "5")
# f4 = Fruit("round", "lemon", "4")
# print(f1.kind)
# print(f2.kind)
# print(f3.kind)
# print(f4.kind)

# class Pet:
#     def __init__(self, name, size, color):
#         self.name = name
#         self.size = size
#         self.color = color
# p1 = Pet("a", "1", "b")
# p2 = Pet("c", "2", "d")
# p3 = Pet("e", "3", "f")

class Vacation:
    def __init__(self, location, activity, food):
        self.location = location
        self.activity = activity
        self.food = food

v1 = Vacation("a", "b", "c")
v2 = Vacation("a", "b", "c")
v3 = Vacation("a", "b", "c")

print(v1.location + " test")
print(v2.activity +  " test")
print(v3.food + " test")
