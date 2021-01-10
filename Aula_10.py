programa

# Cesar Chiper

MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d' . split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your massage:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter your key number (1-%s)' % (MAX_KEY_SIZE) )
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord ('Z'):
                    num -= 26
                elif num < ord ('A'):
                    num +=26
            elif symbol.islower():
                if num > ord ('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
key = getKey()

print('Your translated text is :')
print(getTranslatedMessage(mode, message, key))



_________----------------_________________------------_________-------------______________-------------

resultado        Criptografando

Do you wish to encrypt or decrypt a message?
e
Enter your massage:
ola hoje é dia de ser feliz
Enter your key number (1-26)
6
Your translated text is :
urg nupk Õ jog jk ykx lkrof


______________------------___________________-------------_______________--

                Descriptografando

Do you wish to encrypt or decrypt a message?
d
Enter your massage:
urg nupk Õ jog jk ykx lkrof
Enter your key number (1-26)
6
Your translated text is :
ola hoje µ dia de ser feliz


_-----_______________-----------__________________---------________________-----