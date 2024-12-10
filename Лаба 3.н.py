import math

x1 = 3
xn = 7
dx = 0.2
a = 1.9
b = 1.1

for x in range(int(x1 * 10), int(xn * 10 + 1), int(dx * 10)):
    x = x / 10
    y = math.sqrt((a * x) / (b + math.cos(x) ** 2))
    print(f"x = {x:.1f}, y = {y:.4f}")

while x <= xn:
    y = math.sqrt((a*x)/(b + math.cos(x)**2))
    print(f"x = {x:.1f}, y = {y:.4f}")
    x += dx