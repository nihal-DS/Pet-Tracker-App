import pandas as pd
from collections import defaultdict
import pickle
from class_def.mammal import Mammal
from class_def.fish import Fish
from class_def.amphibian import Amphibian
from class_def.owner import Owner
from validation.validate import owner_input, pet_input, mammal_input, fish_input, amphibian_input



def option_one():
    
    '''
    Option 1: Create Pet objects based on the type entered
    '''
    
    run = True
    while run:
        print("-------------")
        print("Type of pet: ")
        print("1. Mammals")
        print("2. Fish")
        print("3. Amphibians")
        
        try:
            type_of_pet = int(input("Enter value between 1 & 3"))
            if (type_of_pet < 1) or (type_of_pet > 3):
                raise ValueError
                
        except ValueError:
            print("ValueError: Please enter a value between 1 & 3")
            
        else:
            
            pet_name, date_of_birth, birth_weight = pet_input()
            
            if type_of_pet == 1:
                owner_name, owner_address = owner_input()
                owner_inst = Owner(owner_name, owner_address)
                litter_size, has_claw = mammal_input()
                pet_inst = Mammal(pet_name, date_of_birth, birth_weight, owner_inst, litter_size, has_claw)
                
            elif type_of_pet == 2:
                owner_name, owner_address = owner_input()
                owner_inst = Owner(owner_name, owner_address)
                scale_condition, length = fish_input()
                pet_inst = Fish(pet_name, date_of_birth, birth_weight, owner_inst, scale_condition, length)
                
            else:
                owner_name, owner_address = owner_input()
                owner_inst = Owner(owner_name, owner_address)
                number_of_limbs, is_venomous = amphibian_input()
                pet_inst = Amphibian(pet_name, date_of_birth, birth_weight, owner_inst, number_of_limbs, is_venomous)
                
            run = False
            
    return pet_inst


def option_two(pet_list):
    
    '''
    Option 2: Compute and print current weight of all pets in the system
    '''
    
    for obj in pet_list:
        print(f"{obj.pet_name}'s current weight in pounds is {obj.compute_weight()}")


def option_three(pet_list):
    
    '''
    Option 3: Print all pet information for every pet in the system
    '''
            
    mammal_df = pd.DataFrame()
    fish_df = pd.DataFrame()
    amphibian_df = pd.DataFrame()

    for idx, obj in enumerate(pet_list):
        
        temp = obj.__dict__.copy()
        temp.update(temp['owner'].__dict__)
        temp.pop('owner')
        
        if obj.__class__.__name__ == 'Mammal':
            tempm_df = pd.DataFrame(temp, index = [idx])
            mammal_df = pd.concat([mammal_df, tempm_df], axis = 0)
            
        elif obj.__class__.__name__ == 'Fish':
            tempaf_df = pd.DataFrame(temp, index = [idx])
            fish_df = pd.concat([fish_df, tempaf_df], axis = 0)
            
        else:
            tempa_df = pd.DataFrame(temp, index = [idx])
            amphibian_df = pd.concat([amphibian_df, tempa_df], axis = 0)
            
    print("===" * 38)
    print("Data of all Mammals in the database")
    print("===" * 38)
    print(mammal_df.to_markdown(index = False))
    print()
    print("===" * 39)
    print("Data of all Fish in the database")
    print("===" * 39)
    print(fish_df.to_markdown(index = False))
    print()
    print("===" * 40 + "=")
    print("Data of all Amphibians in the database")
    print("===" * 40 + "=")
    print(amphibian_df.to_markdown(index = False))


def option_four(pet_list):
    
    '''
    Option 4: Print owner information and pet names for all owners with more than one pet
    '''
    
    track = defaultdict(list)
    for idx, obj in enumerate(pet_list):
        track[obj.owner.owner_name + obj.owner.owner_address].append(idx)
        
    for uniq in track:
        if len(track[uniq]) > 1:
            print(f"{pet_list[track[uniq][0]].owner.owner_name} lives in {pet_list[track[uniq][0]].owner.owner_address} and has {len(track[uniq])} pets.")
            print("The pet names are:")
            for j in track[uniq]:
                print("\t" + pet_list[j].pet_name)


def option_five(pet_list, cursor):
    print("Saving objects to .dat file")
    save = open("pet_trial.dat", "ab")
    for obj in pet_list[cursor:]:
        pickle.dump(obj, save)
    save.close()
    print("Exiting the application...")
    return 