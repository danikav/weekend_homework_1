# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, cash):
    cc_pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

def increase_pets_sold(cc_pet_shop, number):
    cc_pet_shop["admin"]["pets_sold"] += number

def get_stock_count(cc_pet_shop):
    return len(cc_pet_shop["pets"])

def get_pets_by_breed(cc_pet_shop, breed):
    pets_by_breed = []
    for pet in cc_pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed

def find_pet_by_name(cc_pet_shop, pet_name):
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(cc_pet_shop, name):
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == name:
            cc_pet_shop["pets"].remove(pet)

def add_pet_to_stock(cc_pet_shop, new_pet):
    cc_pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, number):
    customer["cash"] -= number

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        can_buy_pet = True
    else:
        can_buy_pet = False
    return can_buy_pet

def sell_pet_to_customer(cc_pet_shop, pet, customer):
    customer["pets"].append(pet)
    cc_pet_shop["admin"]["pets_sold"] += 1
    customer["cash"] -= pet["price"]
    cc_pet_shop["admin"]["total_cash"] += pet["price"]

    









