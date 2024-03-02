string = "abCCC"
result = 0

def upper_or_lover_case(str, rezult):
    for x in str:
        if x == x.upper():
            rezult += 1
    print(rezult)


upper_or_lover_case(str=string, rezult=result)
