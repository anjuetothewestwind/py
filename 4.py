def make_sanwich(*food):
    print('This sanwich has :')
    for i in food:
        print(i)
    print()

make_sanwich('banana')
make_sanwich('ham','pineapple','seafood')

def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

print(build_profile("john","zhu",hometown = "qingyuan",favorite_food = "egg",favorite_book = "SICP" ))

def make_car(manufacturer,brand,**info):
    return build_profile(manufacturer,brand,**info)

car = make_car('subaru','outback',color = "blue",tow_package = True) 
print(car)