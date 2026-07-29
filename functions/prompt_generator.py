# Made By Learn Build Generator
# AI Prompt Generator
# Python Functions Mini Project


# User-defined Function
def generate_prompt(topic):
    prompt = f"""
You are an expert in {topic}.

Explain the topic in simple language.

Include:
- Definition
- Examples
- Interview Questions
- Summary
"""

    return prompt.strip()


# User-defined Function
def word_count(text):
    return len(text.split())


# Main Program
print("===== AI Prompt Generator =====")

topic = input("Enter a Topic: ")

prompt = generate_prompt(topic)

print("\nGenerated Prompt")
print("-" * 30)
print(prompt)

print("\nPrompt Statistics")
print("-" * 30)
print("Word Count :", word_count(prompt))
print("Character Count :", len(prompt))

print("\nThank You!")