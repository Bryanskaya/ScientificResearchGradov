a, b = 10, 10                           # длина, ширина

u0Left, u0Right = 313, 345              # -10, 76
u0Top, u0Bottom = 313, 313              # 68, 47
u0LeftInside, u0RightInside = 313, 313  # 40, 65
u0TopInside, u0BottomInside = 313, 313  # 56, 51

holeA, holeB = 3, 2                     # hole's length, hole's width
holeX, holeZ = 3, 3                     # top-left hole point
holeU0 = 200                              # temperature inside the hole

k = 10                                  # теплопроводность
f0, beta = 1_000, 0.3

n, m = 60, 60

stepX, stepZ = a / n, b / m
holeI, holeJ = round(holeX / stepX), round(holeZ / stepZ)
holeN, holeM = round(holeA / stepX) + 1, round(holeB / stepZ) + 1
x0, z0 = 8, 2