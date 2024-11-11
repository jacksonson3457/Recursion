import math
import socket
import json
import os

def floor(x):
    return math.floor(x)

def nroot(n, x):
    return math.floor(x ** (1 / n))

def reverse(s):
    return s[::-1]

def validAnagram(str1, str2):
    return sorted(str1) == sorted(str2)

def sort(strArr):
    return sorted(strArr)

functions = {
    'floor': floor,
    'nroot': nroot,
    'reverse': reverse,
    'validAnagram': validAnagram,
    'sort': sort
}

def connection():
    # ソケットを設定
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_address = '/tmp/socket_file'

    # 古いソケットファイルがあれば削除
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    server.bind(server_address)
    server.listen(1)

    print('Server listening on', server_address)

    while True:
        connection, _ = server.accept()
        try:
            data = connection.recv(1024)
            if not data:
                continue

            # リクエストをパース
            request = json.loads(data.decode('utf-8'))
            method = request.get('method')
            params = request.get('params')

            # メソッドの呼び出し
            result = executeMethod(functions[method],params)
            response = {
                    "jsonrpc": "2.0",
                    "result": result,
                    "id": request.get("id")
                }

            # レスポンスを送信
            connection.sendall(json.dumps(response).encode('utf-8'))
            print('Sent result: ' + str(result))
        finally:
            connection.close()

def executeMethod(func, params):
    if isinstance(params, list):
        return func(*params)
    return func(params)


# main 関数の定義
def main():
    print("Starting the server...")
    connection()

# エントリーポイント
if __name__ == "__main__":
    main()
