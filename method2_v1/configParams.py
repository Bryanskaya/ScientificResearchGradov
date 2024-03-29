# Генератор
rangeRight = [0, 0.25]                  # [0; 0.25)
rangeBottom = [0.25, 0.5]               # [0.25; 0.5)
rangeLeft = [0.5, 0.75]                 # [0.5; 0.75)
rangeTop = [0.75, 1]                    # [0.75; 1)

#------------------------------------------------------
a, b = 20, 10                           # длина, ширина

u0Left, u0Right = 313, 313              # -10, 76
u0Top, u0Bottom = 313, 313              # 68, 47
u0LeftInside, u0RightInside = 313, 313  # 40, 65
u0TopInside, u0BottomInside = 313, 313  # 56, 51

holeA, holeB = 10, 2                     # hole's length, hole's width
holeX, holeZ = 5, 3                     # top-left hole point
holeU0 = 200                              # temperature inside the hole

k = 10                                  # теплопроводность
f0, beta = 1_000, 0.3

n, m = 40, 20

stepX, stepZ = a / n, b / m
holeI, holeJ = round(holeZ / stepZ), round(holeX / stepX)
holeN, holeM = round(holeA / stepX) + 1, round(holeB / stepZ) + 1
x0, z0 = 3, 7

#--------------------------
iStart, jStart = 4, 3
nItems = 100