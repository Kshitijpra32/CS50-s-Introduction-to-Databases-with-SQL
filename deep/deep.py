answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?:")
answer = answer.strip().lower()

if answer == "42" or answer == "forty two" or answer == "forty-two":
    print("yes")

else:
    print("No")
