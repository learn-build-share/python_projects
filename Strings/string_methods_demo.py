"""Simple executable examples for common built-in string methods. Made by Learn Build Share."""

# Learn Build Share

# A string is a sequence of characters used to store text.
print("What is a string?")
print("A string is a sequence of characters used to store text.")
print("Example: 'Python'")

# Definition 1: A string is text data inside single quotes.
print("Definition 1:", 'Hello')
# Definition 2: A string is text data inside double quotes.
print("Definition 2:", "World")
# Definition 3: A string is text data inside triple quotes.
print("Definition 3:", """Hello World""")

# Positive indexing starts from 0 on the left.
word = "Python"
print("Positive indexing:", word[0], word[2], word[5])
# Negative indexing starts from -1 on the right.
print("Negative indexing:", word[-1], word[-3], word[-6])

text = "Python Tutorial"
name = " Rohit123 "
number_text = "123"
letters = "Rohit"
message = "Hello {}"
words = "python streamlit"
parts = "a,b,c"
path = "C:/Users/name/demo.txt"
email = "rohit@example.com"
fruit = "banana"

# Returns the number of characters in a string.
print("len(text):", len(text))
# Removes spaces from both ends of a string.
print("name.strip():", name.strip())
# Removes spaces from the left side of a string.
print("name.lstrip():", name.lstrip())
# Removes spaces from the right side of a string.
print("name.rstrip():", name.rstrip())
# Converts a string to lowercase.
print("text.lower():", text.lower())
# Converts a string to uppercase.
print("text.upper():", text.upper())
# Converts the first letter of each word to uppercase.
print("words.title():", words.title())
# Capitalizes only the first character of a string.
print("'python'.capitalize():", "python".capitalize())
# Converts a string to a more aggressive lowercase form.
print("'STRASSE'.casefold():", "STRASSE".casefold())
# Swaps uppercase and lowercase letters.
print("'RoHiT'.swapcase():", "RoHiT".swapcase())
# Replaces all occurrences of one substring with another.
print("'hello'.replace('l', 'p'):", "hello".replace("l", "p"))
# Counts how many times a substring appears.
print("'banana'.count('a'):", fruit.count("a"))
# Finds the first position of a substring, or -1 if missing.
print("'python'.find('th'):", "python".find("th"))
# Finds the first position of a substring from the right.
print("'python'.rfind('t'):", "python".rfind("t"))
# Finds the first position of a substring and raises an error if missing.
print("'python'.index('th'):", "python".index("th"))
# Finds the first position of a substring from the right and raises an error if missing.
print("'python'.rindex('t'):", "python".rindex("t"))
# Checks whether a string starts with a given prefix.
print("'python'.startswith('py'):", "python".startswith("py"))
# Checks whether a string ends with a given suffix.
print("'python'.endswith('on'):", "python".endswith("on"))
# Splits a string into words using whitespace.
print("words.split():", words.split())
# Splits a string by a custom separator.
print("parts.split(','):", parts.split(","))
# Splits a string from the right using whitespace.
print("words.rsplit():", words.rsplit())
# Joins a list of strings using a separator.
print("' '.join([...]):", " ".join(["python", "streamlit"]))
# Splits a string into three parts around a separator.
print("'python-streamlit'.partition('-'):", "python-streamlit".partition("-"))
# Splits a string into three parts around the last separator.
print("'python-streamlit'.rpartition('-'):", "python-streamlit".rpartition("-"))
# Centers the string to a given width.
print("'py'.center(6):", "py".center(6))
# Left-justifies the string to a given width.
print("'py'.ljust(4):", "py".ljust(4))
# Right-justifies the string to a given width.
print("'py'.rjust(4):", "py".rjust(4))
# Expands tab characters to spaces.
print("'a\tb'.expandtabs():", "a\tb".expandtabs())
# Pads a numeric string with zeros on the left.
print("'7'.zfill(3):", "7".zfill(3))
# Checks whether the string contains only letters or numbers.
print("'Rohit123'.isalnum():", "Rohit123".isalnum())
# Checks whether the string contains only letters.
print("'Rohit'.isalpha():", letters.isalpha())
# Checks whether the string contains only ASCII characters.
print("'Rohit'.isascii():", "Rohit".isascii())
# Checks whether the string contains only decimal characters.
print("'123'.isdecimal():", "123".isdecimal())
# Checks whether the string contains only digits.
print("'123'.isdigit():", number_text.isdigit())
# Checks whether the string is a valid identifier.
print("'python'.isidentifier():", "python".isidentifier())
# Checks whether all characters are lowercase letters.
print("'python'.islower():", "python".islower())
# Checks whether the string contains only numeric characters.
print("'123'.isnumeric():", "123".isnumeric())
# Checks whether all characters are printable.
print("'hello'.isprintable():", "hello".isprintable())
# Checks whether the string contains only whitespace.
print("'   '.isspace():", "   ".isspace())
# Checks whether the string is title case.
print("'Python'.istitle():", "Python".istitle())
# Checks whether all characters are uppercase letters.
print("'PYTHON'.isupper():", "PYTHON".isupper())
# Returns a translation table for translate().
print("str.maketrans('abc','123'):", str.maketrans("abc", "123"))
# Translates characters using a translation table.
print("'abc'.translate(table):", "abc".translate(str.maketrans("abc", "123")))
# Encodes the string into bytes.
print("'python'.encode('utf-8'):", "python".encode("utf-8"))
# Formats values inside curly braces.
print("'Hello {}'.format('Rohit'):", message.format("Rohit"))
# Formats values using a mapping dictionary.
print("'{name}'.format_map({'name':'Rohit'}):", "{name}".format_map({"name": "Rohit"}))
# Returns the ASCII representation of an object.
print("ascii(text):", ascii(text))
# Returns the printable representation of an object.
print("repr(text):", repr(text))
# Converts an integer to its character.
print("chr(65):", chr(65))
# Converts a character to its integer code.
print("ord('A'):", ord("A"))
# Converts an object to a string.
print("str(123):", str(123))
# Returns a bytes object from a string.
print("bytes('py', 'utf-8'):", bytes("py", "utf-8"))
# Removes a prefix if present.
print("'hello'.removeprefix('he'):", "hello".removeprefix("he"))
# Removes a suffix if present.
print("'hello'.removesuffix('lo'):", "hello".removesuffix("lo"))
# Splits a string into lines.
print("'hello\nworld'.splitlines():", "hello\nworld".splitlines())
# Returns a substring using a start index.
print("'python'[0:3]:", "python"[0:3])
# Returns a substring using a start and stop index.
print("'python'[2:5]:", "python"[2:5])
# Returns every second character.
print("'python'[::2]:", "python"[::2])
# Reverses the order of characters.
print("'python'[::-1]:", "python"[::-1])
# Returns the first character.
print("'python'[0]:", "python"[0])
# Returns the last character.
print("'python'[-1]:", "python"[-1])
# Joins a list of words using a separator.
print("' '.join(['learn','build','share']):", " ".join(["learn", "build", "share"]))
# Repeats a string multiple times.
print("'py' * 3:", "py" * 3)
# Builds a string with repeated separators.
print("'-'.join(['a','b','c']):", "-".join(["a", "b", "c"]))
# Checks whether a substring exists inside a string.
print("'py' in 'python':", "py" in "python")
# Checks whether a substring does not exist inside a string.
print("'xy' not in 'python':", "xy" not in "python")
# Uses a repeated format pattern for a string.
print("'{} {}' .format('Learn','Build'):", "{} {}".format("Learn", "Build"))
# Uses a named format pattern for a string.
print("'{name} {topic}' .format(name='Rohit', topic='Python'):", "{name} {topic}".format(name="Rohit", topic="Python"))
# Creates a string from a number with fixed width.
print("'10'.zfill(5):", "10".zfill(5))
# Returns the first 3 characters of a string.
print("'streamlit'[:3]:", "streamlit"[:3])
# Returns characters after the first 3 positions.
print("'streamlit'[3:]:", "streamlit"[3:])
# Converts a string to a raw representation.
print("repr('line\nnext'):", repr("line\nnext"))
# Converts a string to a path-like representation.
print("path.split('/'):", path.split("/"))
# Uses the email to split around the symbol.
print("email.split('@'):", email.split("@"))
# Uses the string to split by a comma.
print("'a,b,c'.split(','):", "a,b,c".split(","))
# Checks whether all characters are printable.
print("'\n'.isprintable():", "\n".isprintable())
# Checks whether a string is a valid identifier after stripping.
print("'  name  '.strip().isidentifier():", "  name  ".strip().isidentifier())
# Returns a string with the first letter only capitalized.
print("'python tutorial'.capitalize():", "python tutorial".capitalize())
# Returns a string with each word capitalized.
print("'python tutorial'.title():", "python tutorial".title())
# Returns a string with each word lowercased.
print("'PYTHON TUTORIAL'.lower():", "PYTHON TUTORIAL".lower())
# Returns a string with each word uppercased.
print("'python tutorial'.upper():", "python tutorial".upper())
# Returns a string that is stripped of spaces.
print("'  learn build share  '.strip():", "  learn build share  ".strip())
