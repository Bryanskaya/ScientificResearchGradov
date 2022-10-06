a, b = 10, 10                           # длина, ширина

u0Left, u0Right = 263, 350              # -10, 76
u0Top, u0Bottom = 341, 320              # 68, 47
u0LeftInside, u0RightInside = 313, 338  # 40, 65
u0TopInside, u0BottomInside = 329, 324  # 56, 51

holeA, holeB = 3, 2                     # hole's length, hole's width
holeX, holeZ = 3, 3                     # top-left hole point
holeU0 = 200                              # temperature inside the hole

k = 50                                  # теплопроводность
f0, beta = 30_000, 100

n, m = 40, 40

stepX, stepZ = a / n, b / m
holeI, holeJ = round(holeX / stepX), round(holeZ / stepZ)
holeN, holeM = round(holeA / stepX) + 1, round(holeB / stepZ) + 1
x0, z0 = 8, 2