import pygame
import sys
import time
from card_characters import *
import utils as u

# Khởi tạo Pygame
pygame.init()

# Cài đặt kích thước cửa sổ
win_width = 1000
win_height = 800
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("ELEMENTS BATTLE")

# Load và làm mịn các ảnh cần thiết
introduction_screen = pygame.image.load('./Assets/Screen/Introduction_screen.jpg')
introduction_screen = pygame.transform.smoothscale(introduction_screen, (1000, 800))
main_screen = pygame.image.load('./Assets/Screen/Main_screen.jpg')
main_screen = pygame.transform.smoothscale(main_screen, (1000, 800))
battle_screen = pygame.image.load('./Assets/Screen/Battle_screen.jpg')
battle_screen = pygame.transform.smoothscale(battle_screen, (1000, 800))
battle_prepare_screen = pygame.image.load('./Assets/Screen/Battle_prepare_screen.jpg')
battle_prepare_screen = pygame.transform.smoothscale(battle_prepare_screen, (1000, 800))
win_screen = pygame.image.load('./Assets/Screen/Win_screen.jpg')
win_screen = pygame.transform.smoothscale(win_screen, (1000, 800))
icon = pygame.image.load('./Assets/Screen/Icon.jpg')
icon = pygame.transform.smoothscale(icon, (32, 32))

# Thiết lập icon cho cửa sổ game
pygame.display.set_icon(icon)

