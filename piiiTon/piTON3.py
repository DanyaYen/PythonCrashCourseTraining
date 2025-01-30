from piTON2 import *
def car_info(model, year, **other):
    other[model] = model
    other[year] = year
    return other
car = car_info('subaru', 3000 , color='blue', tow_package=True)
print(car)
show_messages(car)