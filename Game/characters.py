class character:
    """Lớp mô tả đối tượng nhân vật trong trò chơi"""
    def __init__(self):
        """Hàm khởi tạo
        
        Parameters:
            None

        Returns:
            None"""
        self.name = ''
        self.Atk = 0
        self.Hp = 0
        self.Def = 0
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    def check_name(self, opponent):
        """Kiểm tra tên của nhân vật có trùng với nhân vật hiện tại

        Parameters:
            opponent (character): Nhân vật được so sánh

        Returns:
            bollean(True, False)
        """
        # Kiểm tra tên có trùng không
        if isinstance(opponent, character):
            if self.name == opponent.name:
                return True
            else:
                return False
    def using_element(self, seal):
        """Thực hiện việc sử dụng nguyên tố và áp dụng hiệu ứng tương ứng lên bản thân.
            
        Parameters:
            seal (string): Con dấu được sử dụng

        Return:
            None
        """
        if seal == 'Hỏa':
            # Tăng tấn công bằng 50% tấn công của bản thân
            self.Atk_damaged += self.Atk * 1.5
            int(self.Atk)
            if 'Atk_bonus' in self.effect:
                self.effect['Atk_bonus'] += 0.5
            else:
                self.effect['Atk_bonus'] = 0.5
        elif seal == 'Thủy':
            # Hồi máu bằng 150% tấn công của bản thân
            self.Hp_changes += self.Atk * 1.5
        elif seal == 'Băng':
            # Tăng 50% Hp hiện tại của nhân vật
            self.Hp *= 1.5
        elif seal == 'Lôi':
            # Tăng phòng thủ bằng 50% phòng thủ của bản thân
            self.Def_changed += self.Def * 1.5
            if 'Def_bonus' in self.effect:
                self.effect['Def_bonus'] += 0.5
            else:
                self.effect['Def_bonus'] = 0.5
    def used_element(self, seal):
        """Thực hiện việc sử dụng nguyên tố để chuẩn bị tấn công.
            
        Parameters:
            seal (string): Con dấu được sử dụng

        Return:
            None
        """
        self.Seal = seal
    def elementals_combos(self, seal):
        """Định nghĩa các phản ứng giữa các nguyên tố 
        
        Parameters:
            seal (string): con dấu được đưa vào

        Returns:
            effect (string): Tên phản ứng nguyên tố tương ứng 
        """
        effect = ''
        # Tạo một từ điển để lưu trữ các hiệu ứng phản ứng của các kết hợp nguyên tố
        elemental_effects = {
            ('Hỏa', 'Thủy'): 'Bốc hơi',
            ('Hỏa', 'Băng'): 'Tan chảy',
            ('Hỏa', 'Lôi'): 'Quá tải',
            ('Thủy', 'Băng'): 'Đóng băng',
            ('Thủy', 'Lôi'): 'Điện cảm',
            ('Lôi', 'Băng'): 'Siêu dẫn'
        }
        # Kiểm tra xem có phản ứng nào xảy ra không
        if (self.Seal, seal) in elemental_effects:
            effect = elemental_effects[(self.Seal, seal)]
        return effect
    def attack(self, opponent, seal):
        """Thực hiện hành động tấn công từ nhân vật hiện tại đến đối thủ với con dấu seal.
        
        Parameters:
            opponent (character): đối thủ
            seal (string): con dấu để tấn công
        
        Returns:
            None
        """
        # Thực hiện logic tấn công tại đây
        self.used_element(seal)
        opponent.be_attack(self, seal)   
    def be_attack(self, opponent, seal):
        """Thực hiện phản ứng nguyên tố và tính toán sát thương khi bị tấn công
        
        Parameters:
            opponent (character): đối thủ
            seal (string): con dấu bị gán

        Returns:
            None
        """
        # Tính toán sát thương thực tế nhận được từ đòn tấn công
        if self.Atk_damaged == 0:
            if self.Def_changed == 0:
                if (self.Def < opponent.Atk):
                    self.Hp_changes = -(opponent.Atk - self.Def)
            else:
                if (self.Def_changed < opponent.Atk):
                    self.Hp_changes = -(opponent.Atk - self.Def_changed)
        else:
            if self.Def_changed == 0:
                if (self.Def < opponent.Atk_damaged):
                    self.Hp_changes = -(opponent.Atk_damaged - self.Def)
            else:
                if (self.Def_changed < opponent.Atk_damaged):
                    self.Hp_changes = -(opponent.Atk_damaged - self.Def_changed)
        # Kiểm tra nếu con dấu của nhân vật bị tấn công không phải là None
        if self.Seal is not None:
            effect = self.elementals_combos(seal)  # Kiểm tra xem có phản ứng nào xảy ra không
            # Xử lý các hiệu ứng phản ứng
            if effect == 'Bốc hơi':
                # Giảm 50% chỉ số phòng thủ của nhân vật
                self.Def_changed = self.Def * 0.5
                if 'Def_bonus' in self.effect:
                    self.effect['Def_bonus'] -= 0.5
                else:
                    self.effect['Def_bonus'] = -0.5
            elif effect == 'Tan chảy':
                # Nhân vật phải nhận thêm sát thương bằng 5% sát thương đã nhận
                additional_damage = self.Hp_changes * 0.05
                self.Hp_changes -= additional_damage
            elif effect == 'Quá tải':
                # Phải chịu thêm sát thương nổ bằng 10% sát thương nhân vật đã nhận
                additional_damage = self.Hp_changes * 0.1
                self.Hp_changes -= additional_damage
            elif effect == 'Đóng băng':
                # Giảm 50% Hp hiện tại của nhân vật
                self.Hp *= 0.5
            elif effect == 'Điện cảm':
                # Gây choáng giảm 50% sát thương nhân vật gây ra 
                self.Atk_damaged += self.Atk * 0.5  # Giảm 50% chỉ số tấn công
                if 'Atk_bonus' in self.effect:
                    self.effect['Atk_bonus'] -= 0.5
                else:
                    self.effect['Atk_bonus'] = -0.5
            elif effect == 'Siêu dẫn':
                # Tăng thêm 5% sát thương phải nhận
                additional_damage = self.Hp_changes * 0.05
                self.Hp_changes -= additional_damage
        else:
            self.Seal = seal  # Nếu con dấu hiện tại là None, gán con dấu mới cho nhân vật
    def Hp_changed(self):
        """Hàm xử lý việc thay đổi Hp
        
        Parameters:
            None

        Returns:
            None
        """
        self.Hp = self.Hp + self.Hp_changes
        self.Hp_changes = 0

