import itertools;
from colorama import Fore, Back, Style, init
init()


def win(game_map):
	def all_same(l):
		if l.count(l[0])== len(l)  and l[0] != 0 :
			return True
		else:
			return False		
	#horizontal
	for row in game_map:
		if all_same(row):
			print(f"Player {row[0]} winner horizontal!")
			return True

#Vertical
	for col in range(len(game_map)):
		check=[]

		for  row in game_map:
			check.append(row[col])

		if all_same(check):
			print(f"Player {check[0]} winner  vertical!")
			return True

#diagonal
	diags=[]
	for idx in range(len(game_map)):
		diags.append(game[idx][idx])

	if all_same(diags):
			print(f"Player {diags[0]} winner diagonal \\!")
			return True

	diags=[]
	for col,rows in enumerate(reversed(range(len(game_map)))):
		diags.append(game[rows][col])

	if all_same(diags):
			print(f"Player {diags[0]} winner diagonal /!")
			return True

def game_board (game_map, player = 0, row = 0, column = 0, just_display = False):
	try:
		if (game_map[row][column]!= 0):
			print("Position Occupied")
			return game_map, False
		#print("   0  1  2")
		#another way to write above print 
		s = "   "+"  ".join([str(i) for i in range(len(game_map))])
		print(s)
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			colored_row = ""
			for item in row:
				if item == 0:
					colored_row += "   "
				elif item ==1:
					colored_row += Fore.GREEN + ' X '  + Style.RESET_ALL
				elif item ==2:
					colored_row += Fore.YELLOW + ' 0 '  + Style.RESET_ALL
			print(count , colored_row)



		return game_map,True
	except IndexError as e:
		print("Error: make sure your row/column inpout in (0,1,2)",e)
		return game_map, False
	except Exception as e:
		print("ESomething went wrong!",e)
		return game_map, False


play = True
players = [1,2]
while play:
	game_size = int(input("What is size of your game?"))
	game = [[0 for i in range(game_size)] for i in range(game_size)]
	game_won = False;
	game, _ = game_board(game, just_display=True)
	player_Choice = (itertools.cycle([1,2]))
	played = False
	while not game_won:
		current_player = next(player_Choice)
		played = False
		while not played:
			column_choice = int(input("What column do you want to play? (0,1,2): "))
			row_choice = int(input("What row do you want to play? (0,1,2): "))
			game, played = game_board(game, current_player, row_choice, column_choice)

		if win(game):
			game_won = True
			again = input("the game is over, would you like to play again? (y/n)")
			if again.lower() == "y":
				print("restarting")
			elif again.lower()== "n":
				print("Byeeee")
				play = False
			else :
				print("False input")