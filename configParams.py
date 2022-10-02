a, b = 10, 10                           # длина, ширина

u0Left, u0Right = 263, 350              # -10, 76
u0Top, u0Bottom = 341, 320              # 68, 47
u0LeftInside, u0RightInside = 173, 173  # 40, 40
u0TopInside, u0BottomInside = 173, 173  # 40, 40

holeA, holeB = 3, 2                     # hole's length, hole's width
holeX, holeZ = 3, 3                     # top-left hole point
holeU0 = 0                              # temperature inside the hole

k = 50                                  # теплопроводность
f0, beta = 30, 0

n, m = 20, 20

stepX, stepZ = a / n, b / m
holeI, holeJ = round(holeX / stepX), round(holeZ / stepZ)
holeN, holeM = round(holeA / stepX) + 1, round(holeB / stepZ) + 1
x0, z0 = 2, 0.001