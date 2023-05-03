import chess
import chess.pgn
import os

def read_game_from_file(file_path):
    with open(file_path, "r") as pgn_file:
        game = chess.pgn.read_game(pgn_file)
    return game

def navigate_game(game, index):
    board = game.board()
    moves = game.mainline_moves()

    for move_number, move in enumerate(moves):
        if move_number == index:
            break
        board.push(move)

    return board

def threatened_pieces(board):
    threatened = []
    king_square = None
    player_turn = board.turn

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None and piece.color == player_turn:
            if piece.piece_type == chess.KING:
                king_square = square
            elif board.is_attacked_by(not player_turn, square):
                threatened.append(square)

    if board.is_check():
        print("The king is in check at square", chess.square_name(king_square))

    return threatened

def main():
    file_path = input("Enter the path to the PGN file: ")
    game = read_game_from_file(file_path)
    index = 0

    while True:
        os.system('clear')
        board = navigate_game(game, index)
        print(board)

        command = input("Enter command (next, prev, play, undo, hint, or exit): ")

        if command.lower() == "next":
            index += 1
        elif command.lower() == "prev":
            index = max(0, index - 1)
        elif command.lower() == "play":
            # Switch to regular play mode
            pass
        elif command.lower() == "undo":
            undo_count = int(input("Enter the number of moves to undo: "))
            index = max(0, index - undo_count)
        elif command.lower() == "hint":
            threatened = threatened_pieces(board)
            print("Threatened pieces: ", [chess.square_name(sq) for sq in threatened])
            input("Press enter to continue...")
        elif command.lower() == "exit":
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
