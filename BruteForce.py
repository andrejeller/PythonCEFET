programa

# Cesar Chiper

MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt or brute force a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d brute b' . split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".')
 
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
if mode[0] != 'b':
    key = getKey()

print('Your translated text is :')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))
-_________________-------------____________________-----------______________-

          criptografando


Do you wish to encrypt or decrypt or brute force a message?
b
Enter your massage:
ola hoje temos almoço
Your translated text is :
1 nkz gnid sdlnr zklnÌn
2 mjy fmhc rckmq yjkmËm
3 lix elgb qbjlp xijlÊl
4 khw dkfa paiko whikÉk
5 jgv cjez ozhjn vghjÈj
6 ifu bidy nygim ufgiÇi
7 het ahcx mxfhl tefhÆh
8 gds zgbw lwegk sdegÅg
9 fcr yfav kvdfj rcdfÄf
10 ebq xezu jucei qbceÃe
11 dap wdyt itbdh pabdÂd
12 czo vcxs hsacg ozacÁc
13 byn ubwr grzbf nyzbÀb
14 axm tavq fqyae mxya¿a
15 zwl szup epxzd lwxz¾z
16 yvk ryto dowyc kvwy½y
17 xuj qxsn cnvxb juvx¼x
18 wti pwrm bmuwa ituw»w
19 vsh ovql altvz hstvºv
20 urg nupk zksuy grsu¹u
21 tqf mtoj yjrtx fqrt¸t
22 spe lsni xiqsw epqs·s
23 rod krmh whprv dopr¶r
24 qnc jqlg vgoqu cnoqµq
25 pmb ipkf ufnpt bmnp´p
26 ola hoje temos almo³o
_________-----_________________----____________-----___________--

            descriptografando


Do you wish to encrypt or decrypt or brute force a message?
b
Enter your massage:
urg nupk zksuy grsu¹u
Your translated text is :
1 tqf mtoj yjrtx fqrt¹t
2 spe lsni xiqsw epqs¹s
3 rod krmh whprv dopr¹r
4 qnc jqlg vgoqu cnoq¹q
5 pmb ipkf ufnpt bmnp¹p
6 ola hoje temos almo¹o
7 nkz gnid sdlnr zkln¹n
8 mjy fmhc rckmq yjkm¹m
9 lix elgb qbjlp xijl¹l
10 khw dkfa paiko whik¹k
11 jgv cjez ozhjn vghj¹j
12 ifu bidy nygim ufgi¹i
13 het ahcx mxfhl tefh¹h
14 gds zgbw lwegk sdeg¹g
15 fcr yfav kvdfj rcdf¹f
16 ebq xezu jucei qbce¹e
17 dap wdyt itbdh pabd¹d
18 czo vcxs hsacg ozac¹c
19 byn ubwr grzbf nyzb¹b
20 axm tavq fqyae mxya¹a
21 zwl szup epxzd lwxz¹z
22 yvk ryto dowyc kvwy¹y
23 xuj qxsn cnvxb juvx¹x
24 wti pwrm bmuwa ituw¹w
25 vsh ovql altvz hstv¹v
26 urg nupk zksuy grsu¹u