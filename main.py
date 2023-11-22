from validation.validate import read_from_file
from app.options import option_one, option_two, option_three, option_four, option_five
from class_def.mammal import Mammal
from class_def.fish import Fish
from class_def.amphibian import Amphibian
from class_def.owner import Owner

def menu_options():
    
    pet_list = read_from_file()
    pet_count_cursor = len(pet_list)
    
    run = True
    while run:
        print("---------------------------------")
        print("Select an option between 1 and 5: ")
        print("1. Add a new pet")
        print("2. Print current weight of all pets in the system")
        print("3. Print all pet information for all pets in the system")
        print("4. Information of all owners with more than one pet")
        print("5. Exit the application")
        
        try:
            option = int(input("Enter your option: "))
            if (option < 1) or (option > 5):
                raise ValueError
                
        except ValueError:
            print("ValueError: Plese select an option between 1 & 5")
            
        else:
            if option == 1:
                print("Option selected: 1")
                pet_list.append(option_one())
                
            elif option == 2:
                print("Option selected: 2")
                option_two(pet_list)
                
            elif option == 3:
                print("Option selected: 3")
                option_three(pet_list)
                
            elif option == 4:
                print("Option selected: 4")
                option_four(pet_list)
                
            else:
                print("Option selected: 5")
                option_five(pet_list, pet_count_cursor)
                run = False



if __name__ == "__main__":
    menu_options()