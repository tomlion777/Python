from enigma.machine import EnigmaMachine

def Encrypt():
    machine = EnigmaMachine.from_key_sheet(
        rotors='II IV V',
        reflector='B',
        ring_settings='B U L',
        plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

    print("Please Enter Text To Be Encrypted (ALL IN CAPSLOCK AND PUT X INSTEAD OF SPACES) : ")
    Decrypted_form_1 = input()

    machine.set_display('WXC')  # set initial rotor positions

    enc_key = machine.process_text('BLA')  # encrypt message key

    machine.set_display(enc_key)  # use message key BLA

    ciphertext = machine.process_text(Decrypted_form_1)
    print(ciphertext)

    return exit()


def Decrypt():
    machine = EnigmaMachine.from_key_sheet(
        rotors='II IV V',
        reflector='B',
        ring_settings='B U L',
        plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')


    encrypted_text = input("Enter The Encrypted Text : ")

    machine.set_display('WXC')

    msg_key = machine.process_text('KCH')

    print(msg_key)

    machine.set_display(msg_key)  # original message key is BLA
    plaintext = machine.process_text(encrypted_text)
    print(plaintext)
    print(msg_key)

User_Action1 = input("Enter Action (encrypt or decrypt) : ")


if User_Action1 == "Encrypt" or "encrypt":

    Encrypt()

    User_Action2 = input("Would you like to encrypt or decrypt now(Yes or No) : ")

    if User_Action2 == "Yes" or "yes":
        User_Action3 = input("Enter Action (encrypt or decrypt) : ")

        if User_Action3 == "Encrypt" or "encrypt":
            Encrypt()

        if User_Action3 == "Decrypt" or "decrypt":
            Decrypt()

    if User_Action2 == "No" or "no":
        exit(code=0)

if User_Action1 == "Decrypt" or "decrypt":

    Decrypt()

    User_Action4 = input("Would you like to encrypt or decrypt now(Yes or No) : ")

    if User_Action4 == "Yes" or "Yes":
        User_Action5 = input("Enter Action (encrypt or decrypt) : ")

        if User_Action5 == "Encrypt" or "encrypt":
            Encrypt()

        if User_Action5 == "Decrypt" or "decrypt":
            Decrypt()

    if User_Action4 == "No" or "no":
        exit(code=0)