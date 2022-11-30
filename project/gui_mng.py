import pygame
import os
import gui_support
import time
pygame.font.init()   # enable the fonts
pygame.mixer.init()  # enable sounds


class NewGui:
    WIDTH = 500
    HEIGHT = 500

    GREY_COLOR = (97, 97, 97)
    BLACK_COLOR = (0, 0, 0)
    RED_COLOR = (255, 0, 0)
    GREEN_COLOR = (200, 255, 0)
    BLUE_COLOR = (0, 0, 255)

    PIECES_LEFT_FONT = pygame.font.SysFont('arial', 30)
    WIN_GAME_FONT = pygame.font.SysFont('arial', 30)

    PLACE_SOUND = pygame.mixer.Sound(os.path.join('assets', 'hit_ball.mp3'))
    PLACE_SOUND.set_volume(0.2)   # lower volume
    ROW_SOUND = pygame.mixer.Sound(os.path.join('assets', 'goal.mp3'))
    WIN_GAME_SOUND = pygame.mixer.Sound(os.path.join('assets', 'win_sound.mp3'))

    FPS = 60

    GAME_PIECES = 9

    PIECE_WIDTH = 23
    PIECE_HEIGHT = 23

    GREEN_PIECE_IMAGE = pygame.image.load(os.path.join('assets', 'green.png'))
    BLUE_PIECE_IMAGE = pygame.image.load(os.path.join('assets', 'blue.png'))
    BACKGROUND = pygame.image.load(os.path.join('assets', 'background.jpg'))

    BOARD = pygame.image.load(os.path.join('assets', 'board.png'))
    BUTTON_X_POSITIONS = gui_support.BUTTON_X_POSITIONS
    BUTTON_Y_POSITIONS = gui_support.BUTTON_Y_POSITIONS

    EVENT_LIST = []
    RECTANGLE_LIST = []

    def __init__(self):
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("9 men morris")

        # rounds for phase 1 (placement phase)
        self.rounds_left_in_phase1 = 9

        # transform images before display
        self.green_piece = pygame.transform.rotate(
            pygame.transform.scale(self.GREEN_PIECE_IMAGE, (self.PIECE_WIDTH, self.PIECE_HEIGHT)),
            10)
        self.blue_piece = pygame.transform.rotate(
            pygame.transform.scale(self.BLUE_PIECE_IMAGE, (self.PIECE_WIDTH, self.PIECE_HEIGHT)),
            -10)
        self.background = pygame.transform.scale(self.BACKGROUND, (self.WIDTH, self.HEIGHT))
        self.board = pygame.transform.scale(self.BOARD, (300, 300))

        # events 1-24
        self.create_events()

        # player_placements
        self.player_1_placements = []
        self.player_2_placements = []

        self.player_1_pieces_left = 9
        self.player_2_pieces_left = 9

        self.current_player = 1

    def create_events(self):
        self.place_01_pressed = pygame.USEREVENT + 1
        self.EVENT_LIST.append(self.place_01_pressed)
        self.place_02_pressed = pygame.USEREVENT + 2
        self.EVENT_LIST.append(self.place_02_pressed)
        self.place_03_pressed = pygame.USEREVENT + 3
        self.EVENT_LIST.append(self.place_03_pressed)
        self.place_04_pressed = pygame.USEREVENT + 4
        self.EVENT_LIST.append(self.place_04_pressed)
        self.place_05_pressed = pygame.USEREVENT + 5
        self.EVENT_LIST.append(self.place_05_pressed)
        self.place_06_pressed = pygame.USEREVENT + 6
        self.EVENT_LIST.append(self.place_06_pressed)
        self.place_07_pressed = pygame.USEREVENT + 7
        self.EVENT_LIST.append(self.place_07_pressed)
        self.place_08_pressed = pygame.USEREVENT + 8
        self.EVENT_LIST.append(self.place_08_pressed)
        self.place_09_pressed = pygame.USEREVENT + 9
        self.EVENT_LIST.append(self.place_09_pressed)
        self.place_10_pressed = pygame.USEREVENT + 10
        self.EVENT_LIST.append(self.place_10_pressed)
        self.place_11_pressed = pygame.USEREVENT + 11
        self.EVENT_LIST.append(self.place_11_pressed)
        self.place_12_pressed = pygame.USEREVENT + 12
        self.EVENT_LIST.append(self.place_12_pressed)
        self.place_13_pressed = pygame.USEREVENT + 13
        self.EVENT_LIST.append(self.place_13_pressed)
        self.place_14_pressed = pygame.USEREVENT + 14
        self.EVENT_LIST.append(self.place_14_pressed)
        self.place_15_pressed = pygame.USEREVENT + 15
        self.EVENT_LIST.append(self.place_15_pressed)
        self.place_16_pressed = pygame.USEREVENT + 16
        self.EVENT_LIST.append(self.place_16_pressed)
        self.place_17_pressed = pygame.USEREVENT + 17
        self.EVENT_LIST.append(self.place_17_pressed)
        self.place_18_pressed = pygame.USEREVENT + 18
        self.EVENT_LIST.append(self.place_18_pressed)
        self.place_19_pressed = pygame.USEREVENT + 19
        self.EVENT_LIST.append(self.place_19_pressed)
        self.place_20_pressed = pygame.USEREVENT + 20
        self.EVENT_LIST.append(self.place_20_pressed)
        self.place_21_pressed = pygame.USEREVENT + 21
        self.EVENT_LIST.append(self.place_21_pressed)
        self.place_22_pressed = pygame.USEREVENT + 22
        self.EVENT_LIST.append(self.place_22_pressed)
        self.place_23_pressed = pygame.USEREVENT + 23
        self.EVENT_LIST.append(self.place_23_pressed)
        self.place_24_pressed = pygame.USEREVENT + 24
        self.EVENT_LIST.append(self.place_24_pressed)

    def draw_rectangles(self):
        self.RECTANGLE_LIST.clear()
        for i in range(len(self.BUTTON_X_POSITIONS)):
            current_rectangle = pygame.Rect(self.BUTTON_X_POSITIONS[i]-10, self.BUTTON_Y_POSITIONS[i]-10, 20, 20)
            self.RECTANGLE_LIST.append(current_rectangle)
            pygame.draw.rect(self.window, self.GREY_COLOR, current_rectangle)

    @staticmethod
    def update_after_any_change():
        pygame.display.update()

    def rotate_players(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def draw_window(self, message=None):
        self.window.blit(self.background, (0, 0))

        # 1. pieces left
        text_p1 = self.PIECES_LEFT_FONT.render('Tati: ' + str(self.player_1_pieces_left), True, self.GREEN_COLOR)
        text_p2 = self.PIECES_LEFT_FONT.render('Maxi: ' + str(self.player_2_pieces_left), True, self.BLUE_COLOR)
        self.window.blit(text_p1, (10, 10))
        self.window.blit(text_p2, (self.WIDTH - text_p2.get_width()-10, 10))

        # 2. board
        self.window.blit(self.board, (100, 100))

        # 3. rectangles
        self.draw_rectangles()

        # 4. pieces
        self.window.blit(self.green_piece, (100, 100))  # always draw after filling the screen
        self.window.blit(self.blue_piece, (300, 300))

        # 5. custom message
        text_to_display = self.WIN_GAME_FONT.render(message, True, self.BLACK_COLOR)
        self.window.blit(text_to_display,
                         (self.WIDTH//2 - text_to_display.get_width()//2,
                          self.HEIGHT//2 - text_to_display.get_height()//2 + 200))

        self.update_after_any_change()       # update after a change

    # main loop
    def run_game(self):
        run = True
        while run:

# 1
# -----------------------------------------------------------------------------------------#
            self.clock.tick(self.FPS)
            message = f'Player {self.current_player}: Select Place'

# 2
# -----------------------------------------------------------------------------------------#
            for event in pygame.event.get():
                # 0. exit condition
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()   # when we press the x it will actually close the game

                # 1. read clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    # print(m_x, m_y)
                    for idx in range(len(self.RECTANGLE_LIST)):
                        if self.RECTANGLE_LIST[idx].collidepoint(m_x, m_y):
                            # print(f"Rect: {str(idx+1)}", end=', ')
                            # pygame.event.post(pygame.event.Event(self.EVENT_LIST[idx]))
                            # print(f"Event posted: {str(idx + 1)}")

                            if self.current_player == 1:
                                if (idx not in self.player_1_placements) and (idx not in self.player_2_placements):
                                    self.player_1_placements.append(idx)
                                    print(f"Placed for Player {self.current_player} on square {idx+1}")
                                    print(*self.player_1_placements, sep=', ')
                                    self.rotate_players()
                                else:
                                    print(f"Square {idx+1} is occupied. Try again")

                            if self.current_player == 2:
                                if (idx not in self.player_1_placements) and (idx not in self.player_2_placements):
                                    self.player_2_placements.append(idx)
                                    print(f"Placed for Player {self.current_player} on square {idx+1}")
                                    print(*self.player_2_placements, sep=', ')
                                    self.rotate_players()
                                else:
                                    print(f"Square {idx+1} is occupied. Try again")



                # 2. control event nr 4
                # if event.type == self.place_04_pressed:
                #     text = "Control"
                #     print(text)
                #     self.PLACE_SOUND.play()

# 3
# -----------------------------------------------------------------------------------------#

            # 3. draws
            self.draw_window(message)  # update window and pieces' position

# -----------------------------------------------------------------------------------------#

        game = NewGui()    # instead of quitting the game it is restarting by re-initiating!
        game.run_game()

