import pygame
import os
import gui_support
pygame.font.init()   # enable the fonts
pygame.mixer.init()  # enable sounds


class NewGame:
    WIDTH = 500
    HEIGHT = 500

    GREY_COLOR = (97, 97, 97)
    BLACK_COLOR = (0, 0, 0)
    RED_COLOR = (255, 0, 0)
    GREEN_COLOR = (200, 255, 0)
    BLUE_COLOR = (0, 0, 255)

    PIECES_LEFT_FONT = pygame.font.SysFont('arial', 30)
    WIN_GAME_FONT = pygame.font.SysFont('arial', 60)

    PLACE_SOUND = pygame.mixer.Sound(os.path.join('assets', 'hit_ball.mp3'))
    PLACE_SOUND.set_volume(0.2)   # lower volume
    ROW_SOUND = pygame.mixer.Sound(os.path.join('assets', 'goal.mp3'))
    WIN_GAME_SOUND = pygame.mixer.Sound(os.path.join('assets', 'win_sound.mp3'))

    FPS = 60

    PIECE_WIDTH = 23
    PIECE_HEIGHT = 23

    GREEN_PIECE_IMAGE = pygame.image.load(os.path.join('assets', 'green.png'))
    BLUE_PIECE_IMAGE = pygame.image.load(os.path.join('assets', 'blue.png'))
    BACKGROUND = pygame.image.load(os.path.join('assets', 'background.jpg'))

    BOARD = pygame.image.load(os.path.join('assets', 'board.png'))
    BUTTON_RADIUS = 20
    LINE_THICKNESS = 3
    BUTTON_X_POSITIONS = gui_support.BUTTON_X_POSITIONS
    BUTTON_Y_POSITIONS = gui_support.BUTTON_Y_POSITIONS

    RECTANGLE_LIST = []

    def __init__(self):
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("9 men morris")

        # transform images before display
        self.green_piece = pygame.transform.rotate(
            pygame.transform.scale(self.GREEN_PIECE_IMAGE, (self.PIECE_WIDTH, self.PIECE_HEIGHT)),
            10)
        self.blue_piece = pygame.transform.rotate(
            pygame.transform.scale(self.BLUE_PIECE_IMAGE, (self.PIECE_WIDTH, self.PIECE_HEIGHT)),
            -10)
        self.background = pygame.transform.scale(self.BACKGROUND, (self.WIDTH, self.HEIGHT))
        self.board = pygame.transform.scale(self.BOARD, (300, 300))

        self.pieces_left = 9

        # events 1-24
        self.event_list = []
        self.place_01_pressed = pygame.USEREVENT + 1
        self.event_list.append(self.place_01_pressed)
        self.place_02_pressed = pygame.USEREVENT + 2
        self.event_list.append(self.place_02_pressed)
        self.place_03_pressed = pygame.USEREVENT + 3
        self.event_list.append(self.place_03_pressed)
        self.place_04_pressed = pygame.USEREVENT + 4
        self.event_list.append(self.place_04_pressed)
        self.place_05_pressed = pygame.USEREVENT + 5
        self.event_list.append(self.place_05_pressed)
        self.place_06_pressed = pygame.USEREVENT + 6
        self.event_list.append(self.place_06_pressed)
        self.place_07_pressed = pygame.USEREVENT + 7
        self.event_list.append(self.place_07_pressed)
        self.place_08_pressed = pygame.USEREVENT + 8
        self.event_list.append(self.place_08_pressed)
        self.place_09_pressed = pygame.USEREVENT + 9
        self.event_list.append(self.place_09_pressed)
        self.place_10_pressed = pygame.USEREVENT + 10
        self.event_list.append(self.place_10_pressed)
        self.place_11_pressed = pygame.USEREVENT + 11
        self.event_list.append(self.place_11_pressed)
        self.place_12_pressed = pygame.USEREVENT + 12
        self.event_list.append(self.place_12_pressed)
        self.place_13_pressed = pygame.USEREVENT + 13
        self.event_list.append(self.place_13_pressed)
        self.place_14_pressed = pygame.USEREVENT + 14
        self.event_list.append(self.place_14_pressed)
        self.place_15_pressed = pygame.USEREVENT + 15
        self.event_list.append(self.place_15_pressed)
        self.place_16_pressed = pygame.USEREVENT + 16
        self.event_list.append(self.place_16_pressed)
        self.place_17_pressed = pygame.USEREVENT + 17
        self.event_list.append(self.place_17_pressed)
        self.place_18_pressed = pygame.USEREVENT + 18
        self.event_list.append(self.place_18_pressed)
        self.place_19_pressed = pygame.USEREVENT + 19
        self.event_list.append(self.place_19_pressed)
        self.place_20_pressed = pygame.USEREVENT + 20
        self.event_list.append(self.place_20_pressed)
        self.place_21_pressed = pygame.USEREVENT + 21
        self.event_list.append(self.place_21_pressed)
        self.place_22_pressed = pygame.USEREVENT + 22
        self.event_list.append(self.place_22_pressed)
        self.place_23_pressed = pygame.USEREVENT + 23
        self.event_list.append(self.place_23_pressed)
        self.place_24_pressed = pygame.USEREVENT + 24
        self.event_list.append(self.place_24_pressed)

    def draw_circles(self):
        # for i in range(len(self.BUTTON_X_POSITIONS)):
        #     pygame.draw.circle(
        #         self.window, self.BLACK_COLOR,
        #         (self.BUTTON_X_POSITIONS[i], self.BUTTON_Y_POSITIONS[i]),
        #         self.BUTTON_RADIUS, self.LINE_THICKNESS)
        self.RECTANGLE_LIST.clear()
        for i in range(len(self.BUTTON_X_POSITIONS)):
            rectangle = pygame.Rect(self.BUTTON_X_POSITIONS[i],
                                        self.BUTTON_Y_POSITIONS[i],
                                        20, 20)
            self.RECTANGLE_LIST.append(rectangle)
            pygame.draw.rect(self.window, self.GREY_COLOR, rectangle)

    @staticmethod
    def update_after_any_change():
        pygame.display.update()

    def draw_window(self):
        # self.window.fill(self.WINDOW_COLOR)  # RGB
        self.window.blit(self.background, (0, 0))

        green_pieces_left_text = self.PIECES_LEFT_FONT.render(
            'Tati: ' + str(self.pieces_left), True, self.GREEN_COLOR)  # render font
        blue_pieces_left_text = self.PIECES_LEFT_FONT.render(
            'Maxi: ' + str(self.pieces_left), True, self.BLUE_COLOR)  # render font
        self.window.blit(green_pieces_left_text, (10, 10))
        self.window.blit(blue_pieces_left_text, (self.WIDTH - blue_pieces_left_text.get_width()-10, 10))

        self.window.blit(self.board, (100, 100))

        self.draw_circles()

        self.window.blit(self.green_piece, (100, 100))  # always draw after filling the screen
        self.window.blit(self.blue_piece, (300, 300))

        self.update_after_any_change()       # update after a change

    # def draw_winner(self, text):
    #     draw_text = self.WINNER_FONT.render(text, True, self.WINDOW_COLOR2)
    #     self.window.blit(draw_text,
    #                      (self.WIDTH//2 - draw_text.get_width()//2,
    #                       self.HEIGHT//2 - draw_text.get_height()//2))
    #     self.update_after_any_change()  # update after a change
    #     pygame.time.delay(3000)

    # main loop
    def run_game(self):
        run = True
        while run:
            self.clock.tick(self.FPS)

            # exit condition
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()   # when we press the x it will actually close the game

                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     m_x, m_y = pygame.mouse.get_pos()
                #     print(m_x, m_y)
                #
                #     print(self.RECTANGLE_LIST)

                # movement
                # key_pressed = pygame.key.get_pressed()  # get pressed keys
                # self.movement(key_pressed)  # pass to movement method

                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    print(m_x, m_y)
                    for i in range(len(self.RECTANGLE_LIST)):
                        if self.RECTANGLE_LIST[i].collidepoint(m_x, m_y):
                            print(f"Rect: " + str(i))
                            pygame.event.post(pygame.event.Event(self.event_list[i+1]))

                if event.type == self.event_list[3]:
                    print("3333333")
                    self.PLACE_SOUND.play()

                    print(self.RECTANGLE_LIST)

            self.draw_window()  # update window and pieces' position

        # instead of quitting the game it is restarting by re-initiating!
        # pygame.quit()
        game = NewGame()
        game.run_game()