class furina(character):
    def __init__(self):
        self.name = 'Furina'
        self.Atk = 1101
        self.Hp = 3879
        self.Def = 186
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()

class mostima(character):
    def __init__(self):
        self.name = 'Mostima'
        self.Atk = 834
        self.Hp = 1831
        self.Def = 132
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
class irfit(character):
    def __init__(self):
        self.name = 'Irfit'
        self.Atk = 870
        self.Hp = 1680
        self.Def = 130
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
class ebenholz(character):
    def __init__(self):
        self.name = 'Ebenholz'
        self.Atk = 1400
        self.Hp = 1678
        self.Def = 135
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
   
class goldenglow(character):
    def __init__(self):
        self.name = 'Goldenglow'
        self.Atk = 331
        self.Hp = 1480
        self.Def = 125
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()   
    
class lin(character):
    def __init__(self):
        self.name = 'Lin'
        self.Atk = 849
        self.Hp = 2048
        self.Def = 242
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict() 
    
class eyjafjalla(character):
    def __init__(self):
        self.name = 'Eyjafjalla'
        self.Atk = 645
        self.Hp = 1743
        self.Def = 122
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
        
class mudrock(character):
    def __init__(self):
        self.name = 'Mudrock'
        self.Atk = 882
        self.Hp = 3928
        self.Def = 602
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
class penance(character):
    def __init__(self):
        self.name = 'Penance'
        self.Atk = 875
        self.Hp = 4055
        self.Def = 616
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
       
