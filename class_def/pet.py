from class_def.owner import Owner
from datetime import datetime


class Pet:
    def __init__(self, pet_name: str, date_of_birth: datetime, birth_weight: float, owner: Owner):
        self.pet_name = pet_name
        self.date_of_birth = date_of_birth
        self.birth_weight = 0.0625 * birth_weight
        self.owner = owner

    def compute_weight(self):
        pass

    def __str__(self):
        date_out = self.date_of_birth.strftime("%d-%m-%y")
        pet_return = f"\nPet Name: {self.pet_name}"
        pet_return += f"\nBirth Date = {date_out}"
        pet_return += f"\nWeight at birth = {self.birth_weight}"
        pet_return += f"\nOwner details: \n{self.owner}"

        return pet_return
