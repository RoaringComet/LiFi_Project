n=(input("enter the message to be coded "))
# letter separation loop
for i in range(0,len(n)-1):
    print(n[i]+'|',end="")
p=(n[len(n)-1])
print(p)
h = ""
for j in range(len(p)):
    b = p[j]
    m = ord(b)
    if (m == 65):
        h += "0001"
    elif (m == 66):
        h += "0010"
    elif (m == 67):
        h += "0011"
    elif (m == 68):
        h += "0020"
    elif (m == 69):
        h += "0021"
    elif (m == 70):
        h += "0022"
    elif (m == 71):
        h += "0100"
    elif (m == 72):
        h += "0101"
    elif (m == 73):
        h += "0102"
    elif (m == 74):
        h += "0110"
    elif (m == 75):
        h += "0111"
    elif (m == 76):
        h += "0112"
    elif (m == 77):
        h += "0120"
    elif (m == 78):
        h += "0121"
    elif (m == 79):
        h += "0122"
    elif (m == 80):
        h += "0200"
    elif (m == 81):
        h += "0201"
    elif (m == 82):
        h += "0202"
    elif (m == 83):
        h += "0210"
    elif (m == 84):
        h += "0211"
    elif (m == 85):
        h += "0212"
    elif (m == 86):
        h += "0220"
    elif (m == 87):
        h += "0221"
    elif (m == 88):
        h += "0222"
    elif (m == 89):
        h += "1000"
    elif (m == 90):
        h += "1001"
    elif (m == 124):
        h += "2222"
    elif (m == 32):
        h += "2112"
    elif (m == 46):
        h += "2102"
    elif (m == 44):
        h += "2110"
    elif (m == 63):
        h += "2111"
    else:
        print("error")

print(h)