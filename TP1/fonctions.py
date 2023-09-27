def puissance (a,b):
	if not type(a) is int:
		raise TypeError ("only integers are allowed")
	if not type(b) is int:
                raise TypeError ("only integers are allowed")
	i=0
	puis=a
	if b==0 :
		puis =1
	elif a==0 and b<0 :
		raise TypeError ("Operation not supported")
	elif b<0 :
        	puis= 1/a**-b

	else :
		for i in range (1,b): 
			puis=puis*a
			i=i+1
	return puis
	print ("voici la valeur du 1er nombre élever à la puissance de la 2eme valeur: ",puis)


