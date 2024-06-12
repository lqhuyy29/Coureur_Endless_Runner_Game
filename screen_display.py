import pygame

def show_start_screen(screen, screen_img, font, SCREEN_WIDTH, SCREEN_HEIGHT):
    """
    Displays the start screen of the game.
    """
    screen.blit(screen_img, (0, 0))
    text = font.render("Press Enter to Play", True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

def show_game_over_screen(screen, screen_img, font, score, SCREEN_WIDTH, SCREEN_HEIGHT):
    """
    Displays the game over screen with the player's score.
    """
    screen.blit(screen_img, (0, 0))
    game_over_text = font.render(f"Game Over! Your Score: {score}", True, (255, 255, 255))
    game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
    screen.blit(game_over_text, game_over_text_rect)
    
    replay_text = font.render("Press Enter to Replay", True, (255, 255, 255))
    replay_text_rect = replay_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
    screen.blit(replay_text, replay_text_rect)
    pygame.display.flip()
