import time
import random

# Exercise 1: Age Eligibility Checker
print("AGE ELIGIBILITY CHECKER")

age = int(input("Enter your age : "))

if age < 0:
    print("Invalid age entered.")
elif age < 13:
    print(f"You are {age} years old — classified as a CHILD")
    print("Keep exploring and stay curious!")
elif age < 18:
    print(f"You are {age} years old — classified as a TEENAGER")
    print("Great time to start learning to code!")
elif age < 60:
    print(f"You are {age} years old — classified as an ADULT")
    print("Welcome to the world of data!")
else:
    print(f"You are {age} years old — classified as a SENIOR")
    print("Wisdom and experience — a powerful combination!")
print()

# Exercise 2: Password Validator
print("PASSWORD VALIDATOR")

password = input("Create a password : ")
length = len(password)

has_upper  = any(c.isupper() for c in password)
has_lower  = any(c.islower() for c in password)
has_digit  = any(c.isdigit() for c in password)
has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

print(f"Password length   : {length} characters")
print(f"Uppercase letter  : {'✅' if has_upper  else '❌'}")
print(f"Lowercase letter  : {'✅' if has_lower  else '❌'}")
print(f"Contains number   : {'✅' if has_digit  else '❌'}")
print(f"Special character : {'✅' if has_special else '❌'}")

score = sum([has_upper, has_lower, has_digit, has_special])

if length < 6:
    print("Strength : Too Short — minimum 6 characters required")
elif length < 8 or score < 2:
    print("Strength : WEAK — add numbers and special characters")
elif length < 12 or score < 3:
    print("Strength : MODERATE — getting better!")
else:
    print("Strength : STRONG — great password!")
print()


# Exercise 3: Grade Classification
print("GRADE CLASSIFICATION")

score = float(input("Enter your exam score (0–100) : "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a value between 0 and 100. ⚠️")
elif score >= 70:
    print(f"Score: {score}  -->  Grade: A  DISTINCTION")
elif score >= 60:
    print(f"Score: {score}  -->  Grade: B  MERIT")
elif score >= 50:
    print(f"Score: {score}  -->  Grade: C  CREDIT")
elif score >= 40:
    print(f"Score: {score}  -->  Grade: D  PASS")
else:
    print(f"Score: {score}  -->  Grade: F  FAIL – you've got this!")
print()

# Exercise 4: Multiplication Table
print("MULTIPLICATION TABLE")

num = int(input("Enter a number for its multiplication table : "))
print(f"Multiplication table for {num}:\n")

for i in range(1, 13):
    result = num * i
    print(f"  {num:>3} × {i:>2}  =  {result:>4}")
print()

# Exercise 5: Number Guessing Game
print("NUMBER GUESSING GAME")

secret_number = random.randint(1, 20)
attempts      = 0
max_attempts  = 5

print(f"I'm thinking of a number between 1 and 20.")
print(f"You have {max_attempts} attempts. Good luck!\n")

while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}/{max_attempts} — Your guess : "))
    attempts += 1

    if guess < secret_number:
        print(f"Too low! ({max_attempts - attempts} attempts left)\n")
    elif guess > secret_number:
        print(f"Too high! ({max_attempts - attempts} attempts left)\n")
    else:
        print(f"Correct! The number was {secret_number}.")
        print(f"You got it in {attempts} attempt(s)!")
        break
else:
    print(f"Game over! The secret number was {secret_number}. Better luck next time! 🎯")
print()

# Exercise 6: Countdown Timer
print("COUNTDOWN TIMER")

print("Launching countdown...\n")

for i in range(10, 0, -1):
    print(f"  {'🔟' if i == 10 else '9️⃣' if i == 9 else '8️⃣' if i == 8 else '7️⃣' if i == 7 else '6️⃣' if i == 6 else '5️⃣' if i == 5 else '4️⃣' if i == 4 else '3️⃣' if i == 3 else '2️⃣' if i == 2 else '1️⃣'}  {i}")
    time.sleep(0.5)

print("LAUNCH!")
print()

# Exercise 7: ATM Withdrawal Simulation
print("ATM WITHDRAWAL SIMULATION")

account_balance = 15000.00
print(f"Welcome! Your current balance is KES {account_balance:,.2f}\n")

withdrawal_amount = float(input("  Enter withdrawal amount (KES) : "))

if withdrawal_amount <= 0:
    print("Invalid amount. Please enter a positive value.")
elif withdrawal_amount > account_balance:
    print(f"Insufficient funds!")
    print(f"You requested KES {withdrawal_amount:,.2f} but your balance is KES {account_balance:,.2f}")
elif withdrawal_amount % 100 != 0:
    print("Please enter an amount in multiples of KES 100.")
elif withdrawal_amount > 40000:
    print("Daily withdrawal limit is KES 40,000.")
else:
    account_balance -= withdrawal_amount
    print(f"Dispensing KES {withdrawal_amount:,.2f}...")
    print(f"Remaining balance : KES {account_balance:,.2f}")
    print("Please collect your cash. Thank you!")
print()

# Exercise 8: Login System
print("LOGIN SYSTEM")

VALID_USERNAME = "vivian_data"
VALID_PASSWORD = "Solavise2026!"
max_login_attempts = 3
login_attempts = 0

print("Welcome to the Solavise Data Portal\n")

while login_attempts < max_login_attempts:
    username = input("Username : ")
    password = input("Password : ")
    login_attempts += 1

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        print(f"Login successful! Welcome back, {username}!")
        print("Redirecting to your dashboard...")
        break
    else:
        remaining = max_login_attempts - login_attempts
        if remaining > 0:
            print(f"Incorrect credentials. {remaining} attempt(s) remaining.\n")
        else:
            print("Account locked after 3 failed attempts.")
            print("Please contact support to reset your access.")
print()