import random

stroke ="ストローク"
smash = "スマッシュ"
volley = "ボレー"
lob = "ロブ"
for count in range(5):
    x = random.randint(1,10)
    if x <= 2:
        print(volley)
    elif x >= 3 and x <=4:
        print(smash)
    elif x >= 5 and x <= 6:
        print(lob)
    else:
        print(stroke)
