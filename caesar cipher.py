print("Welcome to the Caesar Cipher Encoder/Decoder!")
while True:
    # allows the program to return to this point if an invalid input is given. "break" ends the "while true" when proper
    # input is given.
    operation = input("Would you like to encode or decode?")
    operation = operation.lower()
    if operation == "encode":
        op = 1
        break
    elif operation == "decode":
        op = -1
        # op defines encoding or decoding and flips the value of the shift when decoding
        break
    else:
        print("Invalid answer, please enter \"encode\" or \"decode\"")

while True:
    key = input("What value would you like to shift the input? (A whole number between 1 and 25)")
    key = int(key)
    if key <= 0 or key >= 26:
        print("Invalid answer, please enter a whole number between 1 and 25")
    else:
        print("Your shift is " + str(key))
        break

while True:
    if op == 1:
        phrase = "encoded."
    else:
        phrase = "decoded."
    orig = input("Please input your desired text to be " + phrase + "(numbers must be typed. Ex: 1 is \"one\")")
    orig = orig.replace(" ", "")
    str(orig)
    if orig.isalpha():
        break
    else:
        print("Invalid Input")
orig = orig.lower()

orig_numeric = []
for character in orig:
    number = ord(character) - 96
    orig_numeric.append(number)
output_numeric = []

for number in orig_numeric:
    new_number = number + op * key
    if new_number >= 27:
        new_number = new_number - 26
    elif new_number <= 0:
        new_number = new_number + 26
    output_numeric.append(new_number)

output_char = []
for number in output_numeric:
    character2 = chr(number + 96)
    output_char.append(character2)

output_final = ""
output_final = output_final.join(output_char)
output_final = str(output_final)
if op == 1:
    output_final.upper()

print("Your new text is:")
print(output_final)
