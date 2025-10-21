def car_profile(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

car = car_profile('Nissan', 'GTR', color='Blue', spoiler='True')

#printer information om bilen
print('Her er info om din bil:')
for key, value in car.items():
    print(f'{key.title()}: {value}')

print(f'\n{car}')