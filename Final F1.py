
# conversion program of p into 3 base system
def convertor(p):
   # print(p)
    h = ""
    for j in range(len(p)):
        b = p[j]
        m = ord(b)
        # ascii 65 = 'A'
        if (m == 65):
            h += "0001"+"2222"
        elif (m == 66):
            h += "0010"+"2222"
        elif (m == 67):
            h += "0011"+"2222"
            print("2222")
        elif (m == 68):
            h += "0020"+"2222"
        elif (m == 69):
            h += "0021"+"2222"
        elif (m == 70):
            h += "0022"+"2222"
        elif (m == 71):
            h += "0100"+"2222"
        elif (m == 72):
            h += "0101"+"2222"
        elif (m == 73):
            h += "0102"+"2222"
        elif (m == 74):
            h += "0110"+"2222"
        elif (m == 75):
            h += "0111"+"2222"
        elif (m == 76):
            h += "0112"+"2222"
        elif (m == 77):
            h += "0120"+"2222"
        elif (m == 78):
            h += "0121"+"2222"
        elif (m == 79):
            h += "0122"+"2222"
        elif (m == 80):
            h += "0200"+"2222"
        elif (m == 81):
            h += "0201"+"2222"
        elif (m == 82):
            h += "0202"+"2222"
        elif (m == 83):
            h += "0210"+"2222"
        elif (m == 84):
            h += "0211"+"2222"
        elif (m == 85):
            h += "0212"+"2222"
        elif (m == 86):
            h += "0220"+"2222"
        elif (m == 87):
            h += "0221"+"2222"
        elif (m == 88):
            h += "0222"+"2222"
        elif (m == 89):
            h += "1000"+"2222"
        # ascii 90 = ' Z '
        elif (m == 90):
            h += "1001"+"2222"
        elif (m == 124):
            h += "2222"+"2222"
        elif (m == 32):
            h += "2112"+"2222"
        elif (m == 46):
            h += "2102"+"2222"
        elif (m == 44):
            h += "2110"+"2222"
        elif (m == 63):
            h += "2111"+"2222"
        else:
            print("error")

    print(h,end="")
   # to indicate the finishing of a string 8 , 1's are given
   # i.e. the combination ' 222211111111 ' indicates the end of the message
    print("11111111")

while True:
    p=(input("enter the message to be coded "))
    # raw string input
    # letter separation loop
    for i in range(0,len(p)-1):
        print(p[i]+'|',end="")
    t=(p[len(p)-1])
    print(t)
    # base processed string
    convertor(p)


# for a 0 to 5 volt operation of pwm
# code      voltage
#   0           0 volts
#   1           2.5 volts
#   2           5 volts
