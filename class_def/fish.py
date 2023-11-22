from datetime import datetime
from class_def.owner import Owner
from class_def.pet import Pet

class Fish(Pet):
    def __init__(self, pet_name: str, date_of_birth: datetime, birth_weight: float, owner: Owner, scale_condition: str, length: float):
        super().__init__(pet_name, date_of_birth, birth_weight, owner)
        self.scale_condition = scale_condition
        self.length = length
        
    def compute_weight(self):
        days_old = (datetime.now() - self.date_of_birth).days
        growth = 80
        current_weight = self.birth_weight
        while (growth <= 240) and (growth <= days_old):
            current_weight += (0.05 * self.birth_weight)
            growth += 80
        return round(current_weight, 2)
        
    def __str__(self):
        fish_return = "----------\nPet Type: Fish"
        fish_return += super().__str__()
        fish_return += f"\nScale Condition = {self.scale_condition}"
        fish_return += f"\nLength = {self.length}"
        
        return fish_return