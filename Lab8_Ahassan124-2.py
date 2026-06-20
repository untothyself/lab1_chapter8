"""
Program:Calculator
author: Abass Hassan
purpose: calculate area and permeter of shape
date: june 2026
"""
import circle as c
import rectangle as r

while True:
    shape = input("Enter the shape (circle or rectangle) or 'exit' to quit: ").lower()
    
    if shape == 'exit':
        print("Exiting the program.")
        break
    elif shape == 'circle':
        radius = float(input("Enter the radius of the circle: "))
        area = c.calc_area(radius)
        circumference = c.calc_circumference(radius)
        print(f"Area of the circle: {area}")
        print(f"Circumference of the circle: {circumference}")
