
board = [["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
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

while True:
	print("=========================")
	for i in range(5):
	    for j in range(5):
	        print(board[i][j],end = "")
	    print()
	print("=========================")
	print("player1:")
	p1 = int(input(">"))
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

	print("=========================")
	for i in range(5):
	    for j in range(5):
	        print(board[i][j],end = "")
	    print()
	print("=========================")
	print("player2:")
	p2 = int(input(">"))
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
