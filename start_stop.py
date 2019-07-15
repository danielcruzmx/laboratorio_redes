from infraestructura import contenedor, red

import os
import time
import sys

def __main__():

    parent_dir = os.path.dirname(os.path.realpath(__file__))
    
    if len(sys.argv) == 2: 
      accion = sys.argv[1]
    else:
      accion = ''
    
    net = red(
    {
      'name'  : 'lab_net',
      'driver': 'bridge'
    })
     
    INFRAESTRUCTURA = \
        [{'image': 'ubuntunet',
          'name': 'victima',
          'ports': {'6000/tcp': 6000},
          'links': {},
          'entrypoint': '/bin/bash',
          'environment': [],
          'cap_add': ['NET_ADMIN'],
          'network': net.get_nombre(),
          'mac_address': '00:00:00:00:00:01',
          'volumes': {parent_dir: {'bind': '/home', 'mode': 'rw'}}               
          },
          {'image': 'ubuntunet',
          'name': 'atacante',
          'ports': {'6000/tcp': 6001},
          'links': {},
          'entrypoint': '/bin/bash',
          'environment': [],
          'cap_add': ['NET_ADMIN'],
          'network': net.get_nombre(),
          'mac_address': '00:00:00:00:00:02',
          'volumes': {parent_dir: {'bind': '/home', 'mode': 'rw'}}               
          },
          {'image': 'ubuntunet',
          'name': 'server',
          'ports': {'6000/tcp': 6002},
          'links': {},
          'entrypoint': '/bin/bash',
          'environment': [],
          'cap_add': ['NET_ADMIN'],
          'network': net.get_nombre(),
          'mac_address': '00:00:00:00:00:03',
          'volumes': {parent_dir: {'bind': '/home', 'mode': 'rw'}}               
          }
         ]

    for n in INFRAESTRUCTURA:
      ctr = contenedor(n)
      ## para y remueve si es que existe remanente 
      ctr.stop()
      ctr.remove()
      
      if accion.upper() == 'START':
        ## vuelve a crear   
        ctr.create()
   
        while True:
          edo = ctr.status()
          if edo == 'CREATED':
            ctr.start()
          elif edo == 'RUNNING':
            break
      
        r = ctr.execute('ifconfig','/home')
        ip = r[1][r[1].find('inet') + 4 : r[1].find('inet') + 16]
        mac = r[1][r[1].find('ether') + 5 : r[1].find('ether') + 23]
        print n['name'], ip, mac
    
__main__()
