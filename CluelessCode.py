print ("Hi!")
print ("HELLO")
suggestedbase = "dress"
base = input("Due to the weather, I suggest " + suggestedbase + ", but what are YOU feeling?")
if base == suggestedbase:
    print("Yay!")

dateres = "Pink Dress"
workres = "Grey Dress"
shopres = "Baby Blue Dress"
otherres = "Green Dress"

daintyres = " and a Cardigan"
classicres = " and a Blazer"


activity = input("What are you doing today?")
print(activity + "? How fun!")

vibe = input("What's the vibe today?")
print(vibe + "! Love it!")

if activity == "work":
    base_one = workres
elif activity == "date":
    base_one = dateres
elif activity == "shopping":
    base_one = shopres
else:
    base_one = otherres

if vibe == "dainty":
    base_two = daintyres
elif vibe == "classic":
    base_two = classicres
else:
    base_two = ""

baseoutfit = (base_one + base_two)
print(baseoutfit)

if baseoutfit == workres + classicres:
    print("and a tote!")
else:
    print("and a clutch")