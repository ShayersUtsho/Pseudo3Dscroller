import win32console, win32con, time
from os import system
from win32api import GetAsyncKeyState as keypress
# from win32con import *

screen = ""

arrow = {'left':0x25, 'up':0x26, 'right':0x27, 'down':0x28}

delay = 0.02

depth = 45
height = 45
width = 45

renderDepth = 45
renderHeight = 45
renderWidth = 45

renderposixionX = 0
renderpositionY = 0
renderpositionZ = 0

worldstring = "".join(list(i if i != "\n" else "" for i in open("world.txt").read()))

world = [[[worldstring[i*height*width + j*width + k] for k in range(width)] for j in range(height)] for i in range(depth)]

# cx = 20
# cy = 20
# cz = 20
# for x in range(depth):
#     plane = list()
#     for y in range(height):
#         line = list()
#         for z in range(width):
#             if x == 0 or y == 0 or z == 0 or x == depth-1  or y == height-1  or z == width-1:
#                 line.append("#")
#             elif y%cy == 0 or x%cx == 0 or z%cz == 0:
#                 line.append("#")
#             else:
#                 line.append(" ")
#         plane.append(line)
#     world.append(plane)

current_plane = depth//2

charlist1 = "█▓@&$?+/,."
charlist = ""
shade_multiplier = 1

for ch in charlist1:
    charlist += ch * shade_multiplier

for i in range(depth - len(charlist)):
    charlist += " "

horizontalAngle = 0.5
verticalAngle = -0.5

def addSliceToScreen():
    templist = list()
    for y in range(renderHeight):
        for z in range(renderWidth):
            if world[current_plane][y][z] == " ":
                for i in range(renderDepth):
                    test = False
                    try:
                        test = world[current_plane-i][y-int(i*verticalAngle)][z-int(i*horizontalAngle)] == "#"
                    except:
                        test = False
                    if test:
                         templist.append(charlist[i])
                         break
                else:
                    templist.append(" ")
            else:
                templist.append(charlist[0])
    return "".join(templist)

def addTextToScreen(text, startingX = 0, startingY = 0):
    return screen[0 : startingX + startingY * renderWidth] + text + screen[startingX + startingY * renderWidth + len(text) : len(screen)]

system('mode ' + str(renderWidth) + ',' + str(renderHeight))
system('color 1E')
myConsole = win32console.CreateConsoleScreenBuffer(DesiredAccess = win32con.GENERIC_READ | win32con.GENERIC_WRITE, ShareMode=0, SecurityAttributes=None, Flags=1) # create screen buffer
myConsole.SetConsoleActiveScreenBuffer() # set this buffer to be active

stop = False

while True:
    if current_plane >= depth:
        current_plane = depth-1
    elif current_plane < 0:
        current_plane = 0
    if horizontalAngle > 1.0:
        horizontalAngle = 1.0
    if horizontalAngle < -1.0:
        horizontalAngle = -1.0
    if verticalAngle > 1.0:
        verticalAngle = 1.0
    if verticalAngle < -1.0:
        verticalAngle = -1.0
    screen = addSliceToScreen()
    # screen = addTextToScreen(str(horizontalAngle) + " " + str(verticalAngle), 5,5)
    myConsole.WriteConsoleOutputCharacter(Characters=screen, WriteCoord=win32console.PyCOORDType(0,0))
    
    if keypress(arrow['up']) and verticalAngle < 1.0:
        verticalAngle += 0.05
    if keypress(arrow['down']) and verticalAngle > -1.0:
        verticalAngle -= 0.05
    if keypress(arrow['left']) and horizontalAngle < 1.0:
        horizontalAngle += 0.05
    if keypress(arrow['right']) and horizontalAngle > -1.0:
        horizontalAngle -= 0.05
    if keypress(ord('W')) and current_plane < depth:
        current_plane += 1
    if keypress(ord('S')) and current_plane > 0:
        current_plane -= 1
    time.sleep(delay)

input()
