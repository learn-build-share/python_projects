watchlist = []

menu = """
Netflix Watchlist - List Operations
1. Add movie
2. Remove movie
3. Insert movie at position
4. Show watchlist
5. Show list and length
6. Traverse watchlist
0. Quit
"""

while True:
    print(menu)
    choice = input("Choose an option: ").strip()

    if choice == "0":
        print("Goodbye!")
        break

    if choice == "1":
        movie = input("Movie name: ").strip()
        if movie:
            watchlist.append(movie)
            print(f'Added: {movie}')
        else:
            print("No movie entered.")

    elif choice == "2":
        movie = input("Movie name: ").strip()
        if movie in watchlist:
            watchlist.remove(movie)
            print(f'Removed: {movie}')
        else:
            print("Movie not found.")

    elif choice == "3":
        movie = input("Movie name: ").strip()
        if not movie:
            print("No movie entered.")
            continue
        pos = input(f"Position 0-{len(watchlist)}: ").strip()
        if pos.isdigit():
            pos = int(pos)
            if 0 <= pos <= len(watchlist):
                watchlist.insert(pos, movie)
                print(f'Inserted: {movie} at {pos}')
            else:
                print("Invalid position.")
        else:
            print("Position must be a number.")

    elif choice == "4":
        print("Watchlist:")
        for i, movie in enumerate(watchlist, 1):
            print(f"{i}. {movie}")

    elif choice == "5":
        print("Current list:", watchlist)
        print("Length:", len(watchlist))

    elif choice == "6":
        print("Traversal:")
        for movie in watchlist:
            print(movie)

    else:
        print("Invalid option.")

    print()