# Hiện màn hình giới thiệu
window.blit(introduction_screen, (win_width // 2 - introduction_screen.get_width() // 2, win_height // 2 - introduction_screen.get_height() // 2))
pygame.display.flip()
# Chờ 1 giây
time.sleep(1)

# Màn hình tối dần
u.fade_out()

# Phát nhạc nền
u.play_sound("./Assets/Sounds/Main_screen_theme.mp3")

# Hiện màn hình bắt đầu
window.blit(main_screen, (win_width // 2 - main_screen.get_width() // 2, win_height // 2 - main_screen.get_height() // 2))
start, guide = u.draw_buttons_begin()

# Tạo các biến sự kiện
running = True
guide_event = False
difficulty = ''
difficult_event = False
show_characters = False
show_opponent = False
battle_event = False
player_turn = True
win_event = False
button_clicked = False
roll_button_clicked = False
end_turn_button_clicked = False
current_screen = 'start'

# Vòng lặp game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "start":
                mouse_pos = event.pos
                if start.collidepoint(mouse_pos):
                    # Xử lý màn hình độ khó
                    window.blit(main_screen, (win_width // 2 - main_screen.get_width() // 2, win_height // 2 - main_screen.get_height() // 2))
                    easy, medium, hard = u.draw_difficulty_buttons()
                    back = u.draw_button_back(u.GREENISH)
                    current_screen = "difficulty"
                    difficult_event = True
                elif guide.collidepoint(mouse_pos):
                    # Xử lý các màn hình hướng dẫn
                    u.draw_instructions_loichoi_screen()
                    next, pre = u.draw_button_guide()
                    back = u.draw_button_back(u.GREENISH)
                    pygame.mixer.music.stop()
                    u.play_sound("./Assets/Sounds/Guide_theme.mp3")
                    current_screen = 'loichoi'
                    guide_event = True

            elif current_screen == "difficulty":
                if difficult_event:
                    df_mouse_pos = event.pos
                    if easy.collidepoint(df_mouse_pos):
                        difficulty = 'easy'
                        current_screen = 'load'
                        current_screen = u.draw_loading_screen(current_screen)
                        show_characters = True
                    elif medium.collidepoint(df_mouse_pos):
                        difficulty = 'medium'
                        current_screen = 'load'
                        current_screen = u.draw_loading_screen(current_screen)
                        show_characters = True
                    elif hard.collidepoint(df_mouse_pos):
                        difficulty = 'hard'
                        current_screen = 'load'
                        current_screen = u.draw_loading_screen(current_screen)
                        show_characters = True
                    elif back.collidepoint(df_mouse_pos):
                        # Hiện màn hình bắt đầu
                        window.blit(main_screen, (win_width // 2 - main_screen.get_width() // 2, win_height // 2 - main_screen.get_height() // 2))
                        start, guide = u.draw_buttons_begin()
                        current_screen = "start"
                        difficult_event = False

            elif guide_event:
                # Hiện màn hình hướng dẫn
                guide_mouse_pos = event.pos
                if next.collidepoint(guide_mouse_pos):
                    if current_screen == 'loichoi':
                        u.draw_instructions_nhanvat_screen()
                        u.draw_button_guide()
                        u.draw_button_back(u.GREENISH)
                        current_screen = 'nhanvat'
                    elif current_screen == 'nhanvat':
                        u.draw_instructions_batdau_screen()
                        u.draw_button_guide()
                        u.draw_button_back(u.GREENISH)
                        current_screen = 'batdau'
                    elif current_screen == 'batdau':
                        u.draw_instructions_cachchoi_screen()
                        u.draw_button_guide()
                        u.draw_button_back(u.GREENISH)
                        current_screen = 'cachchoi'
                    elif current_screen == 'cachchoi':
                        u.draw_instructions_loichoi_screen()
                        u.draw_button_guide()
                        u.draw_button_back(u.GREENISH)
                        current_screen = 'loichoi'
                elif pre.collidepoint(guide_mouse_pos):
                    if current_screen == 'loichoi':
                        u.draw_instructions_cachchoi_screen()
                        u.draw_button_guide()
                        u.draw_button_back(u.GREENISH)
                        current_screen = 'cachchoi'
                    elif current_screen == 'cachchoi':
                        u.draw_instructions_batdau_screen()
                        u.draw_button_guide()
                        u.draw_button_back(u.GREENISH)
                        current_screen = 'batdau'
                    elif current_screen == 'batdau':
                        u.draw_instructions_nhanvat_screen()
                        u.draw_button_guide()
                        u.draw_button_back(u.GREENISH)
                        current_screen = 'nhanvat'
                    elif current_screen == 'nhanvat':
                        u.draw_instructions_loichoi_screen()
                        u.draw_button_guide()
                        u.draw_button_back(u.GREENISH)
                        current_screen = 'loichoi'
                elif back.collidepoint(guide_mouse_pos):
                    # Hiện màn hình bắt đầu
                    window.blit(main_screen, (win_width // 2 - main_screen.get_width() // 2, win_height // 2 - main_screen.get_height() // 2))
                    start, guide = u.draw_buttons_begin()
                    pygame.mixer.music.stop()
                    u.play_sound("./Assets/Sounds/Main_screen_theme.mp3")
                    current_screen = 'start'
                    guide_event = False

            if show_characters:
                if current_screen == 'choose characters':
                    # Hiện màn hình chọn nhân vật
                    window.blit(main_screen, (win_width // 2 - main_screen.get_width() // 2, win_height // 2 - main_screen.get_height() // 2))
                    u.draw_title_choose_character()
                    back = u.draw_button_back(u.GREENISH)
                    characters_mouse_pos = event.pos

                    display_character_cards()  # Hiển thị danh sách thẻ nhân vật
                    if event.button == 3: # Nhấn chuột phải
                        for card in character_cards:
                            if card.rect.collidepoint(characters_mouse_pos):
                                display_character_stats(card.character)

                    selected_characters, character_order = handle_mouse_event(event, selected_characters, character_order) # Chọn nhân vật
                    for card in character_cards:
                        character = card.character
                        if character in selected_characters:
                            order = character_order[character]
                            # Tính toán vị trí của văn bản thứ tự ở góc phải trên cùng của thẻ nhân vật
                            font = pygame.font.SysFont(None, 18)
                            order_text = font.render(str(order), True, u.RED)
                            order_rect = order_text.get_rect(topright=(card.rect.right - 5, card.rect.top + 5))  # Điều chỉnh vị trí dựa trên góc trên cùng bên phải của thẻ nhân vật
                            window.blit(order_text, order_rect)
                    finish = u.draw_button_finish()
                    if len(character_order) == 3 and finish.collidepoint(characters_mouse_pos):
                        # Khởi tạo đối thủ
                        pygame.mixer.music.stop()
                        u.play_sound("./Assets/Sounds/Prepare_theme.mp3")
                        opponent_characters, opponent_order = select_opponent_characters(characters, selected_characters)
                        current_screen = 'show opponent'
                        show_opponent = True
                        show_characters = False
                    if back.collidepoint(characters_mouse_pos):
                        # Reset lại biến theo dõi các nhân vật đã chọn và thứ tự của chúng
                        selected_characters = []
                        character_order = {}
                        current_screen = "difficulty"
                        # Xử lý màn hình độ khó
                        window.blit(main_screen, (win_width // 2 - main_screen.get_width() // 2, win_height // 2 - main_screen.get_height() // 2))
                        easy, medium, hard = u.draw_difficulty_buttons()
                        back = u.draw_button_back(u.GREENISH)
                        difficult_event = True
                        show_characters = False

            if show_opponent:
                if current_screen == 'show opponent':
                    # Hiện màn hình nhân vật của 2 bên
                    window.blit(battle_prepare_screen, (win_width // 2 - battle_prepare_screen.get_width() // 2, win_height // 2 - battle_prepare_screen.get_height() // 2))
                    back = u.draw_button_back(u.BROWN)
                    refresh = u.draw_button_refresh()
                    start = u.draw_button_start()
                    draw_characters_on_screen(selected_characters, opponent_characters, event)

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        op_mouse_pos = event.pos
                        if refresh.collidepoint(op_mouse_pos):
                            opponent_characters, opponent_order = select_opponent_characters(characters, selected_characters)
                            draw_characters_on_screen(selected_characters, opponent_characters, event)
                        elif start.collidepoint(op_mouse_pos):
                            current_screen = 'battle'
                            opponent_seal_image = dict()
                            player_seal_image = dict()
                            window.blit(battle_screen, (win_width // 2 - battle_screen.get_width() // 2, win_height // 2 - battle_screen.get_height() // 2))
                            draw_battle(selected_characters, opponent_characters, character_order, opponent_order, event, opponent_seal_image, player_seal_image)
                            show_opponent = False
                            pygame.mixer.music.stop()
                            u.play_sound("./Assets/Sounds/Battle_theme.mp3")
                            battle_event = True
                        elif back.collidepoint(op_mouse_pos):
                            selected_characters = []
                            character_order = {}
                            window.blit(main_screen, (win_width // 2 - main_screen.get_width() // 2, win_height // 2 - main_screen.get_height() // 2))
                            u.draw_title_choose_character()
                            back = u.draw_button_back(u.GREENISH)
                            current_screen = 'choose characters'
                            display_character_cards()
                            show_characters = True
                            show_opponent = False

            if battle_event:
                change, attack, use, end, roll, back = draw_battle(selected_characters, opponent_characters, character_order, opponent_order, event, opponent_seal_image, player_seal_image)
                bt_mouse_pos = event.pos

                if player_turn:
                    if change.collidepoint(bt_mouse_pos):
                        character_order = update_character_order(character_order)
                        draw_battle(selected_characters, opponent_characters, character_order, opponent_order, event, opponent_seal_image, player_seal_image)
                    if roll.collidepoint(bt_mouse_pos) and not roll_button_clicked:
                        seal, seal_image = handle_roll_button_click(window)
                        roll_button_clicked = True
                    if attack.collidepoint(bt_mouse_pos) and not button_clicked and roll_button_clicked:
                        opponent_seal_image = handle_attack(character_order, opponent_order, seal, seal_image)
                        opponent_characters, opponent_order = handle_hp_changes(opponent_characters, opponent_order)
                        draw_battle(selected_characters, opponent_characters, character_order, opponent_order, event, opponent_seal_image, player_seal_image)
                        button_clicked = True
                    elif use.collidepoint(bt_mouse_pos) and not button_clicked:
                        handle_use_element(character_order, seal)
                        selected_characters, character_order = handle_hp_changes(selected_characters, character_order)
                        button_clicked = True
                    if end.collidepoint(bt_mouse_pos):
                        end_turn_button_clicked = True
                        player_turn = False
                if not player_turn and end_turn_button_clicked:
                    if difficulty == 'easy':
                        pl_seal, pl_seal_image = handle_roll_button_click(window)
                        player_seal_image = handle_attack(opponent_order, character_order, pl_seal, pl_seal_image)
                        selected_characters, character_order = handle_hp_changes(selected_characters, character_order)
                        draw_battle(selected_characters, opponent_characters, character_order, opponent_order, event, opponent_seal_image, player_seal_image)
                        player_turn = True
                        button_clicked = False
                        roll_button_clicked = False
                    elif difficulty == 'medium':
                        pass
                    elif difficulty == 'hard':
                        pass
                if len(character_order) <= 0:
                    u.fade_out_lose()
                    # Hiện màn hình bắt đầu
                    window.blit(main_screen, (win_width // 2 - main_screen.get_width() // 2, win_height // 2 - main_screen.get_height() // 2))                        
                    start, guide = u.draw_buttons_begin()
                    current_screen = "start"
                    # Phát nhạc nền
                    u.play_sound("./Assets/Sounds/Main_screen_theme.mp3")
                    battle_event = False
                if len(opponent_order) <= 0:
                    # Reset lại biến theo dõi các nhân vật đã chọn và thứ tự của chúng
                    selected_characters = []
                    character_order = {}
                    # Hiện màn hình chiến thắng
                    window.blit(win_screen, (win_width // 2 - win_screen.get_width() // 2, win_height // 2 - win_screen.get_height() // 2))
                    finish = u.draw_button_finish()
                    battle_event = False
                    win_event = True
                if back.collidepoint(bt_mouse_pos):
                    u.fade_out_lose()
                    # Reset lại biến theo dõi các nhân vật đã chọn và thứ tự của chúng
                    selected_characters = []
                    character_order = {}
                    # Hiện màn hình bắt đầu
                    window.blit(main_screen, (win_width // 2 - main_screen.get_width() // 2, win_height // 2 - main_screen.get_height() // 2))
                    start, guide = u.draw_buttons_begin()
                    current_screen = "start"
                    # Phát nhạc nền
                    u.play_sound("./Assets/Sounds/Main_screen_theme.mp3")
                    battle_event = False

            if win_event:
                # Hiện màn hình chiến thắng
                w_mouse_pos = event.pos
                if finish.collidepoint(w_mouse_pos):
                    # Hiện màn hình bắt đầu
                    window.blit(main_screen, (win_width // 2 - main_screen.get_width() // 2, win_height // 2 - main_screen.get_height() // 2))
                    start, guide = u.draw_buttons_begin()
                    current_screen = "start"
                    # Phát nhạc nền
                    u.play_sound("./Assets/Sounds/Main_screen_theme.mp3")    

    pygame.display.update()

# Kết thúc Pygame
pygame.quit()
sys.exit()

