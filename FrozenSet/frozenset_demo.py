# Made by Learn Build Share
# Event Pass Verification System
# Python Frozen Set Example

# Pass IDs generated before the event starts
pass_ids = frozenset({
    "PASS101",
    "PASS102",
    "PASS103",
    "PASS104"
})

print("🎟️ LearnBuildShare Connect 2026")
print("-" * 30)

# Verify a visitor
visitor_pass = input("Enter your Pass ID: ")

if visitor_pass in pass_ids:
    print("✅ Pass Verified. Welcome!")
else:
    print("❌ Invalid Pass. Entry Denied.")

print("\nTrying to generate a new pass...")

new_pass = input("Enter New Pass ID: ")

if new_pass in pass_ids:
    print("⚠️ This Pass ID is already generated.")
else:
    print("🔒 New Pass IDs cannot be generated while the event is live.")

print("\nTrying to remove a pass...")

remove_pass = input("Enter Pass ID to remove: ")

if remove_pass in pass_ids:
    print(f"🔒 {remove_pass} cannot be removed.")
    print("It has already been issued for this event.")
else:
    print("Pass ID not found.")

print("\nTrying to update a pass...")

old_pass = input("Current Pass ID: ")
updated_pass = input("New Pass ID: ")

if old_pass in pass_ids:
    print(f"🔒 {old_pass} cannot be changed to {updated_pass}.")
    print("Pass IDs are locked until the event is completed.")
else:
    print("Pass ID not found.")

print("\nWhy Frozen Set?")
print("- Unique Pass IDs")
print("- Pass IDs cannot be added")
print("- Pass IDs cannot be removed")
print("- Pass IDs cannot be modified")
print("- Perfect for Event Pass Verification")

