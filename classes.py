class osztalyom:
    def kartyanevek(ertek, kartya,szam):
        if kartya[szam] == 11:
            kartya[szam] = "bubi"
            ertek[szam] = 10
        elif kartya[szam] == 12:
            kartya[szam] = "dáma"
            ertek[szam] = 10
        elif kartya[szam] == 13:
            kartya[szam] = "király"
            ertek[szam] = 10
        elif kartya[szam] == 14:
            kartya[szam] = "ász"
            ertek[szam] = 10
    def nyom(screen):   
        for x in range(len(screen)):
            for y in range(len(screen[x])):
                print(screen[x][y] ,end ="")
            print("")
    def enemynyom(enemyscreen):   
        for x in range(len(enemyscreen)):
            for y in range(len(enemyscreen[x])):
                print(enemyscreen[x][y] ,end ="")
            print("")
    def card(num, tav,screen):
        if num == 0:
            screen[1][tav + 1] = '🟥'; screen[1][tav + 2] = '🟥'; screen[1][tav + 3] = '🟥'
            screen[2][tav + 1] = '🟥'; screen[2][tav + 2] = '⬜'; screen[2][tav + 3] = '🟥'
            screen[3][tav + 1] = '🟥'; screen[3][tav + 2] = '⬜'; screen[3][tav + 3] = '🟥'
            screen[4][tav + 1] = '🟥'; screen[4][tav + 2] = '⬜'; screen[4][tav + 3] = '🟥'
            screen[5][tav + 1] = '🟥'; screen[5][tav + 2] = '🟥'; screen[5][tav + 3] = '🟥'

        if num == 1:
            screen[1][tav + 1] = '⬜'; screen[1][tav + 2] = '🟥'; screen[1][tav + 3] = '⬜'
            screen[2][tav + 1] = '🟥'; screen[2][tav + 2] = '🟥'; screen[2][tav + 3] = '⬜'
            screen[3][tav + 1] = '⬜'; screen[3][tav + 2] = '🟥'; screen[3][tav + 3] = '⬜'
            screen[4][tav + 1] = '⬜'; screen[4][tav + 2] = '🟥'; screen[4][tav + 3] = '⬜'
            screen[5][tav + 1] = '🟥'; screen[5][tav + 2] = '🟥'; screen[5][tav + 3] = '🟥'
        if num == 2:
            screen[1][tav + 1] = '🟥';screen[1][tav + 2] = '🟥';screen[1][tav + 3] = '🟥'
            screen[2][tav + 1] = '⬜';screen[2][tav + 2] = '⬜';screen[2][tav + 3] = '🟥'
            screen[3][tav + 1] = '🟥';screen[3][tav + 2] = '🟥';screen[3][tav + 3] = '🟥'
            screen[4][tav + 1] = '🟥';screen[4][tav + 2] = '⬜';screen[4][tav + 3] = '⬜'
            screen[5][tav + 1] = '🟥';screen[5][tav + 2] = '🟥';screen[5][tav + 3] = '🟥'
        if num == 3:
            screen[1][tav + 1] = '🟥'; screen[1][tav + 2] = '🟥'; screen[1][tav + 3] = '🟥'
            screen[2][tav + 1] = '⬜'; screen[2][tav + 2] = '⬜'; screen[2][tav + 3] = '🟥'
            screen[3][tav + 1] = '🟥'; screen[3][tav + 2] = '🟥'; screen[3][tav + 3] = '🟥'
            screen[4][tav + 1] = '⬜'; screen[4][tav + 2] = '⬜'; screen[4][tav + 3] = '🟥'
            screen[5][tav + 1] = '🟥'; screen[5][tav + 2] = '🟥'; screen[5][tav + 3] = '🟥'

        if num == 4:
            screen[1][tav + 1] = '🟥'; screen[1][tav + 2] = '⬜'; screen[1][tav + 3] = '🟥'
            screen[2][tav + 1] = '🟥'; screen[2][tav + 2] = '⬜'; screen[2][tav + 3] = '🟥'
            screen[3][tav + 1] = '🟥'; screen[3][tav + 2] = '🟥'; screen[3][tav + 3] = '🟥'
            screen[4][tav + 1] = '⬜'; screen[4][tav + 2] = '⬜'; screen[4][tav + 3] = '🟥'
            screen[5][tav + 1] = '⬜'; screen[5][tav + 2] = '⬜'; screen[5][tav + 3] = '🟥'

        if num == 5:
            screen[1][tav + 1] = '🟥'; screen[1][tav + 2] = '🟥'; screen[1][tav + 3] = '🟥'
            screen[2][tav + 1] = '🟥'; screen[2][tav + 2] = '⬜'; screen[2][tav + 3] = '⬜'
            screen[3][tav + 1] = '🟥'; screen[3][tav + 2] = '🟥'; screen[3][tav + 3] = '🟥'
            screen[4][tav + 1] = '⬜'; screen[4][tav + 2] = '⬜'; screen[4][tav + 3] = '🟥'
            screen[5][tav + 1] = '🟥'; screen[5][tav + 2] = '🟥'; screen[5][tav + 3] = '🟥'

        if num == 6:
            screen[1][tav + 1] = '🟥'; screen[1][tav + 2] = '🟥'; screen[1][tav + 3] = '🟥'
            screen[2][tav + 1] = '🟥'; screen[2][tav + 2] = '⬜'; screen[2][tav + 3] = '⬜'
            screen[3][tav + 1] = '🟥'; screen[3][tav + 2] = '🟥'; screen[3][tav + 3] = '🟥'
            screen[4][tav + 1] = '🟥'; screen[4][tav + 2] = '⬜'; screen[4][tav + 3] = '🟥'
            screen[5][tav + 1] = '🟥'; screen[5][tav + 2] = '🟥'; screen[5][tav + 3] = '🟥'

        if num == 7:
            screen[1][tav + 1] = '🟥'; screen[1][tav + 2] = '🟥'; screen[1][tav + 3] = '🟥'
            screen[2][tav + 1] = '⬜'; screen[2][tav + 2] = '⬜'; screen[2][tav + 3] = '🟥'
            screen[3][tav + 1] = '⬜'; screen[3][tav + 2] = '⬜'; screen[3][tav + 3] = '🟥'
            screen[4][tav + 1] = '⬜'; screen[4][tav + 2] = '⬜'; screen[4][tav + 3] = '🟥'
            screen[5][tav + 1] = '⬜'; screen[5][tav + 2] = '⬜'; screen[5][tav + 3] = '🟥'

        if num == 8:
            screen[1][tav + 1] = '🟥'; screen[1][tav + 2] = '🟥'; screen[1][tav + 3] = '🟥'
            screen[2][tav + 1] = '🟥'; screen[2][tav + 2] = '⬜'; screen[2][tav + 3] = '🟥'
            screen[3][tav + 1] = '🟥'; screen[3][tav + 2] = '🟥'; screen[3][tav + 3] = '🟥'
            screen[4][tav + 1] = '🟥'; screen[4][tav + 2] = '⬜'; screen[4][tav + 3] = '🟥'
            screen[5][tav + 1] = '🟥'; screen[5][tav + 2] = '🟥'; screen[5][tav + 3] = '🟥'

        if num == 9:
            screen[1][tav + 1] = '🟥'; screen[1][tav + 2] = '🟥'; screen[1][tav + 3] = '🟥'
            screen[2][tav + 1] = '🟥'; screen[2][tav + 2] = '⬜'; screen[2][tav + 3] = '🟥'
            screen[3][tav + 1] = '🟥'; screen[3][tav + 2] = '🟥'; screen[3][tav + 3] = '🟥'
            screen[4][tav + 1] = '⬜'; screen[4][tav + 2] = '⬜'; screen[4][tav + 3] = '🟥'
            screen[5][tav + 1] = '🟥'; screen[5][tav + 2] = '🟥'; screen[5][tav + 3] = '🟥'
        if num == 10:
            osztalyom.card(1, tav,screen)
            for i in range(len(screen)):
                for o in range(5):
                    screen[i].append('🟩')
            osztalyom.card(0, tav + 5,screen)
            return
        if num == 'bubi':
            screen[1][tav + 1] = '🟥'; screen[1][tav + 2] = '🟥'; screen[1][tav + 3] = '🟥'
            screen[2][tav + 1] = '⬜'; screen[2][tav + 2] = '🟥'; screen[2][tav + 3] = '⬜'
            screen[3][tav + 1] = '⬜'; screen[3][tav + 2] = '🟥'; screen[3][tav + 3] = '⬜'
            screen[4][tav + 1] = '🟥'; screen[4][tav + 2] = '🟥'; screen[4][tav + 3] = '⬜'
            screen[5][tav + 1] = '🟥'; screen[5][tav + 2] = '🟥'; screen[5][tav + 3] = '⬜'
        if num == 'dáma':
            screen[1][tav + 1] = '🟥'; screen[1][tav + 2] = '🟥'; screen[1][tav + 3] = '🟥'
            screen[2][tav + 1] = '🟥'; screen[2][tav + 2] = '⬜'; screen[2][tav + 3] = '🟥'
            screen[3][tav + 1] = '🟥'; screen[3][tav + 2] = '🟥'; screen[3][tav + 3] = '🟥'
            screen[4][tav + 1] = '⬜'; screen[4][tav + 2] = '⬜'; screen[4][tav + 3] = '🟥'
            screen[5][tav + 1] = '⬜'; screen[5][tav + 2] = '⬜'; screen[5][tav + 3] = '🟥'
        if num == 'király':
            screen[1][tav + 1] = '🟥'; screen[1][tav + 2] = '⬜'; screen[1][tav + 3] = '🟥'
            screen[2][tav + 1] = '🟥'; screen[2][tav + 2] = '⬜'; screen[2][tav + 3] = '🟥'
            screen[3][tav + 1] = '🟥'; screen[3][tav + 2] = '🟥'; screen[3][tav + 3] = '⬜'
            screen[4][tav + 1] = '🟥'; screen[4][tav + 2] = '⬜'; screen[4][tav + 3] = '🟥'
            screen[5][tav + 1] = '🟥'; screen[5][tav + 2] = '⬜'; screen[5][tav + 3] = '🟥'
        if num == 'ász':
            screen[1][tav + 1] = '🟥'; screen[1][tav + 2] = '🟥'; screen[1][tav + 3] = '🟥'
            screen[2][tav + 1] = '🟥'; screen[2][tav + 2] = '⬜'; screen[2][tav + 3] = '🟥'
            screen[3][tav + 1] = '🟥'; screen[3][tav + 2] = '🟥'; screen[3][tav + 3] = '🟥'
            screen[4][tav + 1] = '🟥'; screen[4][tav + 2] = '⬜'; screen[4][tav + 3] = '🟥'
            screen[5][tav + 1] = '🟥'; screen[5][tav + 2] = '⬜'; screen[5][tav + 3] = '🟥'
    def enemycard(num, tav,enemyscreen): 
        if num == 0: 
            enemyscreen[1][tav + 1] = '⬛'; enemyscreen[1][tav + 2] = '⬛'; enemyscreen[1][tav + 3] = '⬛' 
            enemyscreen[2][tav + 1] = '⬛'; enemyscreen[2][tav + 2] = '⬜'; enemyscreen[2][tav + 3] = '⬛' 
            enemyscreen[3][tav + 1] = '⬛'; enemyscreen[3][tav + 2] = '⬜'; enemyscreen[3][tav + 3] = '⬛' 
            enemyscreen[4][tav + 1] = '⬛'; enemyscreen[4][tav + 2] = '⬜'; enemyscreen[4][tav + 3] = '⬛' 
            enemyscreen[5][tav + 1] = '⬛'; enemyscreen[5][tav + 2] = '⬛'; enemyscreen[5][tav + 3] = '⬛' 
        if num == 1: 
            enemyscreen[1][tav + 1] = '⬜'; enemyscreen[1][tav + 2] = '⬛'; enemyscreen[1][tav + 3] = '⬜' 
            enemyscreen[2][tav + 1] = '⬛'; enemyscreen[2][tav + 2] = '⬛'; enemyscreen[2][tav + 3] = '⬜' 
            enemyscreen[3][tav + 1] = '⬜'; enemyscreen[3][tav + 2] = '⬛'; enemyscreen[3][tav + 3] = '⬜' 
            enemyscreen[4][tav + 1] = '⬜'; enemyscreen[4][tav + 2] = '⬛'; enemyscreen[4][tav + 3] = '⬜' 
            enemyscreen[5][tav + 1] = '⬛'; enemyscreen[5][tav + 2] = '⬛'; enemyscreen[5][tav + 3] = '⬛' 
        if num == 2: 
            enemyscreen[1][tav + 1] = '⬛';enemyscreen[1][tav + 2] = '⬛';enemyscreen[1][tav + 3] = '⬛' 
            enemyscreen[2][tav + 1] = '⬜';enemyscreen[2][tav + 2] = '⬜';enemyscreen[2][tav + 3] = '⬛' 
            enemyscreen[3][tav + 1] = '⬛';enemyscreen[3][tav + 2] = '⬛';enemyscreen[3][tav + 3] = '⬛' 
            enemyscreen[4][tav + 1] = '⬛';enemyscreen[4][tav + 2] = '⬜';enemyscreen[4][tav + 3] = '⬜' 
            enemyscreen[5][tav + 1] = '⬛';enemyscreen[5][tav + 2] = '⬛';enemyscreen[5][tav + 3] = '⬛' 
        if num == 3: 
            enemyscreen[1][tav + 1] = '⬛'; enemyscreen[1][tav + 2] = '⬛'; enemyscreen[1][tav + 3] = '⬛' 
            enemyscreen[2][tav + 1] = '⬜'; enemyscreen[2][tav + 2] = '⬜'; enemyscreen[2][tav + 3] = '⬛' 
            enemyscreen[3][tav + 1] = '⬛'; enemyscreen[3][tav + 2] = '⬛'; enemyscreen[3][tav + 3] = '⬛' 
            enemyscreen[4][tav + 1] = '⬜'; enemyscreen[4][tav + 2] = '⬜'; enemyscreen[4][tav + 3] = '⬛' 
            enemyscreen[5][tav + 1] = '⬛'; enemyscreen[5][tav + 2] = '⬛'; enemyscreen[5][tav + 3] = '⬛' 
        if num == 4: 
            enemyscreen[1][tav + 1] = '⬛'; enemyscreen[1][tav + 2] = '⬜'; enemyscreen[1][tav + 3] = '⬛' 
            enemyscreen[2][tav + 1] = '⬛'; enemyscreen[2][tav + 2] = '⬜'; enemyscreen[2][tav + 3] = '⬛' 
            enemyscreen[3][tav + 1] = '⬛'; enemyscreen[3][tav + 2] = '⬛'; enemyscreen[3][tav + 3] = '⬛' 
            enemyscreen[4][tav + 1] = '⬜'; enemyscreen[4][tav + 2] = '⬜'; enemyscreen[4][tav + 3] = '⬛' 
            enemyscreen[5][tav + 1] = '⬜'; enemyscreen[5][tav + 2] = '⬜'; enemyscreen[5][tav + 3] = '⬛' 
        if num == 5: 
            enemyscreen[1][tav + 1] = '⬛'; enemyscreen[1][tav + 2] = '⬛'; enemyscreen[1][tav + 3] = '⬛' 
            enemyscreen[2][tav + 1] = '⬛'; enemyscreen[2][tav + 2] = '⬜'; enemyscreen[2][tav + 3] = '⬜' 
            enemyscreen[3][tav + 1] = '⬛'; enemyscreen[3][tav + 2] = '⬛'; enemyscreen[3][tav + 3] = '⬛' 
            enemyscreen[4][tav + 1] = '⬜'; enemyscreen[4][tav + 2] = '⬜'; enemyscreen[4][tav + 3] = '⬛' 
            enemyscreen[5][tav + 1] = '⬛'; enemyscreen[5][tav + 2] = '⬛'; enemyscreen[5][tav + 3] = '⬛' 
        if num == 6: 
            enemyscreen[1][tav + 1] = '⬛'; enemyscreen[1][tav + 2] = '⬛'; enemyscreen[1][tav + 3] = '⬛' 
            enemyscreen[2][tav + 1] = '⬛'; enemyscreen[2][tav + 2] = '⬜'; enemyscreen[2][tav + 3] = '⬜' 
            enemyscreen[3][tav + 1] = '⬛'; enemyscreen[3][tav + 2] = '⬛'; enemyscreen[3][tav + 3] = '⬛' 
            enemyscreen[4][tav + 1] = '⬛'; enemyscreen[4][tav + 2] = '⬜'; enemyscreen[4][tav + 3] = '⬛' 
            enemyscreen[5][tav + 1] = '⬛'; enemyscreen[5][tav + 2] = '⬛'; enemyscreen[5][tav + 3] = '⬛' 
        if num == 7: 
            enemyscreen[1][tav + 1] = '⬛'; enemyscreen[1][tav + 2] = '⬛'; enemyscreen[1][tav + 3] = '⬛' 
            enemyscreen[2][tav + 1] = '⬜'; enemyscreen[2][tav + 2] = '⬜'; enemyscreen[2][tav + 3] = '⬛' 
            enemyscreen[3][tav + 1] = '⬜'; enemyscreen[3][tav + 2] = '⬜'; enemyscreen[3][tav + 3] = '⬛' 
            enemyscreen[4][tav + 1] = '⬜'; enemyscreen[4][tav + 2] = '⬜'; enemyscreen[4][tav + 3] = '⬛' 
            enemyscreen[5][tav + 1] = '⬜'; enemyscreen[5][tav + 2] = '⬜'; enemyscreen[5][tav + 3] = '⬛' 
        if num == 8: 
            enemyscreen[1][tav + 1] = '⬛'; enemyscreen[1][tav + 2] = '⬛'; enemyscreen[1][tav + 3] = '⬛' 
            enemyscreen[2][tav + 1] = '⬛'; enemyscreen[2][tav + 2] = '⬜'; enemyscreen[2][tav + 3] = '⬛' 
            enemyscreen[3][tav + 1] = '⬛'; enemyscreen[3][tav + 2] = '⬛'; enemyscreen[3][tav + 3] = '⬛' 
            enemyscreen[4][tav + 1] = '⬛'; enemyscreen[4][tav + 2] = '⬜'; enemyscreen[4][tav + 3] = '⬛' 
            enemyscreen[5][tav + 1] = '⬛'; enemyscreen[5][tav + 2] = '⬛'; enemyscreen[5][tav + 3] = '⬛' 
        if num == 9: 
            enemyscreen[1][tav + 1] = '⬛'; enemyscreen[1][tav + 2] = '⬛'; enemyscreen[1][tav + 3] = '⬛' 
            enemyscreen[2][tav + 1] = '⬛'; enemyscreen[2][tav + 2] = '⬜'; enemyscreen[2][tav + 3] = '⬛' 
            enemyscreen[3][tav + 1] = '⬛'; enemyscreen[3][tav + 2] = '⬛'; enemyscreen[3][tav + 3] = '⬛' 
            enemyscreen[4][tav + 1] = '⬜'; enemyscreen[4][tav + 2] = '⬜'; enemyscreen[4][tav + 3] = '⬛' 
            enemyscreen[5][tav + 1] = '⬛'; enemyscreen[5][tav + 2] = '⬛'; enemyscreen[5][tav + 3] = '⬛' 
        if num == 10: 
            osztalyom.enemycard(1, tav, enemyscreen) 
            for i in range(len(enemyscreen)): 
                for o in range(5): 
                    enemyscreen[i].append('🟩') 
            osztalyom.enemycard(0, tav + 5, enemyscreen) 
            return 
        if num == 'bubi': 
            enemyscreen[1][tav + 1] = '⬛'; enemyscreen[1][tav + 2] = '⬛'; enemyscreen[1][tav + 3] = '⬛' 
            enemyscreen[2][tav + 1] = '⬜'; enemyscreen[2][tav + 2] = '⬛'; enemyscreen[2][tav + 3] = '⬜' 
            enemyscreen[3][tav + 1] = '⬜'; enemyscreen[3][tav + 2] = '⬛'; enemyscreen[3][tav + 3] = '⬜' 
            enemyscreen[4][tav + 1] = '⬛'; enemyscreen[4][tav + 2] = '⬛'; enemyscreen[4][tav + 3] = '⬜' 
            enemyscreen[5][tav + 1] = '⬛'; enemyscreen[5][tav + 2] = '⬛'; enemyscreen[5][tav + 3] = '⬜' 
        if num == 'dáma': 
            enemyscreen[1][tav + 1] = '⬛'; enemyscreen[1][tav + 2] = '⬛'; enemyscreen[1][tav + 3] = '⬛' 
            enemyscreen[2][tav + 1] = '⬛'; enemyscreen[2][tav + 2] = '⬜'; enemyscreen[2][tav + 3] = '⬛' 
            enemyscreen[3][tav + 1] = '⬛'; enemyscreen[3][tav + 2] = '⬛'; enemyscreen[3][tav + 3] = '⬛' 
            enemyscreen[4][tav + 1] = '⬜'; enemyscreen[4][tav + 2] = '⬜'; enemyscreen[4][tav + 3] = '⬛' 
            enemyscreen[5][tav + 1] = '⬜'; enemyscreen[5][tav + 2] = '⬜'; enemyscreen[5][tav + 3] = '⬛' 
        if num == 'király': 
            enemyscreen[1][tav + 1] = '⬛'; enemyscreen[1][tav + 2] = '⬜'; enemyscreen[1][tav + 3] = '⬛' 
            enemyscreen[2][tav + 1] = '⬛'; enemyscreen[2][tav + 2] = '⬜'; enemyscreen[2][tav + 3] = '⬛' 
            enemyscreen[3][tav + 1] = '⬛'; enemyscreen[3][tav + 2] = '⬛'; enemyscreen[3][tav + 3] = '⬜' 
            enemyscreen[4][tav + 1] = '⬛'; enemyscreen[4][tav + 2] = '⬜'; enemyscreen[4][tav + 3] = '⬛' 
            enemyscreen[5][tav + 1] = '⬛'; enemyscreen[5][tav + 2] = '⬜'; enemyscreen[5][tav + 3] = '⬛' 
        if num == 'ász': 
            enemyscreen[1][tav + 1] = '⬛'; enemyscreen[1][tav + 2] = '⬛'; enemyscreen[1][tav + 3] = '⬛' 
            enemyscreen[2][tav + 1] = '⬛'; enemyscreen[2][tav + 2] = '⬜'; enemyscreen[2][tav + 3] = '⬛' 
            enemyscreen[3][tav + 1] = '⬛'; enemyscreen[3][tav + 2] = '⬛'; enemyscreen[3][tav + 3] = '⬛' 
            enemyscreen[4][tav + 1] = '⬛'; enemyscreen[4][tav + 2] = '⬜'; enemyscreen[4][tav + 3] = '⬛' 
            enemyscreen[5][tav + 1] = '⬛'; enemyscreen[5][tav + 2] = '⬜'; enemyscreen[5][tav + 3] = '⬛'
    def novel_x(screen):
        for i in range(len(screen)):
            screen[i].append('🟧')
            for o in range(5):
                screen[i].append('🟩')