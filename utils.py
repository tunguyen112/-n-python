import pygame
import time

# Khởi tạo Pygame
pygame.init()

# Cài đặt kích thước cửa sổ
win_width = 1000
win_height = 800
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("ELEMENTS BATTLE")

instructions_screen = pygame.image.load('./Assets/Screen/Instructions_screen.jpg')

# Font và kích thước chữ
font = pygame.font.Font(None, 36)
fonts = pygame.font.Font('./Assets/Screen/Arial Unicode Font.ttf', 18)
fontss = pygame.font.Font('./Assets/Screen/Arial Unicode Font.ttf', 36)
fontss.set_bold(True)

# Bảng màu
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)
BROWN = (139, 69, 19)
GREENISH = (0, 128, 0)
LIGHT_BLUE = (173, 216, 230)
BURLYWOOD = (222, 184, 135)
LIGHT_GRAY = (200, 200, 200)

def fade_out():
    """Hàm tạo hiệu ứng tối dần
    
    Parameters:
        None

    Returns:
        None
    """
    black_surface = pygame.Surface((win_width, win_height))
    black_surface.fill((0, 0, 0))

    for alpha in range(0, 255):
        black_surface.set_alpha(alpha)
        window.blit(black_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(2)

def draw_you_lose():
    """Hàm vẽ chữ "You Lose" ở giữa màn hình
    
    Parameters:
        None

    Returns:
        None
    """
    text_surface = fontss.render("YOU LOSE", True, RED)
    text_rect = text_surface.get_rect(center=(win_width // 2, win_height // 2))
    window.blit(text_surface, text_rect)

def fade_out_lose():
    """Hàm vẽ chữ "You Lose" ở giữa màn hình đen tối dần
    
    Parameters:
        None

    Returns:
        None
    """
    black_surface = pygame.Surface((win_width, win_height))
    black_surface.fill((0, 0, 0))

    for alpha in range(0, 255):
        draw_you_lose()  # Vẽ chữ "You Lose" trên màn hình
        black_surface.set_alpha(alpha)
        window.blit(black_surface, (0, 0))
        pygame.time.delay(5)
        pygame.display.flip()

def play_sound(sound_file):
    """Hàm phát âm thanh cho game
    
    Parameters:
        None

    Returns:
        None
    """
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)

def draw_buttons_begin():
    """Hàm vẽ nút Start và Guide
    
    Parameters:
        None

    Returns:
        start_button (pygame.Rect): nút bắt đầu game
        guide_button (pygame.Rect) nút chuyển đến giao diện hướng dẫn
    """
    button_width = 200
    button_height = 50
    button_x = (win_width - button_width) // 2
    button_start_y = (win_height - 200) // 2
    button_guide_y = button_start_y + 100

    start_button = pygame.Rect(button_x, button_start_y, button_width, button_height)
    guide_button = pygame.Rect(button_x, button_guide_y, button_width, button_height)

    # Vẽ hình chữ nhật ngoài với màu chính 
    pygame.draw.rect(window, WHITE, start_button)
    pygame.draw.rect(window, WHITE, guide_button)

    # Vẽ khoảng trống giữa hai hình chữ nhật để tạo màu xám
    gap_rect_start = start_button.inflate(-8, -8)
    gap_rect_guide = guide_button.inflate(-8, -8)
    pygame.draw.rect(window, GRAY, gap_rect_start)
    pygame.draw.rect(window, GRAY, gap_rect_guide)

    # Vẽ hình chữ nhật nhỏ bên trong với màu trắng
    inner_rect_start = start_button.inflate(-16, -16)
    inner_rect_guide = guide_button.inflate(-16, -16)
    pygame.draw.rect(window, BROWN, inner_rect_start)
    pygame.draw.rect(window, BROWN, inner_rect_guide)

    # Vẽ các đường viền 
    pygame.draw.rect(window, BLACK, start_button, 4)
    pygame.draw.rect(window, BLACK, guide_button, 4)

    # Vẽ văn bản trung tâm
    start_text = font.render("Start", True, WHITE)
    start_text_rect = start_text.get_rect(center=start_button.center)
    window.blit(start_text, start_text_rect)

    guide_text = font.render("Guide", True, WHITE)
    guide_text_rect = guide_text.get_rect(center=guide_button.center)
    window.blit(guide_text, guide_text_rect)

    return start_button, guide_button

def draw_instructions_loichoi_screen():
    """Vẽ màn hình hướng dẫn lối chơi
    
    Parameters:
        None

    Returns:
        None
    """
    window.blit(instructions_screen, (win_width // 2 - instructions_screen.get_width() // 2, win_height // 2 - instructions_screen.get_height() // 2))
    pygame.display.flip()

    # Vẽ nội dung hướng dẫn
    # Văn bản của bạn
    text_lines = [
        "LỐI CHƠI:",
        "Game thẻ bài đánh theo lượt xoay quanh các phản ứng nguyên tố để chiến đấu.",
        "Đấu với máy. Có 3 chế độ: easy, medium, hard.",
        "Có 1 bộ thẻ bài nhân vật cho người chơi chọn 3 nhân vật 1 lần chơi.",
        "Có 1 bộ bài hỗ trợ. Người chơi sẽ được bốc mỗi lượt 1 thẻ.",
        "Tung xúc xắc để sử dụng nguyên tố.",
        "Xúc xắc có 4 mặt, tương ứng với 4 nguyên tố (thủy, hỏa, băng, lôi).",
        "Kết hợp sử dụng nguyên tố, kĩ năng nhân vật và thẻ bài hỗ trợ để đưa ra chiến thuật và giành chiến thắng.",
        "Trò chơi sẽ kết thúc khi 1 bên hết nhân vật.",
    ]

    # Tạo văn bản cho mỗi dòng
    y_position = win_height // 2 - len(text_lines) * font.get_height() // 2
    for line in text_lines:
        text_surface = fonts.render(line, True, LIGHT_BLUE)
        text_rect = text_surface.get_rect(center=(win_width // 2, y_position))
        window.blit(text_surface, text_rect)
        y_position += fonts.get_height()  # Điều chỉnh vị trí của dòng tiếp theo

    page_text = font.render("1/4", True, LIGHT_BLUE)
    page_text_rect = page_text.get_rect(center=(win_width // 2, win_height - 150))
    window.blit(page_text, page_text_rect)
    
    pygame.display.flip()

def draw_instructions_nhanvat_screen():
    """Vẽ màn hình hướng dẫn nhân vật
    
    Parameters:
        None

    Returns:
        None
    """
    window.blit(instructions_screen, (win_width // 2 - instructions_screen.get_width() // 2, win_height // 2 - instructions_screen.get_height() // 2))
    pygame.display.flip()

    # Vẽ nội dung hướng dẫn
    # Văn bản của bạn
    text_lines = [
        "NHÂN VẬT:",
        "Các nhân vật có chỉ số cơ bản tấn công, hp, def.",
        "Mỗi thẻ bài nhân vật sẽ có 2 hai loại kỹ năng: kỹ năng bị động và kĩ năng nộ.",
        "Kĩ năng bị động sẽ kích hoạt ngay khi ra sân.",
        "Kĩ năng nộ của mỗi nhân vật sẽ có điểm năng lượng riêng, tích điểm theo lượt và sử dụng được khi đủ điểm.",
    ]

    # Tạo văn bản cho mỗi dòng
    y_position = win_height // 2 - len(text_lines) * font.get_height() // 2
    for line in text_lines:
        text_surface = fonts.render(line, True, LIGHT_BLUE)
        text_rect = text_surface.get_rect(center=(win_width // 2, y_position))
        window.blit(text_surface, text_rect)
        y_position += fonts.get_height()  # Điều chỉnh vị trí của dòng tiếp theo

    page_text = font.render("2/4", True, LIGHT_BLUE)
    page_text_rect = page_text.get_rect(center=(win_width // 2, win_height - 150))
    window.blit(page_text, page_text_rect)
    
    pygame.display.flip()

def draw_instructions_batdau_screen():
    """Vẽ màn hình hướng dẫn bắt đầu
    
    Parameters:
        None

    Returns:
        None
    """
    window.blit(instructions_screen, (win_width // 2 - instructions_screen.get_width() // 2, win_height // 2 - instructions_screen.get_height() // 2))
    pygame.display.flip()

    # Vẽ nội dung hướng dẫn
    # Văn bản của bạn
    text_lines = [
        "BẮT ĐẦU:",
        "Mỗi trận người chơi sẽ chọn độ khó, chọn 3 nhân vật cho đội mình.",
        "Trò chơi sẽ chọn ngẫu nhiên đối thủ trong danh sách đã tạo theo độ khó mà người chơi đã chọn",
        "Trộn bộ thẻ bài hỗ trợ một cách ngẫu nhiên (bộ thẻ đã trộn này sẽ dùng cho suốt màn chơi).",
        "Bắt đầu trò chơi.",
    ]

    # Tạo văn bản cho mỗi dòng
    y_position = win_height // 2 - len(text_lines) * font.get_height() // 2
    for line in text_lines:
        text_surface = fonts.render(line, True, LIGHT_BLUE)
        text_rect = text_surface.get_rect(center=(win_width // 2, y_position))
        window.blit(text_surface, text_rect)
        y_position += fonts.get_height()  # Điều chỉnh vị trí của dòng tiếp theo

    page_text = font.render("3/4", True, LIGHT_BLUE)
    page_text_rect = page_text.get_rect(center=(win_width // 2, win_height - 150))
    window.blit(page_text, page_text_rect)
    
    pygame.display.flip()

def draw_instructions_cachchoi_screen():
    """Vẽ màn hình hướng dẫn cách chơi
    
    Parameters:
        None

    Returns:
        None
    """
    window.blit(instructions_screen, (win_width // 2 - instructions_screen.get_width() // 2, win_height // 2 - instructions_screen.get_height() // 2))
    pygame.display.flip()

    # Vẽ nội dung hướng dẫn
    # Văn bản của bạn
    text_lines = [
        "CÁCH CHƠI:",
        "Mỗi lượt sẽ được chọn nhân vật ra sân hoặc giữ nguyên nhân vật hiện tại(mặc định chọn nhân vật đầu tiên).",
        "Bốc thẻ đầu tiên bộ thẻ bài hỗ trợ.(Sau khi người chơi kích hoạt sẽ đưa thẻ bài về cuối bộ bài)",
        "Tung xúc xắc để sử dụng nguyên tố.",
        "Sử dụng nguyên tố để áp dụng hiệu quả lên bản thân hoặc tấn công đối thủ.",
        "Đối với việc tấn công đối thủ, chỉ có thể tấn công nhân vật đang ra trận của đối thủ (phản ứng nguyên tố sẽ tính riêng).",
        "Sau khi sử dụng nguyên tố lên bản thân hoặc đối thủ xong thì sẽ hết lượt và chuyển sang lượt của đối thủ.",
        "Khi người chơi muốn kết thúc thì nhấn vào nút thoát để trở về giao diện bắt đầu."
    ]

    # Tạo văn bản cho mỗi dòng
    y_position = win_height // 2 - len(text_lines) * font.get_height() // 2
    for line in text_lines:
        text_surface = fonts.render(line, True, LIGHT_BLUE)
        text_rect = text_surface.get_rect(center=(win_width // 2, y_position))
        window.blit(text_surface, text_rect)
        y_position += fonts.get_height()  # Điều chỉnh vị trí của dòng tiếp theo

    page_text = font.render("4/4", True, LIGHT_BLUE)
    page_text_rect = page_text.get_rect(center=(win_width // 2, win_height - 150))
    window.blit(page_text, page_text_rect)
    
    pygame.display.flip()

def draw_button_back(color):
    """Hàm vẽ nút back
    
    Parameters:
        color (tuple): mã màu cần vẽ

    Returns:
        back_button (pygame.Rect): nút trở về
    """
    # Vị trí của nút "Back" ở góc phải trên
    back_button_width = 60
    back_button_height = 60
    back_button_x = win_width - back_button_width - 20
    back_button_y = 20

    # Vẽ nút "Back"
    back_button = pygame.Rect(back_button_x, back_button_y, back_button_width, back_button_height)
    pygame.draw.rect(window, color, back_button)  

    # Vẽ văn bản trung tâm cho nút "Back"
    button_text_back = font.render("Back", True, BLACK)
    button_text_rect_back = button_text_back.get_rect(center=back_button.center)
    window.blit(button_text_back, button_text_rect_back)

    return back_button

def draw_button_guide():
    """Hàm vẽ các nút của giao diện hướng dẫn
    
    Parameters:
        None

    Returns:
        next_button (pygame.Rect): nút chuyển trang tiếp theo
        previous_button (pygame.Rect): nút trở về trang trước
    """
    # Vị trí ngang giữa màn hình
    middle_x = win_width // 2

    # Vị trí của nút chuyển trang
    button_width = 150
    button_height = 50
    button_y = win_height - 100
    button_spacing = 20  # Khoảng cách giữa hai nút
    button_x_next = middle_x + button_spacing // 2  # Vị trí x của nút "Next"
    button_x_previous = middle_x - button_width - button_spacing // 2  # Vị trí x của nút "Previous"

    # Vẽ nút "Next"
    next_button = pygame.Rect(button_x_next, button_y, button_width, button_height)
    pygame.draw.rect(window, GREENISH, next_button)  

    # Vẽ văn bản trung tâm cho nút "Next"
    button_text_next = font.render("Next", True, BLACK)
    button_text_rect_next = button_text_next.get_rect(center=next_button.center)
    window.blit(button_text_next, button_text_rect_next)

    # Vẽ nút "Previous"
    previous_button = pygame.Rect(button_x_previous, button_y, button_width, button_height)
    pygame.draw.rect(window, GREENISH, previous_button)  

    # Vẽ văn bản trung tâm cho nút "Previous"
    button_text_previous = font.render("Previous", True, BLACK)
    button_text_rect_previous = button_text_previous.get_rect(center=previous_button.center)
    window.blit(button_text_previous, button_text_rect_previous)

    return next_button, previous_button

def draw_difficulty_buttons():
    """Hàm vẽ các nút giao diện chọn độ khó
    
    Parameters:
        None

    Returns:
        easy_button (pygame.Rect): nút chọn độ khó dễ
        medium_button (pygame.Rect): nút chọn độ khó trung bình
        hard_button (pygame.Rect): nút chọn độ khó khó
    """
    # Tiêu đề
    title_text = fontss.render("CHOOSE DIFFICULTY", True, BROWN)
    title_text_rect = title_text.get_rect(center=(win_width // 2, 180))
    window.blit(title_text, title_text_rect)

    button_width = 200
    button_height = 50
    button_x = (win_width - button_width) // 2
    button_easy_y = (win_height - 200) // 2
    button_medium_y = button_easy_y + 100
    button_hard_y = button_medium_y + 100

    easy_button = pygame.Rect(button_x, button_easy_y, button_width, button_height)
    medium_button = pygame.Rect(button_x, button_medium_y, button_width, button_height)
    hard_button = pygame.Rect(button_x, button_hard_y, button_width, button_height)

    # Vẽ hình chữ nhật ngoài với màu chính 
    pygame.draw.rect(window, WHITE, easy_button)
    pygame.draw.rect(window, WHITE, medium_button)
    pygame.draw.rect(window, WHITE, hard_button)

    # Vẽ khoảng trống giữa hai hình chữ nhật để tạo màu xám
    gap_rect_easy = easy_button.inflate(-8, -8)
    gap_rect_medium = medium_button.inflate(-8, -8)
    gap_rect_hard = hard_button.inflate(-8, -8)
    pygame.draw.rect(window, GRAY, gap_rect_easy)
    pygame.draw.rect(window, GRAY, gap_rect_medium)
    pygame.draw.rect(window, GRAY, gap_rect_hard)

    # Vẽ hình chữ nhật nhỏ bên trong với màu trắng
    inner_rect_easy = easy_button.inflate(-16, -16)
    inner_rect_medium = medium_button.inflate(-16, -16)
    inner_rect_hard = hard_button.inflate(-16, -16)
    pygame.draw.rect(window, BROWN, inner_rect_easy)
    pygame.draw.rect(window, BROWN, inner_rect_medium)
    pygame.draw.rect(window, BROWN, inner_rect_hard)

    # Vẽ các đường viền 
    pygame.draw.rect(window, BLACK, easy_button, 4)
    pygame.draw.rect(window, BLACK, medium_button, 4)
    pygame.draw.rect(window, BLACK, hard_button, 4)

    # Vẽ văn bản trung tâm
    start_text = font.render("EASY", True, WHITE)
    start_text_rect = start_text.get_rect(center=easy_button.center)
    window.blit(start_text, start_text_rect)

    guide_text = font.render("MEDIUM", True, WHITE)
    guide_text_rect = guide_text.get_rect(center=medium_button.center)
    window.blit(guide_text, guide_text_rect)

    guide_text = font.render("HARD", True, WHITE)
    guide_text_rect = guide_text.get_rect(center=hard_button.center)
    window.blit(guide_text, guide_text_rect)

    return easy_button, medium_button, hard_button

def draw_title_choose_character():
    """Hàm vẽ tiêu đề cho màn hình chọn nhân vật
    
    Parameters:
        None
    
    Returns:
        None
    """
    title_text = fontss.render("CHOOSE YOUR CHARACTERS", True, BROWN)
    title_text_rect = title_text.get_rect(center=(win_width // 2, 50))
    window.blit(title_text, title_text_rect)
    pygame.display.flip()

def draw_button_finish():
    """Hàm vẽ nút Finish
    
    Parameters:
        None

    Returns:
        finish_button (pygame.Rect): nút kết thúc chọn nhân vật
    """
    # Kích thước của nút "Finish"
    finish_button_width = 100
    finish_button_height = 50

    # Vị trí của nút "Finish" ở giữa phía dưới cùng
    finish_button_x = (win_width - finish_button_width) // 2
    finish_button_y = win_height - 100

    # Vẽ nút "Finish"
    finish_button = pygame.Rect(finish_button_x, finish_button_y, finish_button_width, finish_button_height)
    pygame.draw.rect(window, GREENISH, finish_button)  

    # Vẽ văn bản trung tâm cho nút "Finish"
    button_text_finish = font.render("Finish", True, BLACK)
    button_text_rect_finish = button_text_finish.get_rect(center=finish_button.center)
    window.blit(button_text_finish, button_text_rect_finish)

    return finish_button

def draw_fading_text(text, font, color, position, duration):
    """Hàm tạo hiệu ứng chữ tối dần
    
    Parameters:
        text (string): chữ cần tạo
        font (pygame.font.Font()): phông chữ
        color (tuple): màu chữ
        position: vị trí
        duration: thời gian hiện
    
    Returns:
        None
    """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)

    for alpha in range(255, -1, -1):  # Lặp từ 255 (trắng) đến 0 (đen)
        window.fill((0, 0, 0))  # Vẽ màn hình đen
        text_surface.set_alpha(alpha)  # Đặt độ trong suốt cho chữ
        window.blit(text_surface, text_rect)  # Vẽ chữ lên màn hình
        pygame.display.flip()  # Cập nhật màn hình
        pygame.time.delay(2)  # Đợi một khoảng thời gian

def draw_loading_screen(current_screen):
    """Thực hiện vẽ màn hình loading
    
    Parameters:
        current_screen (string): màn hình hiện tại

    Returns:
        current_screen (string): màn hình hiện tại
    """
    # Lấy thời gian bắt đầu
    start_time = pygame.time.get_ticks()

    while current_screen == 'load':
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time

        # Vẽ màn hình đen
        window.fill(BLACK)

        center=(win_width // 2, win_height - 50)
        draw_fading_text('Loading...', font, WHITE, center, 500)

        pygame.display.flip()

        # Thoát khỏi vòng lặp sau khi đã hiển thị trong 2 giây (tức là elapsed_time >= 2000 milliseconds)
        if elapsed_time > 2000:
            current_screen = 'choose characters'

    return current_screen

def draw_button_refresh():
    """Hàm vẽ nút Refresh

    Parameters:
        None

    Returns:
        refresh_button (pygame.Rect): nút đổi nhân vật đối thủ
    """
    # Vị trí của nút "Refresh" ở góc trái trên
    refresh_button_width = 100
    refresh_button_height = 60
    refresh_button_x = 20
    refresh_button_y = 20

    # Vẽ nút "Refresh"
    refresh_button = pygame.Rect(refresh_button_x, refresh_button_y, refresh_button_width, refresh_button_height)
    pygame.draw.rect(window, BROWN, refresh_button)  

    # Vẽ văn bản trung tâm cho nút "Refresh"
    button_text_refresh = font.render("Refresh", True, BLACK)
    button_text_rect_refresh = button_text_refresh.get_rect(center=refresh_button.center)
    window.blit(button_text_refresh, button_text_rect_refresh)

    return refresh_button

def draw_button_start():
    """Hàm vẽ nút Start
    
    Parameters:
        None

    Returns:
        start_button (pygame.Rect): nút bắt đầu trận đấu
    """
    # Kích thước của nút "Start"
    start_button_width = 100
    start_button_height = 50

    # Vị trí của nút "Start" ở giữa phía dưới cùng
    start_button_x = (win_width - start_button_width) // 2
    start_button_y = win_height - 150

    # Vẽ nút "Start"
    start_button = pygame.Rect(start_button_x, start_button_y, start_button_width, start_button_height)
    pygame.draw.rect(window, BROWN, start_button)  

    # Vẽ văn bản trung tâm cho nút "Start"
    button_text_start = font.render("Start", True, BLACK)
    button_text_rect_start = button_text_start.get_rect(center=start_button.center)
    window.blit(button_text_start, button_text_rect_start)

    return start_button

def draw_button_battle():
    """Hàm vẽ các nút trong trận đấu
    
    Return:
        change_button (pygame.Rect): nút thay đổi thứ tự nhân vật của người chơi
        attack_button (pygame.Rect): nút người chơi thực hiện hành động tấn công
        use_element_button (pygame.Rect): nút người chơi thực hiện hành động sử dụng nguyên tố
        end_turn_button (pygame.Rect): nút người chơi thực hiện việc kết thúc lượt của mình
        roll_dice_button (pygame.Rect): nút người chơi thực hiện việc xoay xúc xắc
    """
    # Kích thước của nút "Change Character"
    change_button_width = 250
    change_button_height = 50
    change_button_x = win_width - change_button_width - 20
    change_button_y = win_height // 2

    # Vẽ viền đen cho nút "Change Character"
    change_button_outline = pygame.Rect(change_button_x - 2, change_button_y - 2, change_button_width + 4, change_button_height + 4)
    pygame.draw.rect(window, BLACK, change_button_outline)

    # Vẽ nút "Change Character"
    change_button = pygame.Rect(change_button_x, change_button_y, change_button_width, change_button_height)
    pygame.draw.rect(window, YELLOW, change_button)  

    # Vẽ văn bản trung tâm cho nút "Change Character"
    button_text_change = font.render("Change Character", True, BLACK)
    button_text_rect_change = button_text_change.get_rect(center=change_button.center)
    window.blit(button_text_change, button_text_rect_change)

    # Kích thước của nút "Attack"
    attack_button_width = 250
    attack_button_height = 50
    attack_button_x = win_width - attack_button_width - 20
    attack_button_y = win_height // 2 - change_button_height - 10  # Đặt nút Attack ở phía trên nút Change Character

    # Vẽ viền đen cho nút "Attack"
    attack_button_outline = pygame.Rect(attack_button_x - 2, attack_button_y - 2, attack_button_width + 4, attack_button_height + 4)
    pygame.draw.rect(window, BLACK, attack_button_outline)

    # Vẽ nút "Attack"
    attack_button = pygame.Rect(attack_button_x, attack_button_y, attack_button_width, attack_button_height)
    pygame.draw.rect(window, RED, attack_button)

    # Vẽ văn bản trung tâm cho nút "Attack"
    button_text_attack = font.render("Attack", True, BLACK)
    button_text_rect_attack = button_text_attack.get_rect(center=attack_button.center)
    window.blit(button_text_attack, button_text_rect_attack)

    # Kích thước của nút "Use Element"
    use_element_button_width = 250
    use_element_button_height = 50
    use_element_button_x = win_width - use_element_button_width - 20
    use_element_button_y = win_height // 2 - 2 * change_button_height - 20  # Đặt nút "Use Element" ở phía trên nút "Attack"

    # Vẽ viền đen cho nút "Use Element"
    use_element_button_outline = pygame.Rect(use_element_button_x - 2, use_element_button_y - 2, use_element_button_width + 4, use_element_button_height + 4)
    pygame.draw.rect(window, BLACK, use_element_button_outline)

    # Vẽ nút "Use Element"
    use_element_button = pygame.Rect(use_element_button_x, use_element_button_y, use_element_button_width, use_element_button_height)
    pygame.draw.rect(window, BLUE, use_element_button)

    # Vẽ văn bản trung tâm cho nút "Use Element"
    button_text_use_element = font.render("Use Element", True, BLACK)
    button_text_rect_use_element = button_text_use_element.get_rect(center=use_element_button.center)
    window.blit(button_text_use_element, button_text_rect_use_element)

    # Kích thước của nút "End Turn"
    end_turn_button_width = 250
    end_turn_button_height = 50
    end_turn_button_x = win_width - end_turn_button_width - 20
    end_turn_button_y = win_height // 2 + change_button_height + 10  # Đặt nút End Turn ở phía dưới nút Change Character

    # Vẽ viền đen cho nút "End Turn"
    end_turn_button_outline = pygame.Rect(end_turn_button_x - 2, end_turn_button_y - 2, end_turn_button_width + 4, end_turn_button_height + 4)
    pygame.draw.rect(window, BLACK, end_turn_button_outline)

    # Vẽ nút "End Turn"
    end_turn_button = pygame.Rect(end_turn_button_x, end_turn_button_y, end_turn_button_width, end_turn_button_height)
    pygame.draw.rect(window, GREEN, end_turn_button)

    # Vẽ văn bản trung tâm cho nút "End Turn"
    button_text_end_turn = font.render("End Turn", True, BLACK)
    button_text_rect_end_turn = button_text_end_turn.get_rect(center=end_turn_button.center)
    window.blit(button_text_end_turn, button_text_rect_end_turn)

    # Kích thước của nút "Roll Dice"
    roll_dice_button_width = 250
    roll_dice_button_height = 50
    roll_dice_button_x = 20
    roll_dice_button_y = win_height // 2

    # Vẽ viền đen cho nút "Roll Dice"
    roll_dice_button_outline = pygame.Rect(roll_dice_button_x - 2, roll_dice_button_y - 2, roll_dice_button_width + 4, roll_dice_button_height + 4)
    pygame.draw.rect(window, BLACK, roll_dice_button_outline)

    # Vẽ nút "Roll Dice"
    roll_dice_button = pygame.Rect(roll_dice_button_x, roll_dice_button_y, roll_dice_button_width, roll_dice_button_height)
    pygame.draw.rect(window, PURPLE, roll_dice_button)

    # Vẽ văn bản trung tâm cho nút "Roll Dice"
    button_text_roll_dice = font.render("Roll Dice", True, BLACK)
    button_text_rect_roll_dice = button_text_roll_dice.get_rect(center=roll_dice_button.center)
    window.blit(button_text_roll_dice, button_text_rect_roll_dice)

    return change_button, attack_button, use_element_button, end_turn_button, roll_dice_button

        

