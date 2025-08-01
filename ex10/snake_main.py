import game_parameters
from game_display import GameDisplay
from bomb import Bomb
from board import Board
from snake import Snake
from apple import Apple


def main_loop(gd: GameDisplay) -> None:
    board = Board(game_parameters.WIDTH, game_parameters.HEIGHT)
    bomb = Bomb()
    snake = Snake()
    gd.show_score(board.get_score())
    for i in range(3):
        add_apple_to_board(board)
    board.add_snake(snake)
    board.add_bomb(bomb, 0)
    draw_board(board, gd)
    gd.end_round()
    default_key_clicked = "Up"
    temp_radius = 0
    timer = 1
    while True:
        head = snake.move_requirements(default_key_clicked)
        if head in snake.get_coordinates():
            board.move_snake(default_key_clicked)
            draw_board(board, gd)
            gd.end_round()
            return
        board.move_snake(default_key_clicked)
        if timer >= bomb.get_time():
            board.delete_bomb(bomb, temp_radius)
            if temp_radius == 0 and bomb.get_color() == "red":
                temp_radius = 0
                bomb.update_color()
            elif temp_radius <= bomb.get_radius():
                temp_radius += 1
                bomb.update_color()
            else:
                bomb.update_color()
                temp_radius = 0
                timer = 0
                bomb = Bomb()
        board.add_bomb(bomb, temp_radius)
        x, y = snake.move_requirements(default_key_clicked)
        if not 0 <= x < game_parameters.WIDTH or not 0 <= y < game_parameters.HEIGHT:
            draw_board(board, gd)
            gd.end_round()
            return
        if snake.meet_bomb(bomb.update_orange_list(temp_radius)):
            draw_board(board, gd)
            gd.end_round()
            return
        if board.is_apple((x, y)):
            board.update_board_apples((x, y))
            gd.show_score(board.get_score())
            add_apple_to_board(board)
        draw_board(board, gd)
        gd.end_round()
        timer += 1
        key_clicked = gd.get_key_clicked()
        if key_clicked:
            if (key_clicked == 'Left') and (default_key_clicked != "Right"):
                default_key_clicked = "Left"
            elif (key_clicked == 'Right') and (default_key_clicked != "Left"):
                default_key_clicked = "Right"
            elif key_clicked == "Up" and default_key_clicked != "Down":
                default_key_clicked = "Up"
            elif key_clicked == "Down" and default_key_clicked != "Up":
                default_key_clicked = "Down"


def draw_bomb(bomb, r, gd):
    for coord in bomb.update_orange_list(r):
        gd.draw_cell(coord[0], coord[1], bomb.get_color())


def draw_board(board, gd):
    b = board.get_board()
    # snake_coordinates = board.get_snake_coordinates()
    # apple_coordinates = board.get_apples_coordinates()
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] is not None:
                gd.draw_cell(i, j, b[i][j])
    #
    # for coord in snake_coordinates:
    #     gd.draw_cell(coord[0], coord[1], "Black")
    # for coord in apple_coordinates:
    #     gd.draw_cell(coord[0], coord[1], "Green")


def add_apple_to_board(board):
    apple_data = game_parameters.get_random_apple_data()
    apple = Apple((apple_data[0], apple_data[1]), apple_data[2])
    while not board.add_apple(apple):
        apple_data = game_parameters.get_random_apple_data()
        apple = Apple((apple_data[0], apple_data[1]), apple_data[2])
    board.add_apple(apple)

# if __name__ == '__main__':
#     gd = GameDisplay()
#     gd.start()
#     # main_loop(gd)
