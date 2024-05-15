import random
import pygame
import time

class Dice:
    """Lớp mô ta con xúc xắc"""
    def __init__(self):
        """Hàm khởi tạo
        
        Parameters:
            None

        Returns:
            None
        """
        self.m1 = 'Hỏa'
        self.m2 = 'Thủy'
        self.m3 = 'Băng'
        self.m4 = 'Lôi'
        # Thêm các thuộc tính hình ảnh tượng trưng cho từng nguyên tố
        self.fire_image = pygame.image.load('./Assets/Dice/Fire.jpg')
        self.ice_image = pygame.image.load('./Assets/Dice/Ice.jpg')
        self.electric_image = pygame.image.load('./Assets/Dice/Electric.jpg')
        self.water_image = pygame.image.load('./Assets/Dice/Water.jpg')
        # Thay đổi kích thước của các hình ảnh
        self.fire_image = pygame.transform.smoothscale(self.fire_image, (100, 100))
        self.ice_image = pygame.transform.smoothscale(self.ice_image, (100, 100))
        self.electric_image = pygame.transform.smoothscale(self.electric_image, (100, 100))
        self.water_image = pygame.transform.smoothscale(self.water_image, (100, 100))

    def roll(self, window):
        """Thực hiện việc tạo hiệu ứng xoay xúc xắc
        
        Parameters:
            window (pygame.Surface): màn hình chính

        Returns:
            None
        """
        # Danh sách chứa các hình ảnh
        images = [self.fire_image, self.water_image, self.ice_image, self.electric_image]
        # Thời điểm bắt đầu
        start_time = time.time()
        # Thời gian giữa mỗi lần hiển thị ảnh (20ms)
        display_duration = 0.02
        # Vị trí của ảnh trong danh sách
        index = 0
        # Vòng lặp cho đến khi đã hiển thị đủ 1 giây
        while time.time() - start_time < 1:
            # Hiển thị ảnh tại vị trí hiện tại
            # Lấy kích thước của màn hình
            screen_width, screen_height = pygame.display.get_surface().get_size()
            window.blit(images[index], ((screen_width - 25) // 2 - 35, (screen_height - 25) // 2 - 50))  # Thay (100, 100) bằng vị trí mong muốn
            pygame.display.update()
            # Chuyển sang ảnh tiếp theo trong danh sách
            index = (index + 1) % len(images)
            # Đợi khoảng thời gian để chuyển đến ảnh tiếp theo
            time.sleep(display_duration)

    def rolling(self):
        """Thực hiện việc xoay xúc xắc ngẫu nhiên
        
        Parameters:
            None
        
        Returns: 
            random_attribute (string): nguyên tố ngẫu nhiên mà xúc xắc xoay được
            self.fire_image (jpg): Hình ảnh nguyên tố hỏa
            self.water_image (jpg): Hình ảnh nguyên tố thủy
            self.ice_image (jpg): Hình ảnh nguyên tố băng
            self.electric_image (jpg): Hình ảnh nguyên tố lôi
        """
        # Chọn ngẫu nhiên một trong các thuộc tính m1, m2, m3, m4
        random_attribute = random.choice([self.m1, self.m2, self.m3, self.m4])
        # Trả về nguyên tố và hình ảnh tượng trưng tương ứng
        if random_attribute == 'Hỏa':
            return random_attribute, self.fire_image
        elif random_attribute == 'Thủy':
            return random_attribute, self.water_image
        elif random_attribute == 'Băng':
            return random_attribute, self.ice_image
        elif random_attribute == 'Lôi':
            return random_attribute, self.electric_image 