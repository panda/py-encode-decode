# Steven Kotwal (panda) UF

def encode(password):
    encoded = ""
    for digit in str(password):
        shifted_digit = (int(digit) + 3) % 10
        encoded += str(shifted_digit)
    return encoded


def decode(password):
    pass


def main():
    password = ""
    while True:
        print(f"Menu")
        print(f"-------------")
        print(f"1. Encode")
        print(f"2. Decode")
        print(f"3. Quit")

        choice = int(input("Please enter an option: "))

        if choice == 1:
            password = input("Please enter an 8 digit password to encode: ")
            password = encode(password)
            print(f"Your password has been encoded and stored!")
        elif choice == 2:
            if password == "":
                print("You need to encode a password first!")
            else:
                print(f"The encoded password is: {password}, and the original password is: {decode(password)}")
        elif choice == 3:
            break
        else:
            print("Invalid option. Please pick a valid option.")


if __name__ == "__main__":
    main()
