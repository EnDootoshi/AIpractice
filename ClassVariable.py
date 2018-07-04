class Michael:
    count = 0
    max =5

    def teach(self):
        if self.__class__.count < self.__class__.max:
            print("もっと強く！")
        else:
            print("よーしオッケーだ！")
        self.__class__.count += 1

oni1 = Michael()
for i in range(3):
    print("フォアハンド！")
    oni1.teach()

oni2 = Michael()
for i in range(4):
    print("ボレー！")
    oni2.teach()
    
