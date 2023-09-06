# 09/06/23
# Class Chart

def format(name, grade, age, favCereal):
    print("{}\t{}\t{}\t{}".format(name, grade, age, favCereal))

print("Mrs. Goodman's Python Class")
print("--------------------------------------------------------")
print("Name:\tGrade:\tAge:\tFavorite Cereal:")
format("Christian", 11, 16, "Fruity Pebbles")

data = []

for i in range(16):
    name, grade, age, favCereal = eval(input())
    data.append(format(data))

for item in data:
    # You don't want to type in everything in the input, trust me, just have it hard coded
    print(item)