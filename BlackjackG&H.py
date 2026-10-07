import random
values = []
usercard = []
osztobot = []
osztobotvalues = []
for i in range(2):
    usercard.append(random.randint(2,14))
    values = usercard
for i in range(2):
    osztobot.append(random.randint(2,14))
    osztobotvalues = osztobot
if osztobot[1] == 11:
    osztobot[1] = "bubi"
    osztobotvalues[1] == 10
elif osztobot[1] == 12:
    osztobot[1] = "dáma"
    osztobotvalues[1] == 10
elif osztobot[1] == 13:
    usercard[1] = "király"
    osztobotvalues[1] == 10
elif osztobot[1] == 14:
    osztobot[1] = "ász"
    osztobotvalues[1] == 10

if usercard[1] == 11:
    usercard[1] = "bubi"
    values[1] == 10
elif usercard[1] == 12:
    usercard[1] = "dáma"
    values[1] == 10
elif usercard[1] == 13:
    usercard[1] = "király"
    values[1] == 10
elif usercard[1] == 14:
    usercard[1] = "ász"
    values[1] == 10
print(f"A te kártyáid: {usercard[0]}, {usercard[1]}.")
print(f"Az osztóbot első lapja {osztobot[0]}, a második letakarva!")