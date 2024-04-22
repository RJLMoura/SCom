
def place_ship(board, ship, x, y, orientation):
    size = ship
    if orientation == 0:  # Horizontal
        for i in range(size):
            board[y][x + i] = 1
    else:  # Vertical
        for i in range(size):
            board[y + i][x] = 1

def display_board(board):
    print("   0 1 2 3 4 5 6 7 8 9 ")
    for i in range(len(board)):
        print(f"{i:2}", end=" ")
        for j in range(len(board[i])):
            if board[i][j] == 0:
                print(". ", end="")
            elif board[i][j] == 1:
                print("O ", end="")
            elif board[i][j] == 2:
                print("X ", end="")
            else:
                print("W ", end="")
        print()

def take_turn(player, board, hit_counter):
    print(f"Player {player}, it's your turn.")
    coord = input("Enter coordinates (X,Y): ")
    x, y = map(int, coord.split(','))
    if board[y][x] == 1:
        print("Hit!")
        board[y][x] = 2
        hit_counter[player] += 1
    elif board[y][x] == 0:
        print("Miss.")
        board[y][x] = 3
    else:
        print("You've already hit there!")

def play_game():
    board_size = 10       # Coordinates, 0-9 square board
    total_hits_needed = 2 # 2*1 + 2*2 + 3 + 4 + 5 == 28
    hit_counter = [0, 0]  # Tracks the number of hits for each player
    current_player = 0    # First player (0 or 1)

    ships = [("Carrier", 5), 
             ("Battleship", 4), 
             ("Destroyer", 3), 
             ("Cruiser A", 2), 
             ("Cruiser B", 2), 
             ("Submarine A", 1), 
             ("Submarine B", 1)
            ]
    
    player1_board = [[0] * board_size for _ in range(board_size)]
    player2_board = [[0] * board_size for _ in range(board_size)]

    print("Welcome to Battleship!")

    print("Player 1, place your ships:")
    display_board(player1_board)

    for ship_name, ship_size in ships:
        print(f"Place your {ship_name} ({ship_size} squares):")
        coord = input("Enter coordinates (X,Y,O): ")
        x, y, o = map(int, coord.split(','))
        place_ship(player1_board, ship_size, x, y, o)
        display_board(player1_board)
    
    input("Press Enter to continue...")
    print("\n" * 100)  # Clear the screen
    
    print("Player 2, place your ships:")
    place_ship(player2_board, 5, 3, 0, 0)  
    place_ship(player2_board, 4, 3, 1, 0)
    place_ship(player2_board, 3, 3, 2, 0)
    place_ship(player2_board, 2, 3, 3, 0)
    place_ship(player2_board, 2, 3, 4, 0)
    place_ship(player2_board, 1, 3, 5, 0)
    place_ship(player2_board, 1, 3, 6, 0)
    display_board(player2_board)
    
    input("Press Enter to start the game...")
    print("\n" * 100)  # Clear the screen
    
    while True:
        if current_player == 0:
            take_turn(0, player2_board, hit_counter)
            if hit_counter[0] == total_hits_needed:
                print("Player 1 wins!")
                break
            current_player = 1
        else:
            take_turn(1, player1_board, hit_counter)
            if hit_counter[1] == total_hits_needed:
                print("Player 2 wins!")
                break
            current_player = 0

if __name__ == "__main__":
    play_game()
