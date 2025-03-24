# Week 1 - Conditionals | Problem Set 1
# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
# Otherwise output No.


def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()

    if answer == "42" or answer.lower().replace("-", "").replace(" ", "") == "fortytwo":
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    main()
