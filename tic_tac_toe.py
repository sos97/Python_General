for i in range(11):
    for j in range(11):
        if i!=0 and i%3!=0:
        	if j!=0 and j%3!=0:
        		print(" ", end = "")
        	elif j!=0:
        		print(".",end = "")
        	else:
        		print(" ", end = "")
        elif i!=0:
            print(".",end = "")
        else:
        	print(" ", end = "")
    print()
