import pygame as pg
import random
import sys, os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

pg.init()
def load_font(path, size):
    try:
        return pg.font.Font(resource_path(path), size)
    except FileNotFoundError:
        print(f"Font file '{path}' not found. Using default font.")
        return pg.font.SysFont(None, size)
font = load_font("title_font.ttf",60)
small_font = load_font("text.otf", 50)

black = (0, 0, 0)
red = (120, 1, 22)
orange =(216, 87, 42)
white = (255, 255, 255)

pg.init()
width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Mastermind")

def draw_text(text, font, color, x, y, center=False):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def generate_number():
    return str(random.randrange(1000, 10000))
def main():
    num = generate_number()
    user_input = ""
    message = "Guess the 4-digit number:"

    feedback = ""
    tries = 0
    game_over = False

    cursor_visible = True
    cursor_blink_speed = 500  
    last_blink_time = pg.time.get_ticks()

    textbox_rect = pg.Rect(80, 250, 200, 50)
    text_margin = 10

    running = True
    while running:
        current_time = pg.time.get_ticks()
        if current_time - last_blink_time >= cursor_blink_speed:
            cursor_visible = not cursor_visible
            last_blink_time = current_time

        screen.fill(red)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if game_over:
                    if event.key == pg.K_y:
                        main()  
                    elif event.key == pg.K_n:
                        pg.quit()
                        sys.exit()
                else:
                    if event.key == pg.K_RETURN:
                        if len(user_input) == 4 and user_input.isdigit():
                            tries += 1
                            count = 0
                            correct = ['X'] * 4
                            for i in range(4):
                                if user_input[i] == num[i]:
                                    count += 1
                                    correct[i] = user_input[i]

                            if user_input == num:
                                message = f"You guessed it in {tries} tries! Play again? (Y/N)"
                                feedback = f"The number was: {num}"
                                game_over = True
                            elif count > 0:
                                message = f"{count} digit(s) correct. Try again!"
                                feedback = "Correct digits so far: " + " ".join(correct)
                            else:
                                message = "None match. Try again!"
                                feedback = "Correct digits so far: X X X X"
                            user_input = ""
                        else:
                            message = "Enter a 4-digit number!"
                            feedback = ""
                    elif event.key == pg.K_BACKSPACE:
                        user_input = user_input[:-1]
                    elif event.unicode.isdigit() and len(user_input) < 4:
                        user_input += event.unicode

        draw_text("Mastermind", font, black, width // 2, 70, center=True)
        draw_text(message, small_font, black, 80, 160)
        draw_text(feedback, small_font, black, 80, 210)

        pg.draw.rect(screen, white, textbox_rect, border_radius=10)
        pg.draw.rect(screen, orange, textbox_rect, 2, border_radius=10)

        text_surface = small_font.render(user_input, True, black)
        text_width = text_surface.get_width()

        if text_width > textbox_rect.width - 2 * text_margin:
            offset_x = textbox_rect.x + textbox_rect.width - text_width - text_margin
        else:
            offset_x = textbox_rect.x + text_margin

        screen.blit(text_surface, (offset_x, textbox_rect.y + 10))

        if cursor_visible and not game_over:
            cursor_x = offset_x + text_width + 2
            cursor_y = textbox_rect.y + 10
            if cursor_x > textbox_rect.x + textbox_rect.width - text_margin:
                cursor_x = textbox_rect.x + textbox_rect.width - text_margin
            pg.draw.line(screen, black, (cursor_x, cursor_y), (cursor_x, cursor_y + 30), 2)

        pg.display.flip()

main()
