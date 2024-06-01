import pygame
import sys

# Initialize Pygame
pygame.init()

# Define the size of each cell and the grid
CELL_SIZE = 20
GRID_SIZE = 20
WINDOW_SIZE = CELL_SIZE * GRID_SIZE

# Define colors
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)
BLUE = (0, 0 , 200)

# Set up the display
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Purple Grid')

def draw_grid():
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        for y in range(0, WINDOW_SIZE, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, PURPLE, rect, 1)  # Draw the cell border

def main():
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(BLUE)  # Fill the background with black
        draw_grid()         # Draw the grid
        pygame.display.flip()
        clock.tick(30)      # Cap the frame rate at 30 FPS

if __name__ == "__main__":
    main()


