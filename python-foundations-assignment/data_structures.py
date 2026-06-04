# Exercise 1: Favourite Tools List
print("=" * 55)
print("           FAVOURITE TOOLS LIST 🛠️")
print("=" * 55)

tools = ["Python", "Pandas", "GitHub", "VS Code", "Tableau"]
print(f"  Initial list     : {tools}")

tools.append("Power BI")
print(f"  After append     : {tools}")

tools.insert(2, "NumPy")
print(f"  After insert     : {tools}")

tools.remove("VS Code")
print(f"  After remove     : {tools}")

popped = tools.pop()
print(f"  Popped item      : {popped}")
print(f"  Final list       : {tools}")
print(f"  Total tools      : {len(tools)}")
print()

# Exercise 2: Student Scores
print("STUDENT SCORES")

scores = [78, 92, 65, 88, 73, 95, 61, 84, 70, 90]
print(f"  Scores   : {scores}")
print(f"  Highest  : {max(scores)}")
print(f"  Lowest   : {min(scores)}")
print(f"  Average  : {sum(scores) / len(scores):.2f}")
print(f"  Total    : {sum(scores)}")

sorted_scores = sorted(scores, reverse=True)
print(f"  Ranked   : {sorted_scores}")
print(f"  Top 3    : {sorted_scores[:3]}")
print()

# Exercise 3: Shopping List Manager
print("=" * 55)
print("          SHOPPING LIST MANAGER 🛒")
print("=" * 55)

shopping_list = ["Milk", "Bread", "Eggs", "Avocado", "Tomatoes"]
print(f"  Current list     : {shopping_list}")

shopping_list.append("Onions")
shopping_list.append("Sukuma Wiki")
print(f"  After adding     : {shopping_list}")

shopping_list.remove("Bread")
print(f"  After removing   : {shopping_list}")

print(f"\n  Is 'Eggs' in list? {'Yes ✅' if 'Eggs' in shopping_list else 'No ❌'}")
print(f"  Is 'Bread' in list? {'Yes ✅' if 'Bread' in shopping_list else 'No ❌'}")
print(f"\n  Final shopping list ({len(shopping_list)} items):")

for i, item in enumerate(shopping_list, 1):
    print(f"    {i}. {item}")
print()

# Exercise 4: Country Capitals (Tuples)
print("=" * 55)
print("           COUNTRY CAPITALS 🌍")
print("=" * 55)

country_capitals = (
    ("Kenya",        "Nairobi"),
    ("Uganda",       "Kampala"),
    ("Tanzania",     "Dodoma"),
    ("Rwanda",       "Kigali"),
    ("Ethiopia",     "Addis Ababa"),
    ("Nigeria",      "Abuja"),
    ("South Africa", "Pretoria"),
    ("Ghana",        "Accra"),
)

print(f"  {'Country':<15} {'Capital'}")
print(f"  {'-'*14} {'-'*14}")
for country, capital in country_capitals:
    print(f"  {country:<15} {capital}")

print(f"\n  Total countries stored : {len(country_capitals)}")
print(f"  Tuples are immutable — perfect for fixed reference data like capitals!")
print()

# Exercise 5: Unique Visitors (Sets)
print("=" * 55)
print("            UNIQUE VISITORS 👥")
print("=" * 55)

raw_visitors = [
    "alice", "bob", "vivian", "carol", "bob",
    "alice", "david", "vivian", "eve", "carol", "frank"
]
print(f"  Raw log ({len(raw_visitors)} entries) : {raw_visitors}")

unique_visitors = set(raw_visitors)
print(f"  Unique visitors ({len(unique_visitors)}) : {unique_visitors}")
print(f"  Duplicates removed  : {len(raw_visitors) - len(unique_visitors)}")
print()

# Exercise 6: Common Skills (Sets)
print("=" * 55)
print("             COMMON SKILLS 🤝")
print("=" * 55)

vivian_skills  = {"Python", "R", "SQL", "Cybersecurity", "GitHub", "Data Visualisation", "Machine Learning"}
cohort_skills  = {"Python", "SQL", "Tableau", "Excel", "Data Visualisation", "GitHub", "Statistics"}

print(f"  Vivian's skills : {vivian_skills}")
print(f"  Cohort skills   : {cohort_skills}")

common     = vivian_skills & cohort_skills
only_vivian = vivian_skills - cohort_skills
only_cohort = cohort_skills - vivian_skills
all_skills  = vivian_skills | cohort_skills

print(f"\n  Common skills        : {common}")
print(f"  Only Vivian has      : {only_vivian}")
print(f"  Only cohort has      : {only_cohort}")
print(f"  All skills combined  : {all_skills}")
print()

# Exercise 7: Student Record (Dictionary)
print("=" * 55)
print("            STUDENT RECORD 📋")
print("=" * 55)

student = {
    "name"          : "Vivian Ndung'u",
    "student_id"    : "1049495",
    "university"    : "Catholic University of Eastern Africa",
    "course"        : "BSc Computer Science",
    "year"          : 4,
    "gpa"           : 3.7,
    "honours"       : "Second Class Upper",
    "skills"        : ["Python", "R", "SQL", "Cybersecurity"],
    "certifications": ["IBM Cybersecurity", "ISC2 CC"],
    "is_graduating" : True,
}

print("  STUDENT PROFILE")
print(f"  {'-' * 45}")
for key, value in student.items():
    label = key.replace("_", " ").title()
    if isinstance(value, list):
        print(f"  {label:<18}: {', '.join(value)}")
    else:
        print(f"  {label:<18}: {value}")

# Update and add fields
student["gpa"] = 3.8
student["internship"] = "Palladium Kenya – Data Analyst Intern"
print(f"\n  Updated GPA         : {student['gpa']}")
print(f"  Internship added    : {student['internship']}")
print()

# Exercise 8: Mini Contact Book
print("=" * 55)
print("           MINI CONTACT BOOK 📱")
print("=" * 55)

contacts = {
    "Vivian Ndung'u" : {"phone": "+254 700 000001", "email": "ndunguvihvy@gmail.com",       "city": "Nairobi"},
    "Aisha Mohamed"  : {"phone": "+254 711 000002", "email": "aisha.m@email.com",            "city": "Mombasa"},
    "Grace Wanjiru"  : {"phone": "+254 722 000003", "email": "grace.w@email.com",            "city": "Nakuru"},
    "Fatima Osei"    : {"phone": "+233 500 000004", "email": "fatima.osei@email.com",        "city": "Accra"},
    "Ngozi Adeyemi"  : {"phone": "+234 800 000005", "email": "ngozi.a@email.com",            "city": "Lagos"},
}

print(f"  📒 Contact Book ({len(contacts)} contacts)\n")
print(f"  {'Name':<18} {'Phone':<18} {'City'}")
print(f"  {'-'*17} {'-'*17} {'-'*10}")
for name, info in contacts.items():
    print(f"  {name:<18} {info['phone']:<18} {info['city']}")

# Search feature
print()
search_name = input("  🔍 Search contact by name : ")
search_lower = search_name.lower()

found = {name: info for name, info in contacts.items() if search_lower in name.lower()}

if found:
    print(f"\n  ✅ Found {len(found)} result(s):\n")
    for name, info in found.items():
        print(f"  Name  : {name}")
        print(f"  Phone : {info['phone']}")
        print(f"  Email : {info['email']}")
        print(f"  City  : {info['city']}")
        print()
else:
    print(f"\n  ❌ No contact found matching '{search_name}'")

# Add a new contact
print()
contacts["Solavise Support"] = {
    "phone": "+000 000 000000",
    "email": "support@solavise.com",
    "city" : "Online"
}
print(f"  ➕ New contact added. Total contacts : {len(contacts)}")
print()