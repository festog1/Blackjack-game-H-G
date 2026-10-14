import random
import os
import classes
money = 10000
while money > 0:
    print(f"A pénzed: {money}")
    tet = int(input("Mennyi pénzt szeretnél feltenni?: "))
    if tet <= 0:
        print("Akkor kimaradsz!")
        game = False
    else:
        screen = [
            ['🟩','🟩','🟩','🟩','🟩'],
            ['🟩','🟩','🟩','🟩','🟩'],
            ['🟩','🟩','🟩','🟩','🟩'],
            ['🟩','🟩','🟩','🟩','🟩'],
            ['🟩','🟩','🟩','🟩','🟩'],
            ['🟩','🟩','🟩','🟩','🟩'],
            ['🟩','🟩','🟩','🟩','🟩']
        ]
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
        classes.osztalyom.kartyanevek(osztobotvalues,osztobot,1)
        classes.osztalyom.kartyanevek(osztobotvalues,osztobot,0)
        classes.osztalyom.kartyanevek(values,usercard,1)
        classes.osztalyom.kartyanevek(values,usercard,0)
        ten = 0
        if usercard[0] == 10:
            ten = 5

        classes.osztalyom.card(usercard[0], 0,screen)
        classes.osztalyom.novel_x(screen)
        classes.osztalyom.card(usercard[1], 6 + ten,screen)
        classes.osztalyom.nyom(screen)
        print(f"A te kártyáid: {usercard[0]}, {usercard[1]}.")
        print(f"Az osztóbot első lapja {osztobot[0]}, a második letakarva!")
        enemyscreen = [
            ['🟩','🟩','🟩','🟩','🟩'],
            ['🟩','🟩','🟩','🟩','🟩'],
            ['🟩','🟩','🟩','🟩','🟩'],
            ['🟩','🟩','🟩','🟩','🟩'],
            ['🟩','🟩','🟩','🟩','🟩'],
            ['🟩','🟩','🟩','🟩','🟩'],
            ['🟩','🟩','🟩','🟩','🟩']
        ]
        classes.osztalyom.enemycard(osztobot[0], 0,enemyscreen)
        classes.osztalyom.enemynyom(enemyscreen)
        osztas = osztobotvalues[0]+ osztobotvalues[1]
        player = values[0]+values[1]
        turn = 1
        game = True
        cards = 2
        botcard = 2
        while player<=21 and game == True:
            turn +=1
            print("A lehetőségeid: Hit(Kérsz még lapot) vagy Stand/stay(Nem kérsz lapot, értékelsés.)")
            valasz = input("Mit lépsz? (Hit/Stand) : ").lower()
            if valasz == "hit":
                x = random.randint(2, 14)
                usercard.append(x)
                values.append(x)
                classes.osztalyom.kartyanevek(values, usercard, -1)
                if usercard[-2] == 10:
                    ten += 5
                classes.osztalyom.novel_x(screen)
                classes.osztalyom.card(usercard[-1], (cards * 6) + ten,screen)
                classes.osztalyom.nyom(screen)   
                player += values[-1]
                cards += 1
                print(f"A te kártyáid: {usercard}.")
            elif valasz == "stay" or valasz == "stand":
                if osztas > player:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Vesztettél!")
                    money -= tet
                    print(f"Az osztó kártyái {osztobot}, összege: {osztas}")
                    game = False
                elif osztas > 21 or player > osztas:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Nyertél")
                    money += tet*2
                    print(f"Az osztó kártyái {osztobot}, összege: {osztas}")
                    game = False
            elif osztas == player:
                print("Az osztás és a játékos kártyái egyenlőek!")
            else:
                print("what?")
            if osztas<16:
                print("Az osztó kártyáinak értéke 16 alatt volt és húzott!")
                x = random.randint(2,14)
                osztobot.append(x)
                osztobotvalues.append(x)
                classes.osztalyom.kartyanevek(osztobotvalues,osztobot,botcard)
                osztas += osztobotvalues[turn]
        if player >21:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Vesztettél!")
            money -= int(tet)
            print(f"Az osztó kártyái {osztobot}, összege: {osztas}") 
print(f"A pénzed: {money}")