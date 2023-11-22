from datetime import datetime
from class_def.owner import Owner
from class_def.pet import Pet

class Mammal(Pet):
    def __init__(self, pet_name: str, date_of_birth: datetime, birth_weight: float, owner: Owner, litter_size: int, has_claw: str):
        super().__init__(pet_name, date_of_birth, birth_weight, owner)
        self.litter_size = litter_size
        self.has_claw = has_claw
        
    def compute_weight(self):
        days_old = (datetime.now() - self.date_of_birth).days
        growth = 60
        current_weight = self.birth_weight
        while (growth <= 300) and (growth <= days_old):
            current_weight += (0.1 * self.birth_weight)
            growth += 60
        return round(current_weight, 2)
    
    def __str__(self):
        mammal_return = "----------\nPet Type: Mammal"
        mammal_return += super().__str__()
        mammal_return += f"\nLitter Size = {self.litter_size}"
        mammal_return += f"\nHas Claw = {self.has_claw}"
        
        return mammal_return