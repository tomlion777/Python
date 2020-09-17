from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
rotors='II IV V',
reflector='B',
ring_settings='B U L',
plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

print("Please Enter Text To Be Encrypted (ALL IN CAPSLOCK AND PUT X INSTEAD OF SPACES) : ")
input1 = input()

machine.set_display('WXC') # set initial rotor positions

enc_key = machine.process_text('BLA') # encrypt message key

machine.set_display('BLA') # use message key BLA

ciphertext = machine.process_text(input1)
print(ciphertext)
