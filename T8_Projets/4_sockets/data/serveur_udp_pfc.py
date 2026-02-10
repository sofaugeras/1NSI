
import socket
import threading

PORT = 5000
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', PORT))
print("Serveur UDP lancé sur le port", PORT)

clients = {}
choices = {}

def handle_game():
    if len(choices) == 2:
        keys = list(choices.keys())
        joueur1, joueur2 = keys[0], keys[1]
        coup1, coup2 = choices[joueur1], choices[joueur2]

        def resultat(j1, j2):
            if j1 == j2:
                return "Égalité"
            elif (j1 == "pierre" and j2 == "ciseaux") or \
                 (j1 == "ciseaux" and j2 == "papier") or \
                 (j1 == "papier" and j2 == "pierre"):
                return "Joueur 1 gagne"
            else:
                return "Joueur 2 gagne"

        res = resultat(coup1, coup2)
        server.sendto(f"Résultat : {res} (J1: {coup1} / J2: {coup2})".encode(), joueur1)
        server.sendto(f"Résultat : {res} (J1: {coup1} / J2: {coup2})".encode(), joueur2)
        choices.clear()

def recevoir():
    while True:
        try:
            data, addr = server.recvfrom(BUFFER_SIZE)
            message = data.decode().strip().lower()

            if addr not in clients:
                clients[addr] = f"Joueur {len(clients)+1}"
                print(f"{clients[addr]} connecté depuis {addr}")

            if message in ["pierre", "papier", "ciseaux"]:
                choices[addr] = message
                server.sendto(f"Choix {message} reçu.".encode(), addr)
                handle_game()
            else:
                server.sendto("Choix invalide. Envoyez 'pierre', 'papier' ou 'ciseaux'.".encode(), addr)
        except Exception as e:
            print(f"Erreur : {e}")
            break

threading.Thread(target=recevoir, daemon=True).start()

print("Serveur prêt. Attente des joueurs...")
input("Appuyez sur Entrée pour quitter le serveur.\n")
