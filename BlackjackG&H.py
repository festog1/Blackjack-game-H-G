import random
values = []
usercard = []
osztobot = []
osztobotvalues = []
for i in range(2):
    x = random.randint(2,14)
    usercard.append(x)
    values.append(x)
for i in range(2):
    x = random.randint(2,14)
    osztobot.append(x)
    osztobotvalues.append(x)
if osztobot[1] == 11:
    osztobot[1] = "bubi"
    osztobotvalues[1] = 10
elif osztobot[1] == 12:
    osztobot[1] = "dáma"
    osztobotvalues[1] = 10
elif osztobot[1] == 13:
    osztobot[1] = "király"
    osztobotvalues[1] = 10
elif osztobot[1] == 14:
    osztobot[1] = "ász"
    osztobotvalues[1] = 10
if osztobot[0] == 11:
    osztobot[0] = "bubi"
    osztobotvalues[0] = 10
elif osztobot[0] == 12:
    osztobot[0] = "dáma"
    osztobotvalues[0] = 10
elif osztobot[0] == 13:
    osztobotvalues[0] = "király"
    osztobotvalues[0] = 10
elif osztobot[0] == 14:
    osztobot[0] = "ász"
    osztobotvalues[0] = 10

if usercard[1] == 11:
    usercard[1] = "bubi"
    values[1] = 10
elif usercard[1] == 12:
    usercard[1] = "dáma"
    values[1] = 10
elif usercard[1] == 13:
    usercard[1] = "király"
    values[1] = 10
elif usercard[1] == 14:
    usercard[1] = "ász"
    values[1] = 10
if usercard[0] == 11:
    usercard[0] = "bubi"
    values[0] = 10
elif usercard[0] == 12:
    usercard[0] = "dáma"
    values[0] = 10
elif usercard[0] == 13:
    usercard[0] = "király"
    values[0] = 10
elif usercard[0] == 14:
    usercard[0] = "ász"
    values[0] = 10
print(f"A te kártyáid: {usercard[0]}, {usercard[1]}.")
print(f"Az osztóbot első lapja {osztobot[0]}, a második letakarva!")
osztas = osztobotvalues[0]+ osztobotvalues[1]
player = values[0]+values[1]
turn = 1
while player<21:
    turn +=1
    print("A lehetőségeid: Hit(Kérsz még lapot) vagy Stand/stay(Nem kérsz lapot, értékelsés.)")
    valasz = input("Mit lépsz? (Hit/Stand) : ").lower()
    if valasz == "hit":
        usercard.append(random.randint(2,14))
        values = usercard
        if usercard[2] == 11:
            usercard[2] = "bubi"
            values[2] = 10
        elif usercard[2] == 12:
            usercard[2] = "dáma"
            values[2] = 10
        elif usercard[2] == 13:
            usercard[2] = "király"
            values[2] = 10
        elif usercard[2] == 14:
            usercard[2] = "ász"
            values[2] = 10
        print(f"A te kártyáid: {usercard}.")
        player += values[turn]
    elif valasz == "stay" or "stand":
        if osztas > player:
            print("Vesztettél!")
            print(f"Az osztó kártyái {osztobot}, összege: {osztas}")
        elif osztas > 21:
            print("Vesztettél")
            print(f"Az osztó kártyái {osztobot}, összege: {osztas}")

        else:
            print("Nyertél")
            print(f"Az osztó kártyái {osztobot}, összege: {osztas}")
            break
    else:
        print("what?")
    if osztas<16:
        print("Az osztó kártyáinak értéke 16 alatt volt és húzott!")
        osztobot.append(random.randint(2,14))
        osztobotvalues = osztobot
        if osztobot[2] == 11:
            osztobot[2] = "bubi"
            osztobotvalues[2] = 10
        elif osztobot[2] == 12:
            osztobot[2] = "dáma"
            osztobotvalues[2] = 10
        elif osztobot[2] == 13:
            osztobot[2] = "király"
            osztobotvalues[2] = 10
        elif osztobot[2] == 14:
            osztobot[2] = "ász"
            osztobotvalues[2] = 10
        osztas += osztobotvalues[turn]
if player >21:
    print("Vesztettél!")
    print(f"Az osztó kártyái {osztobot}, összege: {osztas}")
