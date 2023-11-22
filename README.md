# Pet-Tracker-App
Python Object Oriented Programming Practice


Problem Statement:
Create a `Pet Inventory Application` with Inventory Database and an application which performs the following tasks:
- Add a new pet to database
- Compute the current weight of all pets in the database
- Print all pet information for all pets in the inventory
- Print owner information for individuals with multiple pets
- Exit the application


Save all pet objects instatiated on each run and make them available one next run

Create a `Owner` class with the following attributes:
- Name
- Address


Create a `Pet` class with following attributes:
- Name
- Date of birth
- Birth weight
- Owner (class)


Create three child classes of `Pet`:
- Mammals:
  1. Litter size
  2. Has claws
- Fish:
  1. Scale condition (smooth or rough)
  2. Length
- Amphibians:
  1. Number of limbs
  2. Is venomous


All the pet classes must have `comput_weight` method which does calculations based on following rules:
- Mammals: Weight increases by 10% every 60 days for the first 300 days. Weight is constant after that. Assume that the increase occurs on each 60th day only.
- Fish: Weight increases by 5% every 80 days for the first 240 days and then stays constant. Assume that the increase occurs on each 80th day only.
- Amphibians: Weight increases by 5% every 120 days for the first 360 days and then increases by 3% every 120 days. Assume that the increase occurs on each 120th day only.

Also add exception handling for the following cases:
- Date of birth: Valid Date
- Birth Weight: Positive number
- Litter Size: Positive Integer
- hasClaws: User should enter only 'y' or 'n' in either upper or lower case.
- scaleCondition: User should only enter 's' or 'r' in either upper or lower case
- length: Positive integer
- number of limbs: Positive integer
- isVenomous: User should enter only 'y' or 'n' in either upper or lower case.

## Solution: 
### 1. Options:
![1](https://github.com/nihal-DS/Pet-Tracker-App/assets/120628216/247ec60f-765d-46c4-8b6d-492d63aadae5)
### 2. Option 1 - Adding new pet:
![2](https://github.com/nihal-DS/Pet-Tracker-App/assets/120628216/8e8ff725-523f-42b8-b9dc-c2daa711e3da)
### 3. Option 2 - Compute weights:
![3](https://github.com/nihal-DS/Pet-Tracker-App/assets/120628216/a7f8b98e-9770-443a-8b12-84ad47c0ec2a)
### 4. Option 3 - Print database:
![4](https://github.com/nihal-DS/Pet-Tracker-App/assets/120628216/e0589d8b-ae46-49e8-a5ad-2dccf734cc42)
### Option 4 - Find owners with multiple pets:
![5](https://github.com/nihal-DS/Pet-Tracker-App/assets/120628216/94bd0375-153b-4023-8fa6-55ca26c8e4a0)
### Option 5 - Exit application and save to database:
![6](https://github.com/nihal-DS/Pet-Tracker-App/assets/120628216/749f7112-1ec5-4ebe-88a3-a3cba6944a3f)
