import pygame
import sys
import pyttsx3
import threading

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Robot Face")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)

file_text = ""

def draw_eyes(surface, eye_x, eye_y, eye_width, eye_height):
    # Make pixelated blue eyes
    pygame.draw.rect(surface, BLUE, [eye_x - SCREEN_WIDTH / 10, eye_y, eye_width, eye_height], 0, border_radius=10)
    pygame.draw.rect(surface, BLUE, [eye_x + SCREEN_WIDTH / 10, eye_y, eye_width, eye_height], 0, border_radius=10)

def draw_mouth(surface, is_speaking, mouth_frame):
    mouth_width = SCREEN_WIDTH // 4
    mouth_x = SCREEN_WIDTH // 2 - mouth_width // 2
    mouth_y = SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 6
    if is_speaking:
        opening_range = 40  # Range of mouth opening
        opening = opening_range * abs((mouth_frame % 20) - 10) / 10  # Compute mouth opening based on frame
        pygame.draw.rect(surface, WHITE, [mouth_x, mouth_y, mouth_width, 10 + opening], 0, border_radius=5)
    else:
        pygame.draw.rect(surface, WHITE, [mouth_x, mouth_y, mouth_width, 10], 0, border_radius=5)

def tts(text, filename):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()

def speak(filename):
    def _speak():
        global is_speaking
        speech = pygame.mixer.Sound(filename)
        is_speaking = True
        speech.play()
        duration_ms = int(speech.get_length() * 1000)  # Get duration in milliseconds
        pygame.time.wait(duration_ms - 500)  # Wait for the duration minus 500 milliseconds
        is_speaking = False

    # Run the speech in a separate thread
    threading.Thread(target=_speak).start()

def check_file(filename):
    global file_text
    try:
        with open(filename, 'r') as f:
            text = f.read()
            if text != file_text:
                file_text = text
                print("New Text Found:")
                print(text)
                print()
                if text != "":
                    tts(text, 'audio/output.wav')
                    speak('audio/output.wav')
            
    except Exception as e:
        print(e)

def main():
    global is_speaking, SCREEN_WIDTH, SCREEN_HEIGHT, screen
    is_speaking = False
    mouth_frame = 0  # Frame counter for mouth animation

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                tts("Hello world",'audio/test.wav')
                speak('audio/test.wav')

        check_file("input/text.txt")
        # Get the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calculate the eye positions based on the mouse position
        eye_width = SCREEN_WIDTH / 7
        eye_height = SCREEN_HEIGHT / 3
        eye_y = SCREEN_HEIGHT // 2 - eye_height
        eye_offset_x = (mouse_x - SCREEN_WIDTH // 2) // 10  # Adjust sensitivity as needed
        eye_x = SCREEN_WIDTH // 2 - eye_width / 2 + eye_offset_x

        screen.fill(BLACK)
        draw_eyes(screen, eye_x, eye_y, eye_width, eye_height)
        draw_mouth(screen, is_speaking, mouth_frame)  # Move mouth only when speaking

        pygame.display.flip()
        clock.tick(30)
        if is_speaking:
            mouth_frame += 1

if __name__ == "__main__":
    main()
