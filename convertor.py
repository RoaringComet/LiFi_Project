def convertor(p):
    for j in range(len(p)-1):
        b=p[j]
        m=ord(b)
        if(m==65):
            h = 0o0001
        elif(m == 66):
            h = 0o0010
        elif (m == 67):
            h = 0o0011
        elif (m == 68):
            h = 0o0020
        elif (m == 69):
            h = 0o0021
        elif (m == 70):
            h = 0o0022
        elif (m == 71):
            h = 0o0100
        elif (m == 72):
            h = 0o0101
        elif (m == 73):
            h = 0o0102
        elif (m == 74):
            h = 0o0110
        elif (m == 75):
            h = 0o0111
        elif (m == 76):
            h = 0o0112
        elif (m == 77):
            h = 0o0120
        elif (m == 78):
            h = 0o0121
        elif (m == 79):
            h = 0o0122
        elif (m == 80):
            h = 0o0200
        elif (m == 81):
            h = 0o0201
        elif (m == 82):
            h = 0o0202
        elif (m == 83):
            h = 0o0210
        elif (m == 84):
            h = 0o0211
        elif (m == 85):
            h = 0o0212
        elif (m == 86):
            h = 0o0220
        elif (m == 87):
            h = 0o0221
        elif (m == 88):
            h = 0o0222
        elif (m == 89):
            h = 1000
        elif (m == 90):
            h = 1001
        elif (m == 124):
            h = 2222
        elif (m == 32):
            h == 2112
        elif (m == 46):
            h == 2102
        elif (m == 44):
            h == 2110
        elif (m == 63):
            h == 2111
        else:
            print("error")
    print(h,end="")
p=input("enter the string")
convertor(p)


