# Function 1: Receive Topic
def receive_topic():
    topic = input("Enter your study topic: ")
    return topic


# Function 2: Extract Keywords
def extract_keywords(topic):
    words = topic.split()

    keywords = []

    for word in words:
        if len(word) > 4:
            keywords.append(word)

    return keywords


# Function 3: Generate Summary
def generate_summary(keywords):
    summary = "This topic mainly focuses on: "

    for word in keywords:
        summary += word + ", "

    return summary


# Function 4: Display Study Notes
def display_notes(topic, keywords, summary):
    print("\n📄 Study Notes")
    print("----------------")
    
    print("Topic:", topic)

    print("\nKeywords:")
    for keyword in keywords:
        print("- " + keyword)

    print("\nSummary:")
    print(summary)


# Main Program Flow

topic = receive_topic()                 # Output of Function 1

keywords = extract_keywords(topic)      # Input to Function 2

summary = generate_summary(keywords)    # Input to Function 3

display_notes(topic, keywords, summary)  # Input to Function 4