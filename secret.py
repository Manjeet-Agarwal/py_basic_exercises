user_input= int(input("what you want to do with message\n1.Encoding\n2.Decoding:\nchoose the option number: "))

if user_input!=1 and user_input!=2:
    print("enter valid choice")
en_output=[]
de_output=[]
def encoding():
    en_input= input("give the string you want to be encoded: ")
    for i in en_input.split():
        if len(i)<=2:
           en_output.append(i[::-1])
        elif len(i)>2:
            char=i[1:]+i[0]
            en_output.append(char)
    #return en_output
    str_output=" ".join(en_output)
    print(str_output)

def decoding():
    de_input= input("give the string you want to be decoded: ")
    for i in de_input.split():
        if len(i)<=2:
            de_output.append(i[::-1])
        elif len(i)>2:
            char=i[-1]+i[:-1]
            de_output.append(char)
    str_output=" ".join(de_output)
    print(str_output)


if user_input==1:
    encoding()
elif user_input==2:
    decoding()
