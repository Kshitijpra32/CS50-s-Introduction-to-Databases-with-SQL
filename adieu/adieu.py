import inflect

p = inflect.engine()

def main():
    names = []

    # Keep asking for names until EOF
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()  # CS50 expects a blank line before output
            break

    # Join names in natural English
    final = p.join(names)

    print(f"Adieu, adieu, to {final}")

if __name__ == "__main__":
    main()
