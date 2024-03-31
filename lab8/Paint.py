import pygame

WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class GameObject:
    def draw(self):
        raise NotImplementedError

    def handle(self):
        raise NotImplementedError


class Button:
    def __init__(self):
        self.rect0 = pygame.draw.rect(
            SCREEN,
            WHITE,
            (WIDTH // 2, 20, 40, 40)
        )
        self.rect = pygame.draw.rect(
            SCREEN,
            WHITE,
            (WIDTH // 2 - 20, 20, 40, 40)
        )

    def draw(self):
        self.rect0 = pygame.draw.rect(
            SCREEN,
            WHITE,
            (WIDTH // 2 + 50, 20, 40, 40)
        )
        self.rect = pygame.draw.rect(
            SCREEN,
            WHITE,
            (WIDTH // 2, 20, 40, 40)
        )


class Pen(GameObject):
    def __init__(self, color=WHITE, width=5):
        self.points = []
        self.color = color
        self.width = width

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):
            pygame.draw.line(
                SCREEN,
                self.color,
                start_pos=point,
                end_pos=self.points[idx + 1],
                width=self.width,
            )

    def handle(self, mouse_pos):
        self.points.append(mouse_pos)


class Eraser(Pen):
    def __init__(self):
        super().__init__(color=BLACK, width=20)  # Use black color and wider width as an eraser


class Rectangle(GameObject):
    def __init__(self, start_pos, color=WHITE):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.rect(
            SCREEN,
            self.color,
            (
                start_pos_x,
                start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos


class Square(GameObject):
    def __init__(self, start_pos, color=WHITE):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        square_size = min(end_pos_x - start_pos_x, end_pos_y - start_pos_y)

        square_start_pos_x = start_pos_x + (end_pos_x - start_pos_x - square_size) // 2
        square_start_pos_y = start_pos_y + (end_pos_y - start_pos_y - square_size) // 2

        pygame.draw.rect(
            SCREEN,
            self.color,
            (
                square_start_pos_x,
                square_start_pos_y,
                square_size,
                square_size
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos


class Circle(GameObject):
    def __init__(self, start_pos, color=WHITE):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color

    def draw(self):
        radius = ((self.end_pos[0] - self.start_pos[0])**2 + (self.end_pos[1] - self.start_pos[1])**2)**0.5
        pygame.draw.circle(
            SCREEN,
            self.color,
            self.start_pos,
            int(radius),
            width=5
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos


def main():
    running = True
    active_obj = None
    button = Button()
    objects = [button]
    clock = pygame.time.Clock()
    current_shape = 'pen'
    current_color = WHITE

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'rectangle'
                elif button.rect0.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'pen'
                elif event.button == 2:  # Middle mouse button for eraser
                    current_shape = 'eraser'
                else:
                    if current_shape == 'pen':
                        if current_color == WHITE:
                            active_obj = Pen(color=BLACK)
                        else:
                            active_obj = Pen(color=current_color)
                    elif current_shape == 'rectangle':
                        active_obj = Rectangle(start_pos=event.pos, color=current_color)
                    elif current_shape == 'square':
                        active_obj = Square(start_pos=event.pos, color=current_color)
                    elif current_shape == 'circle':
                        active_obj = Circle(start_pos=event.pos, color=current_color)
                    elif current_shape == 'eraser':
                        active_obj = Eraser()

            if event.type == pygame.MOUSEMOTION and active_obj is not None:
                active_obj.handle(mouse_pos=pygame.mouse.get_pos())
                active_obj.draw()

            if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
                objects.append(active_obj)
                active_obj = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    current_shape = 'rectangle'
                elif event.key == pygame.K_p:
                    current_shape = 'pen'
                elif event.key == pygame.K_s:
                    current_shape = 'square'
                elif event.key == pygame.K_c:
                    current_shape = 'circle'
                elif event.key == pygame.K_e:  # E key for eraser
                    current_shape = 'eraser'
                elif event.key == pygame.K_1:
                    current_color = WHITE
                elif event.key == pygame.K_2:
                    current_color = RED
                elif event.key == pygame.K_3:
                    current_color = GREEN
                elif event.key == pygame.K_4:
                    current_color = BLUE

        for obj in objects:
            obj.draw()

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
