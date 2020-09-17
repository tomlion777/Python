from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
rotors='II IV V',
reflector='B',
ring_settings='B U L',
plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

input = input("Enter The Encrypted Text : ")

machine.set_display('WXC')
msg_key = machine.process_text('KCH')

machine.set_display(msg_key) # original message key is BLA
plaintext = machine.process_text(input)
print(plaintext)
