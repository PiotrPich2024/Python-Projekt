import pygame
pygame.init()

# Ustawienia okna
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Przycisk - Hover i Kliknięcie")
clock = pygame.time.Clock()

# Kolory
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (100, 100, 255)
DARK_BLUE = (0, 0, 180)

# Przycisk (prostokąt)
button_rect = pygame.Rect(150, 120, 100, 50)

running = True
while running:
    screen.fill(WHITE)
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    print(mouse_click)

    # Sprawdź czy kursor jest nad przyciskiem
    if button_rect.collidepoint(mouse_pos):
        if mouse_click[0]:  # LPM kliknięty
            pygame.draw.rect(screen, DARK_BLUE, button_rect)
        else:
            pygame.draw.rect(screen, LIGHT_BLUE, button_rect)
    else:
        pygame.draw.rect(screen, BLUE, button_rect)

    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
