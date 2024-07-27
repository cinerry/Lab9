def encode(password):
    encode_password = ""
    for char in password:
        changed_char = (int(char) + 3) % 10
        encode_password += str(changed_char)
    return encode_password

