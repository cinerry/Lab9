def encode(password):
    encode_password = ""
    password = str(password)
    for char in password:
        changed_char = (int(char) + 3) % 10
        encode_password += str(changed_char)
    return encode_password
def decode(password):
    empty_string = ""
    password = str(password)
    for char in password:
        changed_char = (int(char) - 3) % 10
        empty_string += str(changed_char)
    return empty_string

def main ():
    encode_password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("3. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter the password to encode: ")
            encode_password = encode(password)
            print("Your password has been encoded and stored!\n")

        elif option == "2":
            if encode_password:
                decode_password = decode(encode_password)
                print(f"The encoded password is {encode_password}, and the original password is {decode_password}.\n")
            else:
                print("Enter encoded password first.")

        elif option == "3":
            break
if __name__ == "__main__":
    main()
