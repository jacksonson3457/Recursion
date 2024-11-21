import socket
from pathlib import Path

# UDPで通信をします
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = '0.0.0.0'
server_port = 9001
stream_rate = 4096

# 次に、サーバは bind()関数を使用して、ソケットをサーバのアドレスとポートに紐付けします。その後、listen()関数を呼び出すことで、サーバは着信接続の待ち受けを開始します。サーバは一度に最大1つの接続を受け入れることができます。
sock.bind((server_address, server_port))

print("サーバーが起動しました...(UDPモード)")

# クライアントのアドレスを保存するリスト
clients = set()

while True:
    # その後、サーバは無限ループに入り、クライアントからの着信接続を継続的に受け付けます。このコードでは、accept()関数を使用して、着信接続を受け入れ、クライアントのアドレスを取得します。
    data, client_address = sock.recvfrom(stream_rate)
    # 新しいクライアントアドレスを保存
    if client_address not in clients:
        clients.add(client_address)
    
    print(clients)
    try:
        print('connection from', client_address)

        print(f"受信データ (バイナリ): {data}")


        # 取得したusername_lengthを使ってusernameを特定します
        username_length = int.from_bytes(data[:1], "big")
        username = data[1:1 + username_length].decode()
        message = data[1 + username_length:].decode()
        print(f"クライアント {client_address} ユーザー名: {username}")
        print(f"受信メッセージ: {message}")

        #応答を送信
        response = f"{username}: {message}".encode()

       # サーバーは例外が起きない限りはクローズせずに待ち続ける
       # すべてのクライアントに送信
        for client in clients:
            sock.sendto(response, client)

    except Exception as e:
        print('Error: ' + str(e))