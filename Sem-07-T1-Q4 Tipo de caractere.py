palavra=input()
vogal='aeiouAEIOU'
consoantes='qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
numero='0123456789'

if palavra in vogal:
        print('vogal')
elif palavra in consoantes:
        print('consoante')
elif palavra in numero:
        print('número')
else:
    print('símbolo')