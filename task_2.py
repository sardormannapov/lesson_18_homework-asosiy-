string = "moveMENT"

def cap_to_front(str):
    result1 = []
    result2 = []
    for x in str:
        if x.isupper():
            result1.append(x)
        else:
            result2.append(x)

    print("".join(result1 + result2))


cap_to_front(str=string)
