def c_n_v_s(string):
    vowels="aeiouAEIOU"
    digits="0123456789"
    spec="!@#$%^&*|"
    vc=dc=scc=cc=0

    for i in string:
        if i.isalpha():
            if i in vowels:
                vc+=1
            else:
                cc+=1
        elif i.isdigit():
            dc+=1
        elif i in spec:
            scc+=1
    print("Vowels:",vc)
    print("Consoants:",cc)
    print("Number:",dc)
    print("Special Characters:",scc)
            
string=input("enter a string:")
c_n_v_s(string)


    



