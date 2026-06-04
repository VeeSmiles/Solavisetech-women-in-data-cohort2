# Exercise 1: Personal Bio Generator
name = "Vivian Ndung'u"
age = 22
height = 1.67          # in metres
favorite_tech_field = "Data Analytics & Cybersecurity"
is_student = True

print("PERSONAL BIO GENERATOR")
print(f"Hi! My name is {name}.")
print(f"I am {age} years old and {height}m tall.")
print(f"My favourite tech field is {favorite_tech_field}.")
print(f"Currently a student: {is_student}")
print()

# Exercise 2: Type Checker
print("=" * 55)
print("               TYPE CHECKER")
print("=" * 55)

my_name      = "Vivian"
my_age       = 22
my_gpa       = 4.0
is_enrolled  = True
lucky_number = None

variables = {
    "my_name"     : my_name,
    "my_age"      : my_age,
    "my_gpa"      : my_gpa,
    "is_enrolled" : is_enrolled,
    "lucky_number": lucky_number,
}

for var_name, value in variables.items():
    print(f"  {var_name} = {repr(value):15}  -->  Type: {type(value).__name__}")
print()

# Exercise 3: Data Conversion
print("=" * 55)
print("              DATA CONVERSION")
print("=" * 55)

# Integer to String
year = 2026
year_as_string = str(year)
print(f"  Integer to String : {year} ({type(year).__name__}) "
      f"--> '{year_as_string}' ({type(year_as_string).__name__})")

# Float to Integer
temperature = 36.6
temp_as_int = int(temperature)
print(f"  Float to Integer  : {temperature} ({type(temperature).__name__}) "
      f"--> {temp_as_int} ({type(temp_as_int).__name__})")

# String number to Integer
score_str = "95"
score_int = int(score_str)
print(f"  String to Integer : '{score_str}' ({type(score_str).__name__}) "
      f"--> {score_int} ({type(score_int).__name__})")
print()

# Exercise 4: User Information
print("=" * 55)
print("             USER INFORMATION")
print("=" * 55)

user_name    = input("  Enter your name    : ")
user_age     = input("  Enter your age     : ")
user_country = input("  Enter your country : ")

print()
print(f"  Welcome, {user_name}! 🌍")
print(f"  You are {user_age} years old and you're joining us from {user_country}.")
print(f"  Glad to have you in the Solavise Women in Data community!")
print()


# Exercise 5: Temperature Converter (Celsius to Fahrenheit)
print("=" * 55)
print("           TEMPERATURE CONVERTER")
print("=" * 55)

celsius_input = float(input("  Enter temperature in Celsius: "))
fahrenheit = (celsius_input * 9 / 5) + 32

print(f"\n  {celsius_input}°C  =  {fahrenheit:.2f}°F")

if fahrenheit < 32:
    print("  🥶 Freezing cold! Bundle up.")
elif fahrenheit < 59:
    print("  🧥 Cool weather. A jacket would help.")
elif fahrenheit < 77:
    print("  😊 Comfortable temperature!")
elif fahrenheit < 95:
    print("  ☀️  Warm day. Stay hydrated!")
else:
    print("  🔥 Very hot! Stay in the shade.")
print()