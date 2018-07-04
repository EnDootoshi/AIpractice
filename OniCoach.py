class Michael:
    def __init__(self,max):
        self.max = max
        self.count = 0

    def teach(self):
        if self.count < self.max:
            print("もっと強く！")
        else:
            print("よーしオッケーだ！")
        self.count += 1


oni = Michael(6)
for i in range(8):
    if i % 2 ==0:
        print("フォア！")
    else:
        print("バック！")

    oni.teach()
