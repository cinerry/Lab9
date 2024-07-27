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
