# Mini project for simple username validation.
print("=" * 40)
print("Username Validator")
print("=" * 40)

username = input("Enter Username: ")
print("\nOriginal Username :", username)

clean_username = username.strip()
lower_username = clean_username.lower()
upper_username = clean_username.upper()

print("\nAfter Removing Spaces :", clean_username)
print("Lowercase Version     :", lower_username)
print("Uppercase Version     :", upper_username)
print("Username Length       :", len(clean_username))

if len(clean_username) < 5:
    print("❌ Username should contain at least 5 characters.")
else:
    print("✅ Username Accepted.")

print("\nString Immutability Demo")
text = "Python"
print("Original :", text)
new_text = text.upper()
print("After upper() :", new_text)
print("Original Still :", text)

print("\nExample Cases")
print("1.", " Rohit123 ".strip())
print("2.", "Rohit123")
print("3.", "ROHIT123")
print("4.", "RoHiT123")

print("\n© Learn Build Share")