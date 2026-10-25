import math
side_a = float(input("sibe_a (square metres): "))
side_b = float(input("side_b (square metres): "))
hypotenuse = math.hypot(side_a, side_b)

if side_a <= 0 or side_b <= 0:
    print("Each side must be greater than zero.")
else:
    print(f"hypotenuse: {hypotenuse:.2f} m")