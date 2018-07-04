class Miichael:
    def __init__(self, max = 5, count = 0):
        self.__max = max
        self.__count = count

    # __maxのゲッター
    def get_max(self):
        return self.__max

    # __countのゲッター
    def get_count(self):
        return self.__count

    # __maxのセッター
    def set_max(self, max):
        # self.__max = max
        if max < 5:
            self.__max = 5
        else:
            self.__max = max

    # __countのセッター
    def set_count(self, count):
        self.__count = count

    # maxのプロパティの定義
    max = property(get_max, set_max)

    # countのプロパティの定義
    count = property(get_count, set_count)

    def teach(self):
        if self.count < self.max:
            print(もっと強く！)
        else:
            print("よーしオッケーだ！")
        self.count += 1
