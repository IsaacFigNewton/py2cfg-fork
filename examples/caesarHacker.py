# Caesar Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)

message = "NyyJu8zn1Jorv1t6Jun9rJ7u5rrJyv9r6:J38oyvp,J35v9n7r,Jn1qJ6rp5r7MJTno5vryJTn5pnnJZn548r?"
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

# Loop through every possible key:
for key in range(1, len(SYMBOLS)):
    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ""

    # The rest of the program is almost the same as the original program:

    # Loop through each symbol in `message`:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wrap-around:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Display every possible decryption:
    print("Key #%s: %s" % (key, translated))
