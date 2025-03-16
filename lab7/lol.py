import pygame

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SORRY 4DA WAIT")

font = pygame.font.Font(None, 55)
text = font.render("Амина лох", True, (255, 255, 255))
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(text, text_rect)  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()
