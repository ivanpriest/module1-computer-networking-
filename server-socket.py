import socket
import threading

HOST = "0.0.0.0"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("Chatroom server started...")

clients = []


def broadcast(message, sender_client):

    for client in clients:

        if client != sender_client:

            try:
                client.send(message)

            except:
                client.close()

                if client in clients:
                    clients.remove(client)


def handle_client(client):

    while True:

        try:

            message = client.recv(2048)

            if not message:
                break

            decoded = message.decode().strip()

            print(decoded)

            if decoded.lower() == "disconnect":

                client.send("Disconnected".encode())

                break

            broadcast(message, client)

        except:

            break

    print("Client disconnected")

    if client in clients:
        clients.remove(client)

    client.close()


while True:

    client, address = server.accept()

    print(f"Connection from {address} established")

    client.send("Welcome to the chatroom".encode())

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client,)
    )

    thread.start()