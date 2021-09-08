#Training: ASCII
# str = [84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 98, 100, 97, 104, 111, 100, 103, 103, 115, 105, 111, 111]
# output = ''
# for i in str:
#     output = output + chr(i)

# print(output)


#Training: Crypto - Caesar I 
string = 'RFC OSGAI ZPMUL DMV HSKNQ MTCP RFC JYXW BME MD AYCQYP YLB WMSP SLGOSC QMJSRGML GQ CGDPGQLQFJZJ'

for i in range(0,25):
    print("=============="+str(i))
    for letter in string:
        if letter != ' ': 
            tmp = ((ord(letter) - 65) + i) % 26 + 65
            print(chr(tmp), end = '')
        else:
          print(letter, end = '')
    print()
