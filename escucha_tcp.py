from scapy.all import *

res=sniff(filter="tcp port 80")
for pkt in res:
	if TCP in pkt:
		print "\n".join(pkt.sprintf("{Raw:%Raw. load%}\n").split(r"\r\n"))
