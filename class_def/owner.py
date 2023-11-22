class Owner:
    def __init__(self, owner_name: str, owner_address: str):
        self.owner_name = owner_name
        self.owner_address = owner_address
    
    def __str__(self):
        return f"   Owner Name: {self.owner_name}\n   Owner Address: {self.owner_address}"