# Made by Learn Build Share

# 1. Square Pattern

n = 5

for i in range(n):
    print("* " * n)


# 2. Hollow Square

n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 3. Left Triangle


n = 5

for i in range(1, n+1):
    print("* " * i)


# 4. Inverted Left Triangle


n = 5

for i in range(n,0,-1):
    print("* " * i)


# 5. Right Triangle


n=5

for i in range(1,n+1):
    print("  "*(n-i)+"* "*i)


# 6. Inverted Right Triangle

n=5

for i in range(n,0,-1):
    print("  "*(n-i)+"* "*i)


# 7. Pyramid

n=7

half=n//2
space=half
star=1

for i in range(half+1):
    print("_"*space+"*"*star+"_"*space)
    space-=1
    star+=2


# 8. Inverted Pyramid


n=7

half=n//2
space=0
star=n

for i in range(half+1):
    print("_"*space+"*"*star+"_"*space)
    space+=1
    star-=2


# 9. Diamond

n=5

for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))

for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))


# 10. Hollow Pyramid


n=5

for i in range(n):
    print(" "*(n-i),end="")
    for j in range(2*i+1):
        if j==0 or j==2*i or i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()


# 11. Hollow Diamond

n = 5   # Number of rows in the top half

# Top Half
outside = n - 1
inside = 0

for i in range(n):
    print(" " * outside, end="")
    print("*", end="")

    if i != 0:
        print(" " * inside, end="")
        print("*", end="")

    print()

    outside -= 1
    inside += 2

# Bottom Half
outside = 1
inside = 2 * (n - 2) - 1

for i in range(n - 1):
    print(" " * outside, end="")
    print("*", end="")

    if i != n - 2:
        print(" " * inside, end="")
        print("*", end="")

    print()

    outside += 1
    inside -= 2

# 12. X Pattern


n=5

for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()


# 13. Plus Pattern

n = 7
middle = n // 2

for i in range(n):
    for j in range(n):
        if i == middle or j == middle:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 14. Butterfly Pattern

n = 5

# Top Half
stars = 1
spaces = 2 * (n - 1)

for i in range(n):
    print("*" * stars + " " * spaces + "*" * stars)
    stars += 1
    spaces -= 2

# Bottom Half
stars = n - 1
spaces = 2

for i in range(n - 1):
    print("*" * stars + " " * spaces + "*" * stars)
    stars -= 1
    spaces += 2

# 15. Hourglass

n = 5

# Top Half
spaces = 0
stars = 2 * n - 1

for i in range(n):
    print(" " * spaces + "*" * stars)
    spaces += 1
    stars -= 2

# Bottom Half
spaces = n - 2
stars = 3

for i in range(n - 1):
    print(" " * spaces + "*" * stars)
    spaces -= 1
    stars += 2

# 16. Sandglass
n = 5

# Top
spaces = 0
stars = 2 * n - 1

for i in range(n):
    print(" " * spaces + "*" * stars)
    spaces += 1
    stars -= 2

# Bottom
spaces = n - 2
stars = 3

for i in range(n - 1):
    print(" " * spaces + "*" * stars)
    spaces -= 1
    stars += 2


# 17. Zig Zag Pattern
n = 17

for i in range(3):
    for j in range(n):

        if (i == 0 and j % 4 == 0) or \
           (i == 1 and j % 2 == 1) or \
           (i == 2 and j % 4 == 2):
            print("*", end="")
        else:
            print(" ", end="")

    print()


# 18. Checkerboard

n=5

for i in range(n):
    for j in range(n):
        print("*" if (i+j)%2==0 else "_",end=" ")
    print()


# 19. Border Rectangle
rows = 5
cols = 8

for i in range(rows):
    for j in range(cols):

        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# 20. Cross Pattern
n = 7

for i in range(n):
    for j in range(n):

        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# 21. Floyd's Triangle

n=5
num=1

for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()


# 22. Pascal Triangle
n = 5

for i in range(n):

    num = 1

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()

# 23. Binary Triangle
n = 5

for i in range(n):

    for j in range(i + 1):

        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")

    print()

# 24. Continuous Number Triangle

n = 5
num = 1

for i in range(n):

    for j in range(i + 1):

        print(num, end=" ")
        num += 1

    print()
# 25. Row Number Triangle

n = 5

for i in range(1, n + 1):

    for j in range(i):
        print(i, end=" ")

    print()

# 26. Column Number Triangle
n = 5

for i in range(n):

    for j in range(i + 1):
        print(j + 1, end=" ")

    print()
# 27. Reverse Number Triangle
n = 5

for i in range(1, n + 1):

    for j in range(i, 0, -1):
        print(j, end=" ")

    print()

# 28. Character Triangle

for i in range(5):
    print(chr(65+i)*(i+1))




# 29. Alphabet Pyramid
n = 5

for i in range(n):

    for j in range(i + 1):
        print(chr(65 + j), end=" ")

    print()


# 30. Reverse Alphabet Triangle
n = 5

for i in range(n):

    for j in range(i, -1, -1):
        print(chr(65 + j), end=" ")

    print()

# 31. Hollow Triangle
n = 5

