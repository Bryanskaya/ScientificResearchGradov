a, b = 20, 10                           # длина, ширина

u0Left, u0Right = 313, 313              # 40
u0Top, u0Bottom = 313, 313              # 40
u0LeftInside, u0RightInside = 313, 313  # 40
u0TopInside, u0BottomInside = 313, 313  # 40

holeA, holeB = 10, 2                     # hole's length, hole's width
holeX, holeZ = 5, 3                     # top-left hole point
holeU0 = 200                              # temperature inside the hole

k = 10                                  # теплопроводность
f0, beta = 1_000, 0.3

n, m = 60, 30  # simple Jacobi 30 15
# n, m = 200, 100  # parallel Jacobi

stepX, stepZ = a / n, b / m
holeI, holeJ = round(holeZ / stepZ), round(holeX / stepX)
holeN, holeM = round(holeA / stepX) + 1, round(holeB / stepZ) + 1
x0, z0 = 3, 7

# Специально для Монте-Карло
iStart, jStart = 4, 3
nItems = 100
