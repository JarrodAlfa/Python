import  random
dobbel = 0
teller = 0
while dobbel < 12:teller += 1
dobbel = (random.randint(1, 6) + random.randint(1, 6))
print(str(dobbel) + " poging " + str(teller))