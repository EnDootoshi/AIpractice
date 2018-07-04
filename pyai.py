from responder import *
class PyAI:
    """PyAIの本体クラス
    """
    def __init__(self, name):
        """PyAIオブジェクトの名前をnameに格納
           RandomResponderオブジェクトを生成してresponderに格納

           @param name PyAIオブジェクトの名前
        """
        self.name = name
        self.responder = RandomResponder("Random")

    def dialogue(self, input):
        """応答オブジェクトのresponse()を呼び出して
           応答文字列を取得する

           @param input ユーザーによって入力された文字列
           戻り値　応答文字列
        """
        return slef.responder.response(input)

    def get_responder_name(self):
        """応答オブジェクトの名前を返す
        """
        return self.responder.name

    def get_name(self):
        """PyAIオブジェクトの名前を返す
        """
        return self.name
        
