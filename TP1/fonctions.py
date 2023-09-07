def puissance (a,b):
	if not type(a) is int:
		raise TypeError ("only integers are allowed")
	if not type(b) is int:
                raise TypeError ("only integers are allowed")
	puis=a**b
	return puis
	print ("voici la valeur du 1er nombre élever à la puissance de la 2eme valeur: ",puis)


