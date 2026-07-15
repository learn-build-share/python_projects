choice = input("Choose an operation: ")

match choice:
    case "add":
        print("Addition Selected")

    case "sub":
        print("Subtraction Selected")

    case "mul":
        print("Multiplication Selected")

    case "div":
        print("Division Selected")

    case _:
        print("Invalid Choice")