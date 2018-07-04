smash = "スマッシュ"
stroke = "ストローク"
volley = "ボレー"
for count in range(10):
    if (count >= 6) and (count % 2 == 0):
        print(volley)
    elif (count % 2　== 0):
        print(smash)
    else:
        print(stroke)
