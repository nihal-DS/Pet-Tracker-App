import pickle

def owner_input():
    owner_name = input("Enter owner name: ")
    owner_address = input("Enter owner address: ")
    
    return (owner_name, owner_address)



def pet_input():
    
    pet_name = input("Enter the name of the pet: ")
    
    run = True
    while run:
        try:
            date_of_birth = input("Enter the birth date of the pet in DD-MM-YY format: ")
        except ValueError:
            print("ValueError: Please enter a valid date format")
        else:
            run = False
    
    run = True
    while run:
        try:
            birth_weight = float(input("Enter the weight of the pet at birth (in ounces): "))
            if birth_weight < 0:
                raise ValueError
        except ValueError:
            print("ValueError: Enter a valid weight: ")
        else:
            run = False
            
    return (pet_name, date_of_birth, birth_weight)



def mammal_input():
    
    run = True
    while run:
        try:
            litter_size = int(input("Enter the litter size of the mammal: "))
            if litter_size < 0:
                raise ValueError
        except ValueError:
            print("ValueError: Enter a positive value for litter size")
        else:
            run = False
    
    run = True
    while run:
        try:
            has_claw = input("Does the mammal have claws? (y/n) ")
            if has_claw.lower() not in ('y','n'):
                raise ValueError
        except ValueError:
            print("ValueError: Please enter y or n")
        else:
            run = False
    
    return (litter_size, has_claw)



def fish_input():

    run = True
    while run:
        try:
            scale_condition = input("Does the fish have scales? (s/r) ")
            if scale_condition.lower() not in ('s','r'):
                raise ValueError
        except ValueError:
            print("ValueError: Please enter s or r")
        else:
            run = False
            
    run = True
    while run:
        try:
            length = int(input("Enter the length of the fish: "))
            if length < 0:
                raise ValueError
        except ValueError:
            print("ValueError: Enter a positive value for fish length")
        else:
            run = False
    
    return (scale_condition, length)



def amphibian_input():
    
    run = True
    while run:
        try:
            number_of_limbs = int(input("Enter the number of libs in the amphibian: "))
            if number_of_limbs < 0:
                raise ValueError
        except ValueError:
            print("ValueError: Enter a positive value for number of limbs")
        else:
            run = False
            
    run = True
    while run:
        try:
            is_venomous = input("Is the amphibian venomous? (y/n) ")
            if is_venomous.lower() not in ('y','n'):
                raise ValueError
        except ValueError:
            print("ValueError: Please enter y or n")
        else:
            run = False
            
    return (number_of_limbs, is_venomous)



def read_from_file():
    
    saved_object = []
    
    try:
        objects = open("pet_trial.dat", "rb")
    except FileNotFoundError:
        print("Object file (.dat) not found!")
        return saved_object
    else:
        
        try:
            while True:
                saved_object.append(pickle.load(objects))
        except EOFError:
            objects.close()
            return saved_object