my_pizzas = ['diavola', 'calzone', 'margharita']
friends_pizzas = my_pizzas[:]

friends_pizzas.append('kebab')
my_pizzas.append('nutella')

for pizza in my_pizzas:
    print(pizza)
print(f'That was my faveorit pizzas\n')

print('Here is my friends favorit pizzas')
for pizza in friends_pizzas:
    print(pizza)