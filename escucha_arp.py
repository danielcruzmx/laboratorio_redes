from scapy.all import *

print("Escuchando durante 10 segundos")
res=sniff(timeout=10)
print('Sniffer recibio %d packet(s)' % len(res))
res.show()
