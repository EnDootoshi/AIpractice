from random import randint
hands = {0:"グー", 1:"チョキ", 2:"パー"}
rules = {(0,0):"あいこ", (0,1):"勝ち",(0,2):"負け", (1,0):"負け", (1,1):"あいこ", (1,2):"勝ち", (2,0):"勝ち", (2,1):"負け", (2,2):"あいこ"}

while True:
    pc_hand = randint(0,2)
    user_hand_str = input("0：グー　1：チョキ　2：パー 3：やめる" + "\n" + " > ")

    if user_hand_str == "3":
        break
    if user_hand_str not in ("0","1","2"):
        continue

    user_hand = int(user_hand_str)
    print("あなたは" + hands[user_hand] + "を出し、私は" + hands[pc_hand] + "\n")
    print("つまり結果はあなたの" + rules[(user_hand, pc_hand)])
