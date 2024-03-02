string = "anime", "meme", "vines", "roasts", "Danny DeVito"
inp = input("enter ...: ")
for x in string:
    if x in inp:
        print("NO!")
        break
else:
    print("Safe watching!")

