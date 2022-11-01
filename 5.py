def build_profile(first,last):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    return profile

print(build_profile("john","zhu" ))

def make_car(manufacturer,brand):
    return build_profile(manufacturer,brand)

car = make_car('subaru','outback') 
print(car)