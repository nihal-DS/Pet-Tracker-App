from datetime import datetime
from class_def.owner import Owner
from class_def.pet import Pet


class Amphibian(Pet):
    def __init__(self, pet_name: str, date_of_birth: datetime, birth_weight: float, owner: Owner, number_of_limbs: int,
                 is_venomous: str):
        super().__init__(pet_name, date_of_birth, birth_weight, owner)
        self.number_of_limbs = number_of_limbs
        self.is_venomous = is_venomous

    def compute_weight(self):
        days_old = (datetime.now() - self.date_of_birth).days
        growth = 120
        current_weight = self.birth_weight
        while (growth <= 480) and (growth <= days_old):
            if growth <= 360:
                current_weight += (0.05 * self.birth_weight)
            else:
                current_weight += (0.03 * self.birth_weight)
            growth += 120
        return round(current_weight, 2)

    def __str__(self):
        amphibian_return = "----------\nPet Type: Amphibian"
        amphibian_return += super().__str__()
        amphibian_return += f"\nNumber Of Limbs = {self.number_of_limbs}"
        amphibian_return += f"\nIs Venomous = {self.is_venomous}"

        return amphibian_return
