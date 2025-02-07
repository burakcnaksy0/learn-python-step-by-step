import pygame
import sys

# Pygame'i başlat
pygame.init()

# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ekran boyutları (Tam ekran için)
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h

# Ekranı oluştur (Tam ekran modunda)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Basit Oyun")

# Karakter özellikleri
character_size = 50
character_color = RED
character_x = SCREEN_WIDTH // 2
character_y = SCREEN_HEIGHT // 2
character_speed = 5

# Ana oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed
    if keys[pygame.K_UP]:
        character_y -= character_speed
    if keys[pygame.K_DOWN]:
        character_y += character_speed

    # Ekranı beyaz ile doldur
    screen.fill(WHITE)

    # Karakteri çiz
    pygame.draw.rect(screen, character_color, (character_x, character_y, character_size, character_size))

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarı
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
