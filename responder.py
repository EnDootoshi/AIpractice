import prc.random_attack

class Responder:
    """応答クラスのスーパークラス
    """
    def __init__(self, name):
        """Responderオブジェクトの名前をnameに格納

           @param name Responderオブジェクトの名前
        """
        self.name = name

    def response(self, input):
        """オーバーライドを前提としたresponse()メゾット

           @param input 入力された文字列
           戻り値　空の文字列
        """
        return " "

    def get_name(self):
        """応答オブジェクトの名前を返す
        """
        return self.name


class RepeatResponder(Responder):
    """オウム返しのためのサブクラス
    """
    def response(self, input):
        """応答文字列を作って返す

           @param input 入力された文字列
        """
        return "{}ってなに？".format(input)


class RandomResponder(Responder):
    """ランダムな応答のためのサブクラス
    """
    def __init__(self, name):
        """Responderオブジェクトの名前を引数にして
           スーパークラスの__init__()を呼び出す
           ランダムに抽出するメッセージを格納したリストを作成

           @param name Respoderオブジェクトの名前
        """
        super().__init__(name)
        self.responses = ["つまり...どゆこと？", "そっかぁ", "なるほどだね"]

    def response(self, in@ut):
        """応答文字列を作って返す

        　 @param input 入力された文字列
           戻り値　リストからランダムに抽出した文字列
        """
        return (random.choice(self.responses))


        
