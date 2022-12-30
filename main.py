import logo


def caesar(direct, a, b):
    final_text = ""
    for i in a:
        if i in alphabet:
            index_a = alphabet.index(i)
            if direct == "encode":
                index_total = index_a + b
                final_text += alphabet[index_total % 26]
            elif direct == "decode":
                index_total = index_a - b
                final_text += alphabet[index_total % 26]
        else:
            final_text += i
    print(f"The {direct} text is:  {final_text}")


def restart():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direct=direction, a=text, b=shift)
    pro_loop = input("Do you want try program again? ")
    if pro_loop == "yes":
        restart()
    elif pro_loop == "no":
        print("Ok, have fun. Goodbye")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo.logo)
restart()
