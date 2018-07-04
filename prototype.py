class PyAI:
    # PyAIの本体クラス
    def __init__(self, name):
        """ PyAIオブジェクトの名前をnameに格納
            Responderオブジェクトを生成してresponderに格納

            @param name PyAIオブジェクトの名前
        """
        self.name = name
        self.responder = Responder("what")

    def dialogue(self, input):
        """ 応答オブジェクトのresponse()を呼び出して
            応答文字列を取得する

            @param input ユーザーによって入力された文字列
            戻り値 応答文字列
        """
        return self.responder.response(input)

    def get_responder_name(self):
        """ 応答オブジェクトの名前を返す
        """
        return self.responder.name

    def get_name(self):
        """ Ptnaオブジェクトの名前を返す
        """
        return self.name

class Responder:
    """ 応答クラス
    """
    def __init__(self, name):
        """ Responderオブジェクトの名前をnameに格納

            @param name Responderオブジェクトの名前
        """
        self.name = get_name

    def response(self, input):
        """ 応答文字列を作って返す

            @param input 入力された文字列
        """
        return "{}ってなに？".format(input)


##################################################################
#実行ブロック
##################################################################

def prompt(object):
    """ ピティナのプロンプトを作る関数
        戻り値 'Ptnaオブジェクト名:応答オブジェクト名 > '
    """
    return object.get_name() + ":" + object.get_responder_name() + "> "

print("PyAI System prototype : pyai") # プログラムの情報を表示
pyai = PyAI('pyai')                   # PyAIオブジェクトを生成

while True:
    inputs =input(" > ")
    if not inputs:
        print("バイバイ")
        break
    response = pyai.dialogue(inputs)   # 応答文字列を取得
    print(prompt(pyai), response)      # プロンプトと応答文字列をつなげて表示