class horn(character):
    def __init__(self):
        self.name = 'Horn'
        self.Atk = 936
        self.Hp = 3067
        self.Def = 620
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
class saria(character):
    def __init__(self):
        self.name = 'Saria'
        self.Atk = 485
        self.Hp = 3150
        self.Def = 595
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
class hoshiguma(character):
    def __init__(self):
        self.name = 'Hoshiguma'
        self.Atk = 430
        self.Hp = 3850
        self.Def = 723
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
class jessica(character):
    def __init__(self):
        self.name = 'Jessica'
        self.Atk = 522
        self.Hp = 3608
        self.Def = 716
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class gavial(character):
    def __init__(self):
        self.name = 'Gavial'
        self.Atk = 766
        self.Hp = 2906
        self.Def = 391
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class surtr(character):
    def __init__(self):
        self.name = 'Surtr'
        self.Atk = 672
        self.Hp = 2916
        self.Def = 414
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class mountain(character):
    def __init__(self):
        self.name = 'Mountain'
        self.Atk = 587
        self.Hp = 2745
        self.Def = 357
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class nearl(character):
    def __init__(self):
        self.name = 'Nearl'
        self.Atk = 883
        self.Hp = 2698
        self.Def = 295
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class mlynar(character):
    def __init__(self):
        self.name = 'Mlynar'
        self.Atk = 355
        self.Hp = 3906
        self.Def = 502
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class thorns(character):
    def __init__(self):
        self.name = 'Thorns'
        self.Atk = 711
        self.Hp = 2612
        self.Def = 402
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class lappland(character):
    def __init__(self):
        self.name = 'Lappland'
        self.Atk = 685
        self.Hp = 2350
        self.Def = 365
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class nightingale(character):
    def __init__(self):
        self.name = 'Nightingale'
        self.Atk = 350
        self.Hp = 1705
        self.Def = 169
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class reed(character):
    def __init__(self):
        self.name = 'Reed'
        self.Atk = 550
        self.Hp = 1583
        self.Def = 84
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()    
    
class kaltsit(character):
    def __init__(self):
        self.name = 'Kaltsit'
        self.Atk = 490
        self.Hp = 1633
        self.Def = 405
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class warfarin(character):
    def __init__(self):
        self.name = 'Warfarin'
        self.Atk = 505
        self.Hp = 1520
        self.Def = 125
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class lumen(character):
    def __init__(self):
        self.name = 'Lumen'
        self.Atk = 540
        self.Hp = 1825
        self.Def = 111
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class archetto(character):
    def __init__(self):
        self.name = 'Archetto'
        self.Atk = 528
        self.Hp = 1705
        self.Def = 172
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class chen(character):
    def __init__(self):
        self.name = 'Chen'
        self.Atk = 773
        self.Hp = 2501
        self.Def = 203
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class pozemka(character):
    def __init__(self):
        self.name = 'Pozemka'
        self.Atk = 876
        self.Hp = 1802
        self.Def = 193
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class typhon(character):
    def __init__(self):
        self.name = 'Typhon'
        self.Atk = 1045
        self.Hp = 1702
        self.Def = 113
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class gladiia(character):
    def __init__(self):
        self.name = 'Gladiia'
        self.Atk = 801
        self.Hp = 2309
        self.Def = 331
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class skadi(character):
    def __init__(self):
        self.name = 'Skadi'
        self.Atk = 368
        self.Hp = 1603
        self.Def = 233
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()
    
    
class gnosis(character):
    def __init__(self):
        self.name = 'Gnosis'
        self.Atk = 455
        self.Hp = 2035
        self.Def = 132
        self.Atk_damaged = 0
        self.Def_changed = 0
        self.Hp_changes = 0
        self.Seal = None
        self.effect = dict()