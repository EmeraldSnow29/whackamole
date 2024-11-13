import pygame
import random

'''Constants'''
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 512

GRID_COLS = 20
GRID_ROWS = 16

SQUARE_WIDTH = WINDOW_WIDTH / GRID_COLS
SQUARE_HEIGHT = WINDOW_HEIGHT / GRID_ROWS

'''Functions'''

def draw_grid(screen):
    """
    Draws the grid.
    :param screen: the screen to be drawn to
    """
    for x in range(GRID_ROWS):
        pygame.draw.line(screen, "black", (0, x * SQUARE_HEIGHT), (WINDOW_WIDTH, x * SQUARE_HEIGHT))
    for y in range(GRID_COLS):
        pygame.draw.line(screen, "black", (y * SQUARE_WIDTH, 0), (y * SQUARE_WIDTH, WINDOW_HEIGHT))

def get_world_pos(grid_pos):
    """
    Converts from grid coordinates to world coordinates
    :param grid_pos: (tuple) A position in grid coordinates
    :return: (tuple) the position in world coordinates
    """
    x, y = grid_pos
    new_x = x * SQUARE_WIDTH
    new_y = y * SQUARE_HEIGHT
    return new_x, new_y

def get_grid_pos(world_pos):
    """
    Converts from world coordinates to grid coordinates
    :param world_pos: (tuple) A position in world coordinates
    :return: (tuple) the position in grid coordinates
    """
    x, y = world_pos
    new_x = x // SQUARE_WIDTH
    new_y = y // SQUARE_HEIGHT
    return new_x, new_y

def get_random_position():
    """
    Generates a random position on the grid
    :return: (tuple) A random position in grid coordinates
    """
    return random.randrange(0, GRID_COLS), random.randrange(0, GRID_ROWS)

'''Main Program'''

def main():
    try:
        #Setup
        pygame.init()

        #load the mole and get a position for it.
        mole_grid_pos = get_random_position()
        mole_image = pygame.image.load("mole.png")

        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        clock = pygame.time.Clock()
        running = True

        while running:
            #events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #check if the two positions are the same
                    x, y = get_grid_pos(event.pos)
                    i, j = mole_grid_pos
                    if x == i and y == j:
                        #If they are, move the mole.
                        mole_grid_pos = get_random_position()

            #drawing
            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=get_world_pos(mole_grid_pos)))
            pygame.display.flip()

            #sets the game to 60fps
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
