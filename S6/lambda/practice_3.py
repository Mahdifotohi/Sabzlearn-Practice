my_dict = [
    {'weight': 50, 'item': 'appel', 'color': 'red'},
    {'weight': 30, 'item': 'benana', 'color': 'yellow'},
    {'weight': 20, 'item': 'grape', 'color': 'purple'},
    {'weight': 40, 'item': 'kivi', 'color': 'green'},
    ]

print((sorted(my_dict, key= lambda x: x['color'])))