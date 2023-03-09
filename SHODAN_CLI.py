#!/usr/bin/env python
#_*_ coding: utf8 _*_

from shodan import Shodan
import argparse
import sys
reload(sys)
sys.setdefaultencoding('utf8')

parser = argparse.ArgumentParser()
#parser.add_argument('-b', '--buscar', help="Opción a buscar.")
parser.add_argument('-q', '--query', help="Busqueda")
parser = parser.parse_args()



def main():

	key="0PLbljqJzFB5plYsvXyVQjDdKBu94MSs"
	if parser.query:
    
		api = Shodan(key)
		try:
			b = api.search(parser.query)
			print("Total de objetivos {}".format(b['total']))#Key: total contiene todos los resultados
			#print("Imprimimos matches: {}".format(b['matches']))
			for i in b['matches']:#Key matches contiene toda la informacion obtenida
				print('Target encontrado: {}'.format(i['ip_str']))
				print('Puertos abiertos: {}'.format(i['port']))
		except:
			print('Error en la consulta')
	else:
		print('Introduce una consulta con -q')


	
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
