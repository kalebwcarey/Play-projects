import string


def strip(to_be):
    to_be = to_be.replace(" ", "").replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace(";", "")
    to_be = to_be.replace(":", "").replace("\"", "").replace("\'", "").replace("/", "").replace("-", "")
    return to_be


while True:
    orig = input("Please input your text to be encrypted or decrypted (No special Characters; numbers must be typed "
                 "Ex: 1 would be \"one\"):")
    orig = strip(orig)
    if orig.isalpha():
        orig = orig.lower().replace("j", "i")
        break
    else:
        print("Error: text contains special characters and/or numbers. Please remove and reenter")

while True:
    operation = strip(input("Would you like to encrypt or decrypt? Please enter decrypt/encrypt or e/d")).lower()
    if operation == "encrypt" or "e":
        op = 0
        break
    elif operation == "decrypt" or "d":
        op = 1
        break
    else:
        print("Invalid input.")

text = []
for character in orig:
    text.append(character)
n = 0
while n < len(text) - 1:
    if text[n] == text[n + 1]:
        text.insert(n + 1, "x")
    n += 2
if len(text) % 2:
    text.append("x")
while True:
    keyphrase = input("Please input your keyphrase (No special Characters; numbers must be typed Ex: 1 would be "
                      "\"one\"):")
    keyphrase = strip(keyphrase)
    if keyphrase.isalpha():
        keyphrase = keyphrase.lower().replace("j", "i")
        break
    else:
        print("Error: keyphrase contains special characters and/or numbers. Please remove and reenter")
key = []
for character in keyphrase:
    if not character in key:
        key.append(character)
alphabet = list(string.ascii_lowercase)
alphabet.remove("j")
for character in alphabet:
    if not character in key:
        key.append(character)


def playfair_encrypt(char1, char2, table):
    output = []
    position1 = table.index(char1)
    position2 = table.index(char2)
    if int(position1 / 5) == int(position2 / 5):
        if not (position1 + 1) % 5:
            output.append(table[position1 - 4])
        else:
            output.append(table[position1 + 1])
        if not (position2 + 1) % 5:
            output.append(table[position2 - 4])
        else:
            output.append(table[position2 + 1])
    elif position1 % 5 == position2 % 5:
        if position1 / 5 >= 4:
            output.append(table[position1 - 20])
        else:
            output.append(table[position1 + 5])
        if position2 / 5 >= 4:
            output.append(table[position2 - 20])
        else:
            output.append(table[position2 + 5])
    else:
        x1 = position1 % 5
        y1 = int(position1 / 5)
        x2 = position2 % 5
        y2 = int(position2 / 5)
        output.append(table[y1 * 5 + x2])
        output.append(table[y2 * 5 + x1])
    return output


def playfair_decrypt(char1, char2, table):
    output = []
    position1 = table.index(char1)
    position2 = table.index(char2)
    if int(position1 / 5) == int(position2 / 5):
        if (position1 + 1) % 5 == 1:
            output.append(table[position1 + 4])
        else:
            output.append(table[position1 - 1])
        if (position2 + 1) % 5 == 1:
            output.append(table[position2 + 4])
        else:
            output.append(table[position2 - 1])
    elif position1 % 5 == position2 % 5:
        if position1 / 5 < 1:
            output.append(table[position1 + 20])
        else:
            output.append(table[position1 - 5])
        if position2 / 5 < 1:
            output.append(table[position2 + 20])
        else:
            output.append(table[position2 - 5])
    else:
        x1 = position1 % 5
        y1 = int(position1 / 5)
        x2 = position2 % 5
        y2 = int(position2 / 5)
        output.append(table[y1 * 5 + x2])
        output.append(table[y2 * 5 + x1])

    return output


n = 0
encrypted_list = []
while n != len(text):
    if op == 0:
        encrypted_list.append(playfair_encrypt(text[n], text[n + 1], key))
    else:
        encrypted_list.append(playfair_decrypt(text[n], text[n + 1], key))
    n += 2
conversion_list = []
for object in encrypted_list:
    conversion_list.append("".join(object))
final = "".join(conversion_list)
if op == 0:
    print("Your ciphertext is:")
    final.upper()
else:
    print("(Your plaintext may contain unnecessary Xs or may have Is that are actually Js due to the limitations of "
          "the Playfair cipher)")
    print("Your plaintext is:")
print(final)
input("Press Enter to exit")