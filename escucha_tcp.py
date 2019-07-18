from scapy.all import *

print("Escuchando durante 10 segundos")
res=sniff(filter="tcp port 80", timeout=10)
print('Sniffer recibio %d packet(s)' % len(res))
for pkt in res:
	if TCP in pkt:
		content = "\n".join(pkt.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
		stripped = re.sub('<[^<]+?>', '', content)	
		print(stripped)
