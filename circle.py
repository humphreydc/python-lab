import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


radius_input = float(input("Enter the radius of the circle: "))
louise_circle = Circle(radius_input)

print(f"\nFor a circle with radius {louise_circle.radius:.2f}:")
print(f"Area: {louise_circle.area():.2f}")
print(f"Circumference: {louise_circle.circumference():.2f}")

print("\nBible verse:")
print("\"Para sa lahat ng bagay ay may kakayahan ako sa pamamagitan niya na nagpapalakas sa akin.” – Philippians 4:13")
