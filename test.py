# text = open("world.txt").read()
# newtext = ""
# for t in text:
#     if t != "\n":
#         newtext += t
# print(newtext)
# input()


# text = "".join(list(i if i != "\n" else "" for i in open("world.txt").read()))
# print(len(text)**(1.00000000000000012/3))
# input()


# class MyList(list):
#     def __getitem__(self, key):
#         return super(MyList, self).__getitem__(self, key-1)

# newlist = MyList([5,4,3,2,1,0])

# print(newlist[6])
# input()


worldstring = "".join(list(i if i != "\n" else "" for i in open("world.txt").read()))

depth = 45
height = 45
width = 45

world = []

for i in range(depth):
    plane = []
    for j in range(height):
        line = []
        for k in range(width):
            line.append(worldstring[i*height*width + j*width + k])
        plane.append(line)
    world.append(plane)

print(world)
input()
