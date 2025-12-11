import art

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

print(art.logo)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")

while True:
    # Ask once, then validate without re-printing the prompt
    print("Type 'encode' to encrypt, type 'decode' to decrypt:")
    direction = input().lower()
    while direction not in ["encode", "decode"]:
        print("Invalid choice. Please type 'encode' or 'decode'.")
        direction = input().lower()

    text = input("Type your message:\n").lower()

    # Validate shift as integer
    print("Type the shift number:")
    while True:
        shift_input = input().strip()
        try:
            shift = int(shift_input)
            shift = shift % len(alphabet)
            break  # valid input, exit loop
        except ValueError:
            print("Invalid shift. Please enter a whole number (e.g., 3).")

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    print("Would you like to go again? (type 'yes' or 'no')")
    restart = input().lower()
    while restart not in ["yes", "no"]:
        print("Invalid choice. Please type 'yes' or 'no'.")
        restart = input().lower()

    if restart == "no":
        print("Goodbye")
        break
