import os
import sys
import serial,time
from string import Template

#abriendo achivo
filein = open('/var/www/html/plantilla.html')
#leyendo archivo
src = Template(filein.read())

def mates():
	global b
	b='caca'
	return b
c = mates()
print(c)

#def cridallum():
#	n=0
#	global g
#	arduino=serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=3.0)
#	arduino.close()
#	arduino.open()
#	time.sleep(2)
#	var="D"
#	varb=var.encode('utf-8')
#	arduino.write(varb)
#	time.sleep(0.1)
#	n=n+1
#	while arduino.inWaiting() > 0:	
	#while n==1:
#		dist = arduino.read(1)
#		distd=dist.decode('utf-8')
			#s'ha de declarar com a global la variable, dintre 
			#de la mateixa estructura en la qual s'asigna un valor
				#char_llum=str(dist_d)	
#		print(distd)			
#		g=distd
#		n=n+1
			
#	return 12


temperatura = "temp" #input("ingresa temperatura")
llum = "1111"#cridallum()
#print(llum)
humitat = "humit"#input("ingrese humitat: ")
presencia = "vvvvv" #input("presencia ")

#######os.remove('/var/www/html/perfil/1999.html')
d = { 'temperatura':temperatura, 'llum':llum, 'humitat':humitat, 'presencia':presencia}
result = src.substitute(d)
os.remove('/var/www/html/index.html')
#os.substitute('/var/www/html/perfil/1999.html')


try:
	os.mkdir("/var/www/html")
	filein2 = open('html/'+'index'+'.html','a')
	filein2.writelines(result)
	
except OSError:
	if os.path.exists('/var/www/html'):

		filein2 = open('/var/www/html/'+'index'+'.html','a')
		filein2.writelines(result)

sys.exit()
####################################










        
