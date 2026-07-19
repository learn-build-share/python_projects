# Made by Learn Build Share
# set is  a collection of unique elements in Python. 
# we will define set using curly braces {} or the set() constructor.
# followers = {"rahul", "sai", "priya"}

# Instagram Followers using Set
followers = {"rahul", "sai", "priya"}
print("Original:", followers)

# Add username
followers.add("john")
# {"rahul", "sai", "priya", "john"}


# Remove username
followers.remove("sai")
print("After Remove:", followers)
#{"rahul", "priya", "john"}

# Update multiple usernames
followers.update(["kiran", "vamsi"])
print("After Update:", followers)
# Duplicate removal
user_list = ["rahul", "priya", "rahul", "john", "priya"]

unique_users = set(user_list)

print("Original List:", user_list)
print("Unique Followers:", unique_users)