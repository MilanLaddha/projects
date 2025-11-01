import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
FONT = pygame.font.SysFont("Arial", 40)
SMALL_FONT = pygame.font.SysFont("Arial", 24)

# Hangman images (you'd load these from files)
# For now, let's use a simple representation like your graphic list
# You would ideally have 7 image files named hangman_0.png, hangman_1.png, etc.
hangman_images = []
for i in range(7):
    # This is a placeholder. You'd load actual images here.
    # For example: hangman_images.append(pygame.image.load(f"images/hangman_{i}.png"))
    hangman_images.append(None) # Placeholder if not using images yet

# Game variables
word_bank = [
        "apple", "banana", "orange", "grape", "strawberry",
        "blueberry", "kiwi", "pineapple", "mango", "peach",
        "cat", "dog", "bird", "fish", "hamster",
        "tree", "flower", "river", "mountain", "ocean",
        "happy", "sad", "angry", "excited", "calm",
        "run", "jump", "sing", "dance", "read",
        "python", "java", "csharp", "javascript", "ruby"
]
chosen_word = random.choice(word_bank)
guessed_letters = []
lives = 6
game_over = False
win = False

# Function to draw the hangman figure (using basic shapes for now)
def draw_hangman_pygame(screen, lives_left):
    # Draw scaffold (simplified)
    pygame.draw.line(screen, BLACK, (100, 500), (400, 500), 5) # Base
    pygame.draw.line(screen, BLACK, (150, 500), (150, 100), 5) # Post
    pygame.draw.line(screen, BLACK, (150, 100), (300, 100), 5) # Beam
    pygame.draw.line(screen, BLACK, (300, 100), (300, 150), 5) # Rope

    if lives_left < 6: # Head
        pygame.draw.circle(screen, BLACK, (300, 175), 25, 2)
    if lives_left < 5: # Body
        pygame.draw.line(screen, BLACK, (300, 200), (300, 280), 2)
    if lives_left < 4: # Left Arm
        pygame.draw.line(screen, BLACK, (300, 220), (270, 250), 2)
    if lives_left < 3: # Right Arm
        pygame.draw.line(screen, BLACK, (300, 220), (330, 250), 2)
    if lives_left < 2: # Left Leg
        pygame.draw.line(screen, BLACK, (300, 280), (280, 320), 2)
    if lives_left < 1: # Right Leg
        pygame.draw.line(screen, BLACK, (300, 280), (320, 320), 2)

    # If you had images:
    # if hangman_images[6 - lives_left]:
    #    screen.blit(hangman_images[6 - lives_left], (appropriate_x, appropriate_y))


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.unicode.isalpha(): # Check if it's an alphabet character
                    guess = event.unicode.lower()
                    if guess not in guessed_letters:
                        guessed_letters.append(guess)
                        if guess not in chosen_word:
                            lives -= 1

    # Clear screen
    screen.fill(WHITE)

    # Draw hangman
    draw_hangman_pygame(screen, lives)

    # Display word
    display_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    word_text = FONT.render(display_word, True, BLACK)
    screen.blit(word_text, (WIDTH // 2 - word_text.get_width() // 2, 400))

    # Display guessed letters
    guessed_text = SMALL_FONT.render(f"Guessed: {', '.join(sorted(guessed_letters))}", True, BLACK)
    screen.blit(guessed_text, (50, 550))

    # Check win/loss
    if "_" not in display_word:
        win = True
        game_over = True
    elif lives == 0:
        game_over = True

    if game_over:
        if win:
            message = FONT.render("YOU WIN!", True, GREEN)
        else:
            message = FONT.render("YOU LOSE!", True, RED)
        screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
        word_reveal = SMALL_FONT.render(f"The word was: {chosen_word}", True, BLACK)
        screen.blit(word_reveal, (WIDTH // 2 - word_reveal.get_width() // 2, HEIGHT // 2 + 50 - word_reveal.get_height() // 2))

    pygame.display.flip() # Update the full display Surface to the screen

pygame.quit()