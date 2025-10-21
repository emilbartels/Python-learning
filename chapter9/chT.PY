from random import choices

lotterynumbers = [1, 2, 3, 4]

# Lav en fast billet med 4 tal
my_ticket = tuple(choices(lotterynumbers, k=4))
print("Din billet:", my_ticket)

attempts = 0
while True:
    attempts += 1
    draw = tuple(choices(lotterynumbers, k=4))
    if draw == my_ticket:
        break

print(f"Vandt med træk: {draw}")
print(f"Det tog {attempts} forsøg.")
