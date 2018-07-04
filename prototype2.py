from pyai import *
"""実行ブロック
"""

def prompt(obj):
    """PyAIのプロンプトを作る関数
    　 戻り値　'PyAIオブジェクト名：応答オブジェクト名　＞　'
    """
    return obj.get_name() + ":" + obj.get_responder_name() + "> "

print("PyAI System prototype : pyai") # プログラムの情報を表示
pyai = PyAI("pyai")                   # PyAIオブジェクトを生成

while True:
    inputs = input(" > ")
    if not inputs:
        print("バイバイ")
        break
    response = pyai.dialogue(inputs) # 応答文字列を取得
    print(prompt(pyai), response)    # プロンプトと応答文字列をつなげて表示
    
