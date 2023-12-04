#encryption/ decription key
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
       
coded_message = 'Bttije xh pi Adcsdc-Tnt pi 9eb hwpge'

def get_originalmessage(message):
    for l in message:
        return l

def translate(message, key):
    translated = ''
    for l in message:
        if l in key:
            translated += key[l]
        else:
            translated += l
    return translated

print(translate(coded_message, key))

ROT1 = {'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i', 
       'i':'j', 'j':'k', 'k':'l', 'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p':'q', 
       'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 'x':'y',
       'y':'z', 'z':'a', 'A':'B', 'B':'C', 'C':'D', 'D':'E', 'E':'F', 'F':'G', 
       'G':'H', 'H':'I', 'I':'J', 'J':'K', 'K':'L', 'L':'M', 'M':'N', 'N':'O', 
       'O':'P', 'P':'Q', 'Q':'R', 'R':'S', 'S':'T', 'T':'U', 'U':'V', 'V':'W', 
       'W':'X', 'X':'Y', 'Y':'Z', 'Z':'A'}

def encode(message, key):
    coded = ''
    for l in message:
        if l in key:
            coded += key[l]
        else:
            coded += l
    return coded

def decode(coded_message, key):
    decoded = ''
    for l in coded_message:
        if l in key:
            for c in key:
                if l == key[c]:
                    decoded += c
        else:
            decoded += l
    return decoded

def make_key(rot_value):
    '''put in the rot value for your caesar cypher key, eg rot value of 1 means a = b etc...'''
    key = {}
    for l in 'abcdefghijklmnopqrstuvwxyz':
        if ord(l) + rot_value > 122:
            key[l] = chr(ord(l) + rot_value - 26)
        elif ord(l) + rot_value < 97:
            key[l] = chr(ord(l) + rot_value + 26)
        else:
            key[l] = chr(ord(l) + rot_value)
    for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if ord(l) + rot_value > 90:
            key[l] = chr(ord(l) + rot_value - 26)
        elif ord(l) + rot_value < 65:
            key[l] = chr(ord(l) + rot_value + 26)
        else:
            key[l] = chr(ord(l) + rot_value)
    return key
            
decode(coded_message, key)
