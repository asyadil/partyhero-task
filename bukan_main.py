
class Character:
    def __init__(self, name, hp, char_type, role, damage_point, is_alive):
        self.name = name
        self.hp = hp
        self.char_type = char_type
        self.role = role
        self.damage_point = damage_point
        self.is_alive = is_alive
        input(f"{self.name} memasuki arena!\n(tekan enter)\n")

    def alive_chek(self):
        if self.hp == 0 or self.hp <= 0:
            self.is_alive = False
            input(f"{self.name} mati konyol karena menerima terlalu banyak luka dalam\n pertempuran ini disebabkan healer tim yang egois dan rekan tempur yang idiot,\n(tekan enter)\n\n")
        return self.is_alive

    def attack(self, hit_obj):
        # - damage validation
        if self.is_alive == False:
            return None
        else:
            return self.damage_point, hit_obj

    def take_damage(self, external_damage):
        print(f"{self.name} menerima damage sebesar {external_damage}")
        self.hp -= external_damage

    def heal(self):
        # - hero mati tidak bisa heal
        if self.is_alive == False:
            return None
        else:
            if self.role == 'healer':
                self.hp += 20
                print(f"{self.name} heal sebesar 20 HP")
                return self.hp