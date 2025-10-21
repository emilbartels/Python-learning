current_users = ['Mugfuio', 'Seal', 'Mavrit', 'echmil', 'flindt', 'admin']
#her bliver current user lowercase
current_users = [current_user.lower() for current_user in current_users]

new_users = ['mugfuio', 'echmil', 'lebron', 'dwade', 'kobe', 'jordan']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('U need to make a new name')
    else: 
        print('This username is available')
