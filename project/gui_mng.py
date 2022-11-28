import pygame
import os
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

        self.window.blit(self.green_piece, (100, 100))  # always draw after filling the screen
        self.window.blit(self.blue_piece, (300, 300))

        self.update_after_any_change()       # update after a change

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

            self.draw_window()  # update window and pieces' position

        # instead of quitting the game it is restarting by re-initiating!
        # pygame.quit()
        game = NewGame()
        game.run_game()

