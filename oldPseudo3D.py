import win32console, win32con, time
from os import system
from win32api import GetAsyncKeyState as keypress
# from win32con import *

screen = ""

arrow = {'left':0x25, 'up':0x26, 'right':0x27, 'down':0x28}

world = list()

ax = 45
ay = 45
az = 45
d = 9

delay = 0.01

c = 45

sp1 = {
"h" : ax//2,
"j" : ay//2,
"k" : az//2,
"r" : 7}

sp1["dif"] = 9
sp1["rs"] = sp1["r"]**2
sp1["rx"] = sp1["rs"] + sp1["dif"]
sp1["rn"] = sp1["rs"] - sp1["dif"]

sp2 = {
"h" : ax//4,
"j" : ay//4,
"k" : az//4,
"r" : 3}

sp2["dif"] = 7
sp2["rs"] = sp2["r"]**2
sp2["rx"] = sp2["rs"] + sp2["dif"]
sp2["rn"] = sp2["rs"] - sp2["dif"]

for x in range(ax):
    plane = list()
    for y in range(ay):
        line = list()
        for z in range(az):
            if x == 0 or y == 0 or z == 0 or x == ax-1  or y == ay-1  or z == az-1:
                line.append("#")
            elif x%c == 0 or y%c == 0 or z%c == 0:
                line.append("#")
            elif (x-sp1["h"])**2 + (y-sp1["j"])**2 + (z-sp1["k"])**2 < sp1["rx"]:
                line.append("#")
            elif (x-sp2["h"])**2 + (y-sp2["j"])**2 + (z-sp2["k"])**2 < sp2["rx"] and (x-sp2["h"])**2 + (y-sp2["j"])**2 + (z-sp2["k"])**2 > sp2["rn"]:
                line.append("#")
            else:
                line.append(" ")
        plane.append(line)
    world.append(plane)

cp = ax//2

#▒░

charlist = "█▓@&$?+/,"

for i in range(ax - len(charlist)):
    charlist += " "

d = 9
mz = 1
my = 1

def addSliceToScreen():
    templist = list()
    for y in range(ay):
        for z in range(az):
            if world[cp][y][z] == " ":
                for i in range(d):
                    test = False
                    try:
                        test = world[cp-i][y-int(i*my)][z-int(i*mz)] == "#"
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

system('mode ' + str(az) + ',' + str(ay))
system('color 1E')
myConsole = win32console.CreateConsoleScreenBuffer(DesiredAccess = win32con.GENERIC_READ | win32con.GENERIC_WRITE, ShareMode=0, SecurityAttributes=None, Flags=1) # create screen buffer
myConsole.SetConsoleActiveScreenBuffer() # set this buffer to be active

stop = False

while True:
    if cp >= ax:
        cp = ax-1
    elif cp < 0:
        cp = 0
    screen = addSliceToScreen()
    myConsole.WriteConsoleOutputCharacter(Characters=screen, WriteCoord=win32console.PyCOORDType(0,0))
    
    if keypress(arrow['up']):
        my += 0.05
    if keypress(arrow['down']):
        my -= 0.05
    if keypress(arrow['left']):
        mz += 0.05
    if keypress(arrow['right']):
        mz -= 0.05
    if keypress(ord('W')):
        cp += 1
    if keypress(ord('S')):
        cp -= 1
    time.sleep(delay)

input()
