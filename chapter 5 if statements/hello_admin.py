users = ['mugfuio', 'seal', 'mavrit', 'echmil', 'flindt', 'admin']
for user in users:
    if user == 'admin':
        print('Hello Admin, would u like a status report?')
    else:
        print(f"Sup' dawg. How we doing {user.title()}")