# Traditional For loop to filter employees with salary greater than 50
employees = {
    "Rahul": 45,
    "Priya": 60,
    "Arjun": 75,
    "Sneha": 40,
    "Kiran": 55
}

high_salary = {}

for name, salary in employees.items():
    if salary > 50:
        high_salary[name] = salary

print(high_salary)



employees = {
    "Rahul": 45,
    "Priya": 60,
    "Arjun": 75,
    "Sneha": 40,
    "Kiran": 55
}

high_salary = {
    name: salary
    for name, salary in employees.items()
    if salary > 50
}

print(high_salary)



skills = ["Python", "Java", "Python", "SQL", "Java"]

unique_skills = {skill for skill in skills}

print(unique_skills)


numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print(squares)
#squares = [1, 4, 9, 16, 25]