- Para construir imagen 

$ docker build -t ubuntu_lab:latest .

- Para crear contenedores

$ python start_stop.py start

- Para parar contenedores

$ python start_stop.py 

- Probar practica
- abrir 4 ventanas

$ docker exec -it victima bash
$ docker exec -it atacante bash
$ docker exec -it atacante bash
$ docker exec -it server bash

- Arrancar Web Server 
- en ventana de server

# cd /home
# python webserver.py

- Arrancar en victima consulta a web server
- en ventana de victima

# cd /home
# ./viewpage.sh

- Envenenamiento y hack
- en ventana de atacante

# cd /home
# python poisoning.py <ip_victima> <ip_server>

- Vision del canal
- en otra ventana de atacante

# cd /home
# python escucha_arp.py

o

# python escucha_tcp.py


 



