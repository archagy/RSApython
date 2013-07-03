from math import sqrt
from random import randint
num_iniciar=int(raw_input("Define el rango aleatorio valor 1: "))
num_iniciar2=int(raw_input("Define el rango aleatorio valor 2: "))
user=raw_input("Nombre de usuario:")
def comprueba_primo(numero_primo):
	if all(numero_primo%i!=0 for i in range(2,int(sqrt(numero_primo))+1)):
		return False
	return True
	
def generadornumeros():
	while True:
		numero_primo=randint(num_iniciar,num_iniciar2)
		if comprueba_primo(numero_primo):
			return numero_primo
	
def regla(phi,e):
    if phi%e ==0:
        return e
    else:
        return regla(e, phi%e)

def	obtener_e(phi):
    e=generadornumeros()
    if(regla(phi, e)==1):
        return e
    else:
        obtener_e(phi)

def egcd(e, phi):
	c=e%phi
	if c==0:
		return (phi,0,1)
	(r,x,y) = egcd(phi,c)
	return (r,y,x-y*(e/phi))

def inversa(e, n):
	(gcd,tmp,d) = egcd(e, n)
	if not gcd == 1:
		return None
	else:
		return (tmp+n) %n
		
def generador_llaves(user,d,e,n):
    naviserver= str(user)+" "+str(d) +" "+str(e)+ "\n"
    txt=open("naviserver.txt","a")
    txt.write(naviserver)
    txt.close
    usuario= str(user)+ ".txt"
    txt2=open(usuario,"a")
    usr= str(user)+" "+str(d) +" "+str(n)
    txt2.write(usr)
    txt2.close
def main():
	
	while True:		
		num_iniciar
		num_iniciar2
		if num_iniciar >=num_iniciar2:
			print "El primer numero no puede ser menor al segundo, intente de nuevo"
			return False	
		else:
			p=generadornumeros()
			q = generadornumeros()
			phi = (p-1)*(q-1)
			n=p*q 
			e=obtener_e(phi)			
			while True:
				if e==None:
					e=obtener_e(phi)
					print e
				else:
					return False
			generador_llaves(user,d,e,n)
			return False
			
		
	
			
main()