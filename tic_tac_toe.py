outer = 1
while outer != 0:
	board = [["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
	success_list = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
	legal_moves = [1,2,3,4,5,6,7,8,9]
	c = 1
	for i in range(5):
	    for j in range(5):
	    	if i%2 == 0 and j%2 == 0:
	    	    board[i][j] = " "
	    	    print(c,end = "")
	    	    c += 1
	    	elif i%2 == 0 and j%2 != 0:
	    	    board[i][j] = "|"
	    	    print(board[i][j],end = "")
	    	elif i%2 != 0 and j%2 == 0:
	    	    board[i][j] = "- "
	    	    print(board[i][j],end = "")
	    	elif i%2 != 0 and j%2 != 0:
	    	    board[i][j] = ""
	    	    print(board[i][j],end = "")
	    print()
	print("Board Structure...\nEnter the number in your desired position:")
	p1_c = [] 
	p2_c = []
	inner = 1
	while inner != 0:
		print("=========================")
		for i in range(5):
		    for j in range(5):
		        print(board[i][j],end = "")
		    print()
		print("=========================")
		print("player1:")
		
		while True:
			p1 = int(input(">"))
			if p1 not in legal_moves:
				print("Invalid Position...Try again:")
			elif p1 in legal_moves:
				legal_moves.remove(p1)
				break
    
		sym1 = "x"
		if p1 ==  1:
		    board[0][0] = sym1
		elif p1 == 2:
			board[0][2] = sym1
		elif p1 == 3:
			board[0][4] = sym1
		elif p1 ==  4:
		    board[2][0] = sym1
		elif p1 == 5:
			board[2][2] = sym1
		elif p1 == 6:
			board[2][4] = sym1
		elif p1 ==  7:
		    board[4][0] = sym1
		elif p1 == 8:
			board[4][2] = sym1
		elif p1 == 9:
			board[4][4] = sym1
		#some logic
		p1_c.append(p1)
		if(len(p1_c) >= 3):

			for i in range(8):
				f1 = 0
				for j in range(3):
					if(success_list[i][j] not in p1_c):
						f1 = 1
				if f1 == 0:
					print("=========================")
					for i in range(5):
					    for j in range(5):
					        print(board[i][j],end = "")
					    print()
					print("=========================")
					print("        ********Player1 is the Winner!!********")
					var = input("want to Start another Game? (yes/no)")
					if var.lower() == "yes":
						outer = 1
						inner = 0
						break
					elif var.lower() == "no":
						outer = 0
						inner = 0
						break
			if inner == 0:
				break
		print(len(p1_c)+len(p2_c))
		if (len(p1_c)+len(p2_c)) >= 9:
			print("=========================")
			for i in range(5):
			    for j in range(5):
			        print(board[i][j],end = "")
			    print()
			print("=========================")
			print("match draw!!")
			var = input("want to Start another Game? (yes/no)")
			if var.lower() == "yes":
				outer = 1
				inner = 0
				break
			elif var.lower() == "no":
				outer = 0
				inner = 0
				break




	    
		print("=========================")
		for i in range(5):
		    for j in range(5):
		        print(board[i][j],end = "")
		    print()
		print("=========================")
		print("player2:")
		while True:
			p2 = int(input(">"))
			if p2 not in legal_moves:
				print("Invalid Position...Try again:")
			elif p2 in legal_moves:
				legal_moves.remove(p2)
				break
		sym2 = "o"
		if p2 ==  1:
		    board[0][0] = sym2
		elif p2 == 2:
			board[0][2] = sym2
		elif p2 == 3:
			board[0][4] = sym2
		elif p2 ==  4:
		    board[2][0] = sym2
		elif p2 == 5:
			board[2][2] = sym2
		elif p2 == 6:
			board[2][4] = sym2
		elif p2 ==  7:
		    board[4][0] = sym2
		elif p2 == 8:
			board[4][2] = sym2
		elif p2 == 9:
			board[4][4] = sym2

		#some logic
		p2_c.append(p2)
		if(len(p2_c) >= 3):

			for i in range(8):
				f2 = 0
				for j in range(3):
					if(success_list[i][j] not in p2_c):
						f2 = 1
				if f2 == 0:
					print("=========================")
					for i in range(5):
					    for j in range(5):
					        print(board[i][j],end = "")
					    print()
					print("=========================")
					print("        ********Player2 is the Winner!!********")
					var = input("want to Start another Game? (yes/no)")
					if var.lower() == "yes":
						outer = 1
						inner = 0
						break
					elif var.lower() == "no":
						outer = 0
						inner = 0
						break
			if inner == 0:
				break
		print(len(p1_c)+len(p2_c))
		if (len(p1_c)+len(p2_c)) >= 9:
			print("=========================")
			for i in range(5):
			    for j in range(5):
			        print(board[i][j],end = "")
			    print()
			print("=========================")
			print("match draw!!")
			var = input("want to Start another Game? (yes/no)")
			if var.lower() == "yes":
				outer = 1
				inner = 0
				break
			elif var.lower() == "no":
				outer = 0
				inner = 0
				break
					
			
print("------------- Thanks for playing my game :) --------------")
