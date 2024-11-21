import socket
import threading

server_address = ('127.0.0.1', 9001)
stream_rate = 4096

username = input("ユーザー名を入力してください: ")
username_length = len(username)
username_header = username_length.to_bytes(1, "big")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive_messages():
    """サーバーからのメッセージを受信して表示"""
    while True:
        try:
            response, _ = client_socket.recvfrom(stream_rate)
            print(f"\n{response.decode()}")  # 入力行に影響しないように改行して表示
        except Exception as e:
            print(f"受信エラー: {e}")
            break

# サーバーからのメッセージ受信を別スレッドで実行
receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

print("チャットを開始します。終了するには 'exit' と入力してください。")

while True:
    try:
        message = input()
        if message.lower() == 'exit':
            break

        data = username_header + username.encode() + message.encode()
        client_socket.sendto(data, server_address)

    except Exception as e:
        print(f"送信エラー: {e}")
        break

client_socket.close()
