# DASM-symbol-to-FCEUX-nl

A simple, fragile script to parse the symbol output from the DASM assembler's `-s` argument and convert it to a FCEUX NES emulator compatible format for debugging and development purposes. This enables the user to see meaningful labels in the FCEUX debugger instead of raw addresses, where appropriate.

This is a first pass attempt, quickly made for use in a game jam.

# Example usage

Generate your assembler output, being sure to generate a symbol dump with `-s`

`dasm myfile.asm -f3 -omyrom.nes -smyrom.nes.sym`

Pass the symbol dump to DASM-symbol-to-FCEUX-nl

`dasm-symbol-to-fceux.py myrom.nes.sym myrom.nes.nl`

Launch FCEUX, ensuring the .nl file is in the same directory as the nes rom

`fceux myrom.nes`



