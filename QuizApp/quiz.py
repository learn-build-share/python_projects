questions = [
    "What is Python?",
    "What is a Variable?",
    "What is a Loop?",
    "What is a List?",
    "What is a Function?",
    "What is an If Statement?",
    "What is a For Loop?",
    "What is a While Loop?",
    "What is a Comment in Python?",
    "What is a Dictionary?"
]
for question in questions:
    answer = input(f"{question} (type 'skip' or 'exit'): ")
    if answer.lower() == "exit":
        print("Quiz Ended. Thank you! 👋")
        break

    if answer.lower() == "skip":
        print("Question Skipped!\n")
        continue

    print("Answer Submitted ✅\n")

print("Quiz Completed!")





