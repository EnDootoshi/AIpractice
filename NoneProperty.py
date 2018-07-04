class Michael:
    # パラメータmaxとcountのデフォルト値を設定
    def __init__(self, max = 5, count = 0 ):
        # 引数が渡されない場合はデフォルト値で変数を初期化
        # 引数が渡されたら引数の値で変数を初期化
        self.max = max
        self.count = count

    def teach(self):
        if self.count < self.max:
            print("もっと強く！")
        else:
            print("よーしオッケーだ！")
        self.count += 1

# Michaelオブジェクトを生成
oni = Michael()
# countの値を1にする
oni.count = 1

for i in range(5):
    print("ストローク")
    oni.teach()
    