for i in range(n):

    for j in range(i + 1):

        if j == 0 or i == n - 1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# 32. Hollow Right Triangle
n = 5

for i in range(n):

    print(" " * (n - i - 1), end="")

    for j in range(i + 1):

        if j == 0 or j == i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# 33. Hollow Inverted Triangle
n = 5

for i in range(n):

    for j in range(n - i):

        if i == 0 or j == 0 or j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# 34. Hollow Rectangle
rows = 5
cols = 8

for i in range(rows):

    for j in range(cols):

        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# 35. Hollow Diamond

n = 5

# Top
outside = n - 1
inside = 0

for i in range(n):

    print(" " * outside, end="")
    print("*", end="")

    if i != 0:
        print(" " * inside, end="")
        print("*", end="")

    print()

    outside -= 1
    inside += 2

# Bottom
outside = 1
inside = 2 * (n - 2) - 1

for i in range(n - 1):

    print(" " * outside, end="")
    print("*", end="")

    if i != n - 2:
        print(" " * inside, end="")
        print("*", end="")

    print()

    outside += 1
    inside -= 2

# 36. Hollow Butterfly
n = 5

# Top
for i in range(1, n + 1):

    # Left Wing
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")

    print(" " * (2 * (n - i)), end="")

    # Right Wing
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")

    print()

# Bottom
for i in range(n - 1, 0, -1):

    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")

    print(" " * (2 * (n - i)), end="")

    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")

    print()

# 37. Snake Pattern
rows = 5
cols = 4

num = 1

for i in range(rows):

    if i % 2 == 0:

        for j in range(cols):
            print(num + j, end=" ")

    else:

        for j in range(cols - 1, -1, -1):
            print(num + j, end=" ")

    num += cols
    print()

# 38. Spiral Matrix
n = 4

matrix = [[0] * n for _ in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1

num = 1

while top <= bottom and left <= right:

    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1

    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    print(row)

# 39. Wave Matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rows = len(matrix)
cols = len(matrix[0])

for j in range(cols):

    if j % 2 == 0:

        for i in range(rows):
            print(matrix[i][j], end=" ")

    else:

        for i in range(rows - 1, -1, -1):
            print(matrix[i][j], end=" ")

# 40. Spiral Stars
n = 7

grid = [[" " for _ in range(n)] for _ in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1

while top <= bottom and left <= right:

    for i in range(left, right + 1):
        grid[top][i] = "*"
    top += 1

    for i in range(top, bottom + 1):
        grid[i][right] = "*"
    right -= 1

    for i in range(right, left - 1, -1):
        grid[bottom][i] = "*"
    bottom -= 1

    for i in range(bottom, top - 1, -1):
        grid[i][left] = "*"
    left += 1

for row in grid:
    print(" ".join(row))

# 41. Heart Pattern
# Top
for i in range(6):

    for j in range(7):
        if ((i == 0 and j % 3 != 0) or
            (i == 1 and j % 3 == 0) or
            (i - j == 2) or
            (i + j == 8)):
            print("*", end="")
        else:
            print(" ", end="")

    print()

# Bottom
space = 1
stars = 9

for i in range(5):
    print(" " * space + "*" * stars)
    space += 1
    stars -= 2


# 42. Christmas Tree
n = 4

for level in range(3):

    for i in range(n):

        print(" " * (n - i + 2), end="")
        print("*" * (2 * i + 1))

for i in range(3):
    print(" " * (n + 1) + "***")

# 43. Arrow Pattern
n = 5

for i in range(1, n + 1):
    print("*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i)

# 44. Kite Pattern
n = 5

# Top
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Bottom
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# 45. Rhombus
n = 5

for i in range(n):

    print(" " * (n - i - 1), end="")
    print("* " * n)


# 46. Hollow Rhombus

n = 5

for i in range(n):

    print(" " * (n - i - 1), end="")

    for j in range(n):

        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
# 47. Number Diamond

n = 5

# Top
for i in range(1, n + 1):

    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()

# Bottom
for i in range(n - 1, 0, -1):

    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()
# 48. Alphabet Diamond
n = 5

# Top
for i in range(n):

    print(" " * (n - i - 1), end="")

    for j in range(i + 1):
        print(chr(65 + j), end="")

    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")

    print()

# Bottom
for i in range(n - 2, -1, -1):

    print(" " * (n - i - 1), end="")

    for j in range(i + 1):
        print(chr(65 + j), end="")

    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")

    print()


# 49. Concentric Square
n = 4
size = 2 * n - 1

for i in range(size):

    for j in range(size):

        value = n - min(i, j, size - 1 - i, size - 1 - j)

        print(value, end=" ")

    print()


# 50. Concentric Rectangle

rows = 5
cols = 9

for i in range(rows):

    for j in range(cols):

        value = min(i, j, rows - 1 - i, cols - 1 - j)

        print(value, end=" ")

    print()

# 51. Spiral Numbers

n = 5

matrix = [[0] * n for _ in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1

num = 1

while top <= bottom and left <= right:

    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1

    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    print(*row)

# 52. Palindrome Pyramid

n=5

for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()

# 53. Mirror Number Triangle


# 54. Mirror Alphabet Triangle



# 55. Hollow Number Pyramid

