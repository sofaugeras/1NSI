
import socket
import threading

SERVER_IP = 'IP_DU_SERVEUR'  # À modifier
SERVER_PORT = 5000
BUFFER_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def recevoir():
    while True:
        try:
            data, addr = client.recvfrom(BUFFER_SIZE)
            print(f"\n[Serveur] : {data.decode()}")
        except:
            break

threading.Thread(target=recevoir, daemon=True).start()

print("Jeu Pierre-Feuille-Ciseaux UDP. Tape ton choix : 'pierre', 'papier', ou 'ciseaux'. 'exit' pour quitter.")
while True:
    msg = input(">> ")
    if msg.lower() == 'exit':
        break
    client.sendto(msg.encode(), (SERVER_IP, SERVER_PORT))
