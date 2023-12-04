import pygame

FPS = 60


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 75

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        grid = [
            pygame.Rect(x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size)
            for x in
            range(self.width) for y in range(self.height)]
        [pygame.draw.rect(screen, (255, 255, 255), i, 1) for i in grid]

    def get_click(self, mouse_pos):
        self.on_click(self.get_cell(mouse_pos))
    def get_cell(self, mouse_pos):
        if (self.left < mouse_pos[0] < self.width * self.cell_size + self.left
                and self.top < mouse_pos[1] < self.height * self.cell_size + self.top):
            col = mouse_pos[0] // (self.cell_size + self.left)
            row = mouse_pos[1] // (self.cell_size + self.top)
            return col, row
        return None

    def on_click(self, cell_coords):
        print(cell_coords)



def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    board = Board(5, 7)
    board.set_view(100, 100, 50)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
