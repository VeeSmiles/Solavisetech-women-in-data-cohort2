import math

# Exercise 1: Simple Calculator
print("=" * 55)
print("             SIMPLE CALCULATOR")
print("=" * 55)

num1 = float(input("  Enter first number  : "))
num2 = float(input("  Enter second number : "))

print(f"\n  {num1} + {num2}  =  {num1 + num2}")
print(f"  {num1} - {num2}  =  {num1 - num2}")
print(f"  {num1} × {num2}  =  {num1 * num2}")

if num2 != 0:
    print(f"  {num1} ÷ {num2}  =  {num1 / num2:.4f}")
else:
    print("  Division by zero is not allowed! ⚠️")
print()

# Exercise 2: Area of Shapes
print("=" * 55)
print("              AREA OF SHAPES")
print("=" * 55)

# Circle
radius = float(input("  Circle  – enter radius         : "))
circle_area = math.pi * radius ** 2
print(f"  Area of circle    = {circle_area:.4f} sq units")

# Rectangle
length = float(input("  Rectangle – enter length        : "))
width  = float(input("  Rectangle – enter width         : "))
rect_area = length * width
print(f"  Area of rectangle = {rect_area:.4f} sq units")

# Triangle
base   = float(input("  Triangle – enter base           : "))
height = float(input("  Triangle – enter height         : "))
tri_area = 0.5 * base * height
print(f"  Area of triangle  = {tri_area:.4f} sq units")
print()

# Exercise 3: Even or Odd
print("=" * 55)
print("               EVEN OR ODD")
print("=" * 55)

number = int(input("  Enter a whole number : "))

if number % 2 == 0:
    print(f"  {number} is EVEN 🟢")
else:
    print(f"  {number} is ODD 🔵")
print()

# Exercise 4: Student Grade Percentage
print("=" * 55)
print("         STUDENT GRADE PERCENTAGE")
print("=" * 55)

marks_obtained = float(input("  Enter marks obtained : "))
total_marks    = float(input("  Enter total marks    : "))

if total_marks > 0:
    percentage = (marks_obtained / total_marks) * 100
    print(f"\n  Marks    : {marks_obtained} / {total_marks}")
    print(f"  Score    : {percentage:.2f}%")

    if percentage >= 70:
        print("  Result   : First Class Honours 🏆")
    elif percentage >= 60:
        print("  Result   : Second Class Upper 🥈")
    elif percentage >= 50:
        print("  Result   : Second Class Lower 🥉")
    elif percentage >= 40:
        print("  Result   : Pass")
    else:
        print("  Result   : Fail – keep pushing! 💪")
else:
    print("  Total marks cannot be zero! ⚠️")
print()

# Exercise 5: BMI Calculator
print("=" * 55)
print("               BMI CALCULATOR")
print("=" * 55)

weight_kg = float(input("  Enter your weight (kg) : "))
height_m  = float(input("  Enter your height (m)  : "))

if height_m > 0:
    bmi = weight_kg / (height_m ** 2)
    print(f"\n  Weight : {weight_kg} kg")
    print(f"  Height : {height_m} m")
    print(f"  BMI    : {bmi:.2f}")

    if bmi < 18.5:
        print("  Status : Underweight")
    elif bmi < 25.0:
        print("  Status : Normal weight ✅")
    elif bmi < 30.0:
        print("  Status : Overweight")
    else:
        print("  Status : Obese")
else:
    print("  Height cannot be zero! ⚠️")
print()

# Exercise 6: Power & Modulus
print("=" * 55)
print("            POWER & MODULUS")
print("=" * 55)

base_num = float(input("  Enter base number     : "))
exp_num  = float(input("  Enter exponent        : "))
mod_num  = int(input("  Enter modulus divisor : "))

power_result = base_num ** exp_num
print(f"\n  {base_num} ^ {exp_num}          = {power_result}")

if mod_num != 0:
    mod_result = int(base_num) % mod_num
    print(f"  {int(base_num)} mod {mod_num}            = {mod_result}")
    print(f"\n  💡 Modulus gives the remainder after division.")
    print(f"     {int(base_num)} ÷ {mod_num} = {int(base_num) // mod_num} remainder {mod_result}")
else:
    print("  Modulus divisor cannot be zero! ⚠️")
print()