import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 9999))


def receive_messages():

    while True:

        try:
            message = client.recv(2048).decode()

            print(message)

        except:
            break


threading.Thread(target=receive_messages).start()


while True:

    message = input()

    client.send(message.encode())

    if message.lower() == "disconnect":
        break

client.close()