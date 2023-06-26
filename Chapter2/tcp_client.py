import socket

targetHost = '0.0.0.0'
targetPort = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((targetHost,targetPort))

client.send(input().encode())

response = client.recv(4096)

print(response)
client.close()