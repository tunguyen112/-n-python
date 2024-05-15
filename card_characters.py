import pygame
import random
import time
import dice as d
import utils as u
from Game.characters import *

# Cài đặt kích thước cửa sổ
win_width = 1000
win_height = 800
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("ELEMENTS BATTLE")

font = pygame.font.SysFont(None, 24)

class CharacterCard:
    """Lớp định nghĩa thẻ nhân vật"""
    def __init__(self, character, order = 0):
        """Hàm khởi tạo
        
        Parameters:
            None

        Returns:
            None
        """
        self.character = character
        self.order = order
        self.width = 90
        self.height = 120
        self.image = pygame.Surface((self.width, self.height))  # Thay đổi kích thước của thẻ nhân vật
        self.rect = self.image.get_rect()

    def draw(self, surface, x, y):
        """Thực hiện việc vẽ khung cho thẻ nhân vật
        
        Parameters:
            surface (pygame.Surface): bề mặt vẽ
            x: vị trí tọa độ theo trục x
            y: vị trí tọa độ theo trục y

        Returns:
            None
        """
        pygame.draw.rect(surface, u.BLACK, (x - 1, y - 1, self.width + 4, self.height + 4), 8)  # Vẽ khung đen bao quanh
        surface.blit(self.image, (x, y))
        
        if self.order != 0:
            # Hiển thị thứ tự
            font = pygame.font.SysFont(None, 18)
            text_surface = font.render(str(self.order), True, u.BLACK)
            text_rect = text_surface.get_rect(center=(x + self.width // 2, y + 10))
            surface.blit(text_surface, text_rect)

    def render(self):
        """Thực hiện việc vẽ thẻ nhân vật lên màn hình
        
        Parameters:
            None

        Returns:
            None
        """
        # Vẽ background cho thẻ nhân vật
        self.image.fill(u.BURLYWOOD)
        
        # Load và làm mịn hình ảnh nhân vật
        character_image = pygame.image.load(f"./Assets/Characters/{self.character.name}.jpg")
        character_image = pygame.transform.smoothscale(character_image, (60, 60))  # Thay đổi kích thước và làm mịn
        self.image.blit(character_image, (15, 15))  # Điều chỉnh vị trí hiển thị hình ảnh

        # Vẽ khung đen bao quanh hình ảnh nhân vật
        pygame.draw.rect(self.image, u.BLACK, (15, 15, 60, 60), 2)

        # Vẽ tên nhân vật
        font = pygame.font.SysFont(None, 18)  # Điều chỉnh kích thước font chữ
        text_surface = font.render(self.character.name, True, u.BLACK)
        text_rect = text_surface.get_rect(center=(self.rect.width // 2, 90))
        self.image.blit(text_surface, text_rect)

    def resize(self, width, height):
        """Thực hiện việc thay đổi kích thước cho thẻ nhân vật
        
        Parameters:
            width: chiều rộng muốn thay đổi
            height: chiều cao muốn thay đổi
        
        Returns:
            None
        """
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))  # Tạo lại bề mặt với kích thước mới
        self.rect = self.image.get_rect()  # Cập nhật lại rect

        # Tính toán tỉ lệ thay đổi kích thước
        scale_x = width / 90  # Tỉ lệ thay đổi kích thước theo chiều rộng
        scale_y = height / 120  # Tỉ lệ thay đổi kích thước theo chiều cao

        # Load lại hình ảnh nhân vật và thay đổi kích thước theo tỉ lệ
        character_image = pygame.image.load(f"./Assets/Characters/{self.character.name}.jpg")
        character_image = pygame.transform.smoothscale(character_image, (int(60 * scale_x), int(60 * scale_y)))
        
        # Vẽ lại hình ảnh nhân vật và các thành phần khác trên bề mặt mới
        self.image.fill(u.BURLYWOOD)  # Vẽ background
        self.image.blit(character_image, (int(15 * scale_x), int(15 * scale_y)))  # Vẽ hình ảnh nhân vật
        pygame.draw.rect(self.image, u.BLACK, (int(15 * scale_x), int(15 * scale_y), int(60 * scale_x), int(60 * scale_y)), 2)  # Vẽ khung đen
        font = pygame.font.SysFont(None, 30)  # Điều chỉnh kích thước font chữ
        text_surface = font.render(self.character.name, True, u.BLACK)  # Vẽ tên nhân vật
        text_rect = text_surface.get_rect(center=(self.rect.width // 2, int(90 * scale_y)))
        self.image.blit(text_surface, text_rect)
    
# Tạo danh sách các nhân vật
characters = [
    furina(),
    mostima(),
    irfit(),
    ebenholz(),
    goldenglow(),
    lin(),
    eyjafjalla(),
    mudrock(),
    penance(),
    horn(),
    saria(),
    hoshiguma(),
    jessica(),
    gavial(),
    surtr(),
    mountain(),
    nearl(),
    mlynar(),
    thorns(),
    lappland(),
    nightingale(),
    reed(),
    kaltsit(),
    warfarin(),
    lumen(),
    archetto(),
    chen(),
    pozemka(),
    typhon(),
    gladiia(),
    skadi(),
    gnosis(),
]

# Tạo danh sách thẻ nhân vật
character_cards = [CharacterCard(character) for character in characters]

# Hiển thị danh sách thẻ nhân vật trên màn hình
x_offset = 50
y_offset = 100
spacing = 20
for i, card in enumerate(character_cards):
    card.rect.topleft = (x_offset + i * (card.rect.width + spacing), y_offset)
    card.render()

def display_character_cards():
    """Thực hiện việc vẽ tất cả các nhân vật lên màn hình
    
    Parameters:
        None

    Returns:
        None
    """
    x_offset = 50
    y_offset = 100
    spacing = 20
    row_length = 8  # Số lượng thẻ nhân vật trên mỗi hàng
    for i, card in enumerate(character_cards):
        row = i // row_length  # Tính toán hàng hiện tại
        col = i % row_length   # Tính toán cột hiện tại
        x = x_offset + col * (card.rect.width + spacing)
        y = y_offset + row * (card.rect.height + spacing)
        card.rect.topleft = (x, y)
        card.draw(window, x, y)

def display_character_stats(character):
    """Thực hiện việc hiện thông số của nhân vật
    
    Parameters:
        character (character): nhân vật muốn xem thông tin

    Returns:
        None
    """
    # Kiểm tra xem chuột có đang nhấn nút phải không
    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[2]:  # Nút phải được nhấn
        # Hiển thị thông số của nhân vật
        text_lines = [
            "Name: " + str(character.name),
            "Atk: " + str(character.Atk),
            "Hp: " + str(character.Hp),
            "Def: " + str(character.Def),
            "Effect: ",
        ]
        # Thêm mỗi cặp khóa-giá trị của từ điển character.effect vào danh sách dòng văn bản
        for key, value in character.effect.items():
            text_lines.append(f"{key}: {value}")
        # Tính toán kích thước bề mặt dựa trên số lượng dòng văn bản
        line_height = 20
        surface_height = len(text_lines) * line_height
        character_stats_surface = pygame.Surface((150, surface_height))
        character_stats_surface.fill(u.LIGHT_GRAY)
        
        # Hiển thị các thông số của nhân vật
        font = pygame.font.SysFont(None, 18)
        for i, line in enumerate(text_lines):
            text_surface = font.render(line, True, u.BLACK)
            character_stats_surface.blit(text_surface, (10, i * line_height))
        
        character_stats_rect = character_stats_surface.get_rect()
        character_stats_rect.topleft = pygame.mouse.get_pos()
        
        # Hiển thị bề mặt thông số nhân vật lên màn hình chính
        window.blit(character_stats_surface, character_stats_rect)

# Định nghĩa biến để theo dõi các nhân vật đã chọn và thứ tự của chúng
selected_characters = []
character_order = {}

def handle_mouse_event(event, selected_characters, character_order):
    """Hàm xử lý việc chọn nhân vật cho người chơi
    
    Parameters:
        event: sự kiện của game
        selected_characters (list): danh sách nhân vật người chơi đã chọn
        character_order (dictionary): danh sách nhân vật người chơi đã chọn và thứ tự của nhân vật
    
    Returns:
        selected_characters (list): danh sách nhân vật người chơi đã chọn
        character_order (dictionary): danh sách nhân vật người chơi đã chọn và thứ tự của nhân vật
    """
    characters_mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
        
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Chuột trái được nhấn
        # Kiểm tra xem chuột có nằm trên một nhân vật hay không
        for i, card in enumerate(character_cards):
            if card.rect.collidepoint(characters_mouse_pos):
                character = card.character
                if len(selected_characters) < 3:  # Chỉ cho phép chọn tối đa 3 nhân vật
                    if character in selected_characters:  # Nếu nhân vật đã được chọn, bỏ chọn nó
                        selected_characters.remove(character)
                        # Cập nhật lại thứ tự theo thứ tự mà người chơi đã chọn trước đó
                        for index, c in enumerate(selected_characters):
                            character_order[c] = index + 1
                        character_order.pop(character, None)  # Loại bỏ nhân vật khỏi danh sách thứ tự
                    else:  # Nếu nhân vật chưa được chọn, thêm vào danh sách và cập nhật thứ tự
                        selected_characters.append(character)
                        # Cập nhật thứ tự của nhân vật
                        character_order[character] = len(selected_characters)
                else:  # Nếu đã chọn đủ 3 nhân vật
                    if character in selected_characters:  # Nếu nhân vật đã được chọn
                        selected_characters.remove(character)
                        # Cập nhật lại thứ tự theo thứ tự mà người chơi đã chọn trước đó
                        for index, c in enumerate(selected_characters):
                            character_order[c] = index + 1
                        character_order.pop(character, None)  # Loại bỏ nhân vật khỏi danh sách thứ tự
                    else:  # Nếu nhân vật chưa được chọn
                        removed_character = selected_characters.pop(0)  # Loại bỏ nhân vật đầu tiên
                        character_order.pop(removed_character, None)  # Loại bỏ cả nhân vật khỏi danh sách thứ tự
                        selected_characters.append(character)  # Thêm nhân vật mới vào cuối danh sách
                        # Cập nhật lại thứ tự theo thứ tự mà người chơi đã chọn trước đó
                        for index, c in enumerate(selected_characters):
                            character_order[c] = index + 1
    return selected_characters, character_order

def select_opponent_characters(characters, selected_characters):
    """Chọn ngẫu nhiên các nhân vật cho đối thủ
    
    Parameters:
        characters (list): danh sách tất cả nhân vật
        selected_characters (list): danh sách các nhân vật người chơi đã chọn

    Returns:
        opponent_characters (list): danh sách nhân vật của đối thủ
        opponent_order (dictionary): danh sách nhân vật của đối thủ và thứ tự của nhân vật
    """
    # Loại bỏ các nhân vật đã được chọn cho người chơi khỏi danh sách nhân vật
    available_characters = [character for character in characters if character not in selected_characters]
    
    # Chọn ngẫu nhiên các nhân vật cho đối thủ từ danh sách nhân vật còn lại
    opponent_characters = random.sample(available_characters, 3)
    
    # Tạo danh sách thứ tự cho các nhân vật đã chọn
    opponent_order = {character: index + 1 for index, character in enumerate(opponent_characters)}
    
    return opponent_characters, opponent_order

def draw_characters_on_screen(selected_characters, opponent_characters, event):
    """Thực hiện việc vẽ thẻ nhân vật đã chọn cho cả người chơi và đối thủ lên màn hình
    
    Parameters:
        selected_characters (list): danh sách nhân vật người chơi đã chọn
        opponent_characters (list): danh sách nhân vật của đối thủ
        event: sự kiện của game

    Returns:
        None
    """
    title_text = u.fontss.render("BATTLE PREPARE", True, u.BROWN)
    title_text_rect = title_text.get_rect(center=(win_width // 2, 50))
    window.blit(title_text, title_text_rect)

    # Tạo danh sách thẻ nhân vật cho người chơi
    character_cards = [CharacterCard(selected_character) for selected_character in selected_characters]

    # Hiển thị danh sách thẻ nhân vật trên màn hình cho người chơi
    x_offset_player = 50
    y_offset_player = 100
    spacing_player = 20
    row_length_player = 4  # Số lượng thẻ nhân vật trên mỗi hàng
    card_width_player = 150  # Kích thước mới của thẻ nhân vật
    card_height_player = 200  # Kích thước mới của thẻ nhân vật
    for i, card in enumerate(character_cards):
        row = i % row_length_player  # Tính toán hàng hiện tại
        col = i // row_length_player  # Tính toán cột hiện tại
        x = x_offset_player + col * (card_width_player + spacing_player)
        y = y_offset_player + row * (card_height_player + spacing_player)
        card.resize(card_width_player, card_height_player)  # Thay đổi kích thước của thẻ nhân vật
        card.rect.topleft = (x, y)

    # Vẽ thẻ nhân vật cho người chơi
    for card in character_cards:
        card.draw(window, card.rect.x, card.rect.y)

    # Xử lý sự kiện nhấp chuột phải để hiển thị thông tin của nhân vật
    mouse_pos = event.pos
    if event.button == 3: # Nhấn chuột phải
        for card in character_cards:
            if card.rect.collidepoint(mouse_pos):
                display_character_stats(card.character)

    # Tạo danh sách thẻ nhân vật cho đối thủ
    opponent_cards = [CharacterCard(opponent_character) for opponent_character in opponent_characters]

    # Hiển thị danh sách thẻ nhân vật trên màn hình cho đối thủ
    x_offset_opponent = win_width - 50 - card_width_player  # Đảm bảo thẻ nhân vật cho đối thủ đặt ở cạnh phải của màn hình
    y_offset_opponent = y_offset_player  # Đối xứng với vị trí của thẻ người chơi theo trục y
    spacing_opponent = spacing_player  # Giữ nguyên khoảng cách giữa các thẻ
    row_length_opponent = row_length_player  # Số cột của thẻ nhân vật cho đối thủ giống với số cột của thẻ người chơi
    card_width_opponent = card_width_player  # Giữ nguyên kích thước của thẻ nhân vật cho đối thủ
    card_height_opponent = card_height_player  # Giữ nguyên kích thước của thẻ nhân vật cho đối thủ
    for i, card in enumerate(opponent_cards):
        row = i % row_length_opponent  # Tính toán hàng hiện tại
        col = i // row_length_opponent  # Tính toán cột hiện tại
        x = x_offset_opponent - col * (card_width_opponent + spacing_opponent)  # Đảo ngược vị trí x
        y = y_offset_opponent + row * (card_height_opponent + spacing_opponent)
        card.resize(card_width_opponent, card_height_opponent)  # Thay đổi kích thước của thẻ nhân vật
        card.rect.topleft = (x, y)

    # Vẽ thẻ nhân vật cho đối thủ
    for card in opponent_cards:
        card.draw(window, card.rect.x, card.rect.y)

    # Xử lý sự kiện nhấp chuột phải để hiển thị thông tin của nhân vật cho đối thủ
    if event.button == 3: # Nhấn chuột phải
        for card in opponent_cards:
            if card.rect.collidepoint(mouse_pos):
                display_character_stats(card.character)

    # Load hình ảnh từ tệp tin
    vs_icon = pygame.image.load('./Assets/Screen/Prepare_screen.jpg')

    # Điều chỉnh kích thước của hình ảnh để phù hợp với màn hình
    desired_width = 250
    desired_height = 200
    vs_icon = pygame.transform.smoothscale(vs_icon, (desired_width, desired_height))

    # Tính toán vị trí để đặt hình ảnh vào giữa màn hình
    x = (win_width - desired_width) // 2
    y = -desired_height  # Bắt đầu từ vị trí trên cùng của màn hình

    window.blit(vs_icon, (x, (win_height - desired_height) // 2))  # Hiển thị ảnh ở giữa màn hình
    pygame.display.update()

battle_screen = pygame.image.load('./Assets/Screen/Battle_screen.jpg')
battle_screen = pygame.transform.smoothscale(battle_screen, (1000, 800))

def draw_battle(selected_characters, opponent_characters, character_order, opponent_order, event, opponent_seal_image = None, player_seal_image = None):
    """Thực hiện việc vẽ tất cả các sự kiện trong trận đấu
    
    Parameters:
        selected_characters (list): danh sách nhân vật người chơi đã chọn
        opponent_characters (list): danh sách nhân vật của đối thủ
        character_order (dictionary): danh sách nhân vật người chơi đã chọn và thứ tự của nhân vật
        opponent_order (dictionary): danh sách nhân vật của đối thủ và thứ tự của nhân vật
        event: sự kiện của game
        opponent_seal_image (dictionary): danh sách nhân vật của đối thủ và hình ảnh con dấu tương ứng
        player_seal_image (dictionary): danh sách nhân vật của người chơi và hình ảnh con dấu tương ứng

    Return:
        change (pygame.Rect): nút thay đổi thứ tự nhân vật của người chơi
        attack (pygame.Rect): nút người chơi thực hiện hành động tấn công
        use(pygame.Rect): nút người chơi thực hiện hành động sử dụng nguyên tố
        end (pygame.Rect): nút người chơi thực hiện việc kết thúc lượt của mình
        roll (pygame.Rect): nút người chơi thực hiện việc xoay xúc xắc
        back (pygame.Rect): nút thoát trở về giao diện bắt đầu
    """
    window.blit(battle_screen, (win_width // 2 - battle_screen.get_width() // 2, win_height // 2 - battle_screen.get_height() // 2))
    change, attack, use, end, roll = u.draw_button_battle()
    back = u.draw_button_back(u.GREENISH)
    # Tạo danh sách thẻ nhân vật cho người chơi
    character_cards = [CharacterCard(selected_character) for selected_character in selected_characters]

    # Tạo danh sách thẻ nhân vật cho đối thủ
    opponent_cards = [CharacterCard(opponent_character) for opponent_character in opponent_characters]
    
    # Tính toán vị trí x cho các thẻ nhân vật của đối thủ
    x_offset_opponent = (win_width - (len(opponent_cards) * 150 + (len(opponent_cards) - 1) * 150)) // 2
    j = 0
    # Vẽ các thẻ nhân vật của đối thủ và hiển thị văn bản thứ tự
    for i, card in enumerate(opponent_cards):
        x = x_offset_opponent + i * 300
        y = 30  # Đặt ở đầu màn hình
        card.resize(150, 200)
        card.rect.topleft = (x, y)
        card.draw(window, card.rect.x, card.rect.y)

        # Hiển thị văn bản thứ tự trên thẻ nhân vật của đối thủ
        character = card.character
        order = opponent_order[character]
        font = pygame.font.SysFont(None, 30)
        order_text = font.render(str(order), True, u.RED)
        order_rect = order_text.get_rect(topright=(card.rect.right - 5, card.rect.top + 5))
        window.blit(order_text, order_rect)

        # Vẽ hình ảnh con dấu lên góc trái của hình ảnh nhân vật của đối thủ bị tấn công
        # Vẽ hình ảnh con dấu nếu có
        if opponent_seal_image is not None:
            if card.character in opponent_seal_image:
                seal_img = opponent_seal_image[card.character]
                window.blit(seal_img, (card.rect.x, card.rect.y))
                j += 1

        mouse_pos = event.pos
        # Xử lý sự kiện nhấp chuột phải để hiển thị thông tin của nhân vật cho đối thủ
        if event.button == 3 and card.rect.collidepoint(mouse_pos): # Nhấn chuột phải
            display_character_stats(character)

    # Tính toán vị trí x cho các thẻ nhân vật của người chơi
    x_offset_player = (win_width - (len(character_cards) * 150 + (len(character_cards) - 1) * 150)) // 2
    # Vẽ các thẻ nhân vật của người chơi và hiển thị văn bản thứ tự
    k = 0
    for i, card in enumerate(character_cards):
        x = x_offset_player + i * 300
        y = win_height - 250  # Đặt ở cuối màn hình
        card.resize(150, 200)
        card.rect.topleft = (x, y)
        card.draw(window, card.rect.x, card.rect.y)

        # Hiển thị văn bản thứ tự trên thẻ nhân vật của người chơi
        character = card.character
        order = character_order[character]
        font = pygame.font.SysFont(None, 30)
        order_text = font.render(str(order), True, u.RED)
        order_rect = order_text.get_rect(topright=(card.rect.right - 5, card.rect.top + 5))
        window.blit(order_text, order_rect)

        # Vẽ hình ảnh con dấu lên góc trái của hình ảnh nhân vật của người chơi bị tấn công
        if player_seal_image is not None:
            if card.character in player_seal_image:
                seal_img = player_seal_image[card.character]
                window.blit(seal_img, (card.rect.x, card.rect.y))
                k += 1

        # Xử lý sự kiện nhấp chuột phải để hiển thị thông tin của nhân vật
        if event.button == 3 and card.rect.collidepoint(mouse_pos): # Nhấn chuột phải
            display_character_stats(character)

    return change, attack, use, end, roll, back

def update_character_order(character_order):
    """Thực hiện việc thay đổi thứ tự nhân vật của người chơi
    
    Parameters:
        character_order (dictionary): danh sách nhân vật người chơi đã chọn và thứ tự của nhân vật

    Returns:
        character_order (dictionary): danh sách nhân vật người chơi đã chọn và thứ tự của nhân vật (đã thay đổi)
    """
    # Lấy danh sách các giá trị từ từ điển hiện tại
    current_values = list(character_order.values())
    l1 = [1,2,3]
    l2 = [1,3,2]
    l3 = [2,1,3]
    l4 = [2,3,1]
    l5 = [3,1,2]
    l6 = [3,2,1]
    l7 = [1,2]
    l8 = [2,1]
    i = 0
    if current_values == l1:
    # Cập nhật lại giá trị trong từ điển
        for key in character_order:
            character_order[key] = l2[i] # gán giá trị mới cho key
            i += 1 
    # So sánh danh sách giá trị hiện tại với danh sách giá trị mong muốn
    elif current_values == l2:
        # Cập nhật lại giá trị trong từ điển
        for key in character_order:
            character_order[key] = l3[i] # gán giá trị mới cho key
            i += 1 
    # So sánh danh sách giá trị hiện tại với danh sách giá trị mong muốn
    elif current_values == l3:
        # Cập nhật lại giá trị trong từ điển
        for key in character_order:
            character_order[key] = l4[i] # gán giá trị mới cho key
            i += 1 
    # So sánh danh sách giá trị hiện tại với danh sách giá trị mong muốn
    elif current_values == l4:
        # Cập nhật lại giá trị trong từ điển
        for key in character_order:
            character_order[key] = l5[i] # gán giá trị mới cho key
            i += 1 
    # So sánh danh sách giá trị hiện tại với danh sách giá trị mong muốn
    elif current_values == l5:
        # Cập nhật lại giá trị trong từ điển
        for key in character_order:
            character_order[key] = l6[i] # gán giá trị mới cho key
            i += 1 
    # So sánh danh sách giá trị hiện tại với danh sách giá trị mong muốn
    elif current_values == l6:
        # Cập nhật lại giá trị trong từ điển
        for key in character_order:
            character_order[key] = l1[i] # gán giá trị mới cho key
            i += 1  
     # So sánh danh sách giá trị hiện tại với danh sách giá trị mong muốn
    if current_values == l7:
        # Cập nhật lại giá trị trong từ điển
        for key in character_order:
            character_order[key] = l8[i] # gán giá trị mới cho key
            i += 1 
    # So sánh danh sách giá trị hiện tại với danh sách giá trị mong muốn
    elif current_values == l8:
        # Cập nhật lại giá trị trong từ điển
        for key in character_order:
            character_order[key] = l7[i] # gán giá trị mới cho key
            i += 1
    return character_order

character_seal_image = dict()

def handle_attack(character_order, opponent_order, seal, seal_image):
    """Thực hiện xử lý hành động tấn công.
    
    Parameters:
        character_order (dictionary): danh sách nhân vật tấn công và thứ tự của nhân vật
        opponent_order (dictionary): danh sách nhân vật bị tấn công và thứ tự của nhân vật
        seal (string): nguyên tố sử dụng để tấn công
        seal_image: hình ảnh nguyên tố tương ứng

    Returns:
        character_seal_image (dictionary): danh sách nhân vật và hình ảnh con dấu nguyên tố tương ứng
    """
    if len(character_order) > 0 and len(opponent_order) > 0:
        # Lấy nhân vật đầu tiên của người chơi và đối thủ
        player_character = next((character for character, order in character_order.items() if order == 1), None)
        opponent_character = next((character for character, order in opponent_order.items() if order == 1), None)
        # Thay đổi kích thước của ảnh
        desired_width = 25  # Chiều rộng mong muốn
        desired_height = 25  # Chiều cao mong muốn
        resize_seal_image = pygame.transform.smoothscale(seal_image, (desired_width, desired_height))
        # Thực hiện hành động tấn công
        player_character.attack(opponent_character, seal)
        character_seal_image[opponent_character] = resize_seal_image

        return character_seal_image  
    
def handle_use_element(character_order, seal):
    """Xử lý hành động sử dụng nguyên tố
    
    Parameters:
        character_order (dictionary): danh sách nhân vật sử dụng nguyên tố
        seal (string): nguyên tố được sử dụng
    
    Returns:
        None
    """
    if len(character_order) > 0:
        # Lấy nhân vật đầu tiên của người chơi và đối thủ
        player_character = next((character for character, order in character_order.items() if order == 1), None)
        player_character.using_element(seal)

def update_character_order_lost(character_order):
    """Cập nhật lại thứ tự cho character_order khi một nhân vật ngã xuống
    Parameters:
        character_order (dictionary): danh sách nhân vật

    Returns:
        updated_order (dictionary): danh sách nhân vật đã cập nhật thứ tự
    """
    updated_order = {}  # Tạo một dictionary mới để lưu trữ thứ tự đã cập nhật
    new_order = 1  # Bắt đầu từ thứ tự 1

    for character in character_order:
        updated_order[character] = new_order
        new_order += 1

    return updated_order

def handle_hp_changes(selected_characters, character_order):
    """Thực hiện xử lý việc thay đổi HP sau khi bị tấn công hoặc sau khi sử dụng nguyên tố.
    
    Parameters:
        selected_characters (list): danh sách nhân vật 
        character_order (dictionary): danh sách nhân vật và thứ tự của nhân vật
    
    Returns:
        selected_characters (list): danh sách nhân vật đã được cập nhật
        character_order (dictionary): danh sách nhân vật và thứ tự của nhân vật đã được cập nhật
    """
    characters_to_remove = []  # Danh sách các nhân vật cần loại bỏ

    for character, order in character_order.items():
        character.Hp_changed()  # Áp dụng thay đổi HP
        if character.Hp <= 0:
            characters_to_remove.append(character)  # Thêm nhân vật cần loại bỏ vào danh sách

    for character in selected_characters:
        if character.Hp <= 0:
            selected_characters.remove(character)

    # Loại bỏ nhân vật ra khỏi character_order và character_seal_image
    for character in characters_to_remove:
        del character_order[character]
        del character_seal_image[character]

    # Cập nhật lại thứ tự cho character_order
    if characters_to_remove != []:
        character_order = update_character_order_lost(character_order)

    return selected_characters, character_order

def handle_roll_button_click(window):
    """Thực hiện xử lý hiệu ứng và hiện kết quả xúc xắc
    
    Parameters:
        window (pygame.Surface): màn hình chính
    Returns:
        seal: kết quả nguyên tố 
        seal_image: hình ảnh tương ứng
    """
    # Gọi phương thức roll() của đối tượng Dice
    dice = d.Dice()
    dice.roll(window)
    seal, seal_image = dice.rolling()  # Lấy cả nguyên tố và hình ảnh tượng trưng
    # Thay đổi kích thước của ảnh
    desired_width = 25  # Chiều rộng mong muốn
    desired_height = 25  # Chiều cao mong muốn
    # Lấy kích thước của màn hình
    screen_width, screen_height = pygame.display.get_surface().get_size()
    # Tính toán vị trí để vẽ hình ảnh giữa màn hình
    x = (screen_width - desired_width) // 2 - 35
    y = (screen_height - desired_height) // 2 - 50
    # Vẽ seal_image lên màn hình
    window.blit(seal_image, (x, y))
    return seal, seal_image