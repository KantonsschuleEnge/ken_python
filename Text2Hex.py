# filename: Text2Hex.py
# author:   gregor luedi
# date:     

import binascii

def hexText(s):
    s =s.encode('ascii')
    return binascii.b2a_hex(s)

def hexTextreverse(s):
    s =s.encode('ascii')[::-1]
    return binascii.b2a_hex(s)    

def isValid(s):
    if len(s)%4==0:
        return True
    else:
        return False

def generateCode(s):
    text = hexTextreverse(s)
    splits=[text[x:x+8] for x in range(0,len(text),8)]
    code = ''
    for item in splits:
        code =code + 'push 0x'+item.decode('ascii')+'\n'

    return code

def main():
    code = 'Hello World\n'
    print(hexTextreverse(code))
    print(generateCode(code))

if __name__ == '__main__':main()
