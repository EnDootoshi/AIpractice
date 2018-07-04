print("身長は？ ｃｍで入力してね")
height = float(input("あなたの身長　> "))
print("あなたの体重は？ ｋｇで入力してね")
weight = float(input("あなたの体重 > "))
bmi = 22
no_wei = bmi * (height/100) **2
print("身長が" + str(height) + "cmの場合、標準体重は" ,end= '')
print("{:.2f}kgです。".format(no_wei))
if weight >= no_wei+3:
    print("ちょっと重いかな(笑)")
elif weight <= no_wei-3:
    print("ちょっと細くない？？")
else:
    print("ちょうどいい感じの体重だね！！")
