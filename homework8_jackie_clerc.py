pizza_orders = ['pepperoni pizza', 'sausage pizza', 'veggie pizza', 'buffalo chicken pizza', 'tikka masala pizza']
finished_pizzas = [ ] 
while pizza_orders:
    current_pizza = pizza_orders.pop()
    print('Your pizza pie is finished!')
    finished_pizzas.append(current_pizza)

for finished_pizzas in finished_pizzas:
    print(f'The pizza ' + finished_pizzas.title() + ' was made.')





