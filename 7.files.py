cook_book = {}


with open('recipes.txt', encoding='utf8') as f:
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break
        ingrid_count = f.readline().strip()
        for _ in range(int(ingrid_count)):
            ingrid_list = f.readline().strip().split(" | ")
            if dish_name not in cook_book.keys():
                cook_book[dish_name] = [{'ingredient_name': ingrid_list[0],
                                         'quantity': ingrid_list[1], 'measure': ingrid_list[2]}]
            else:
                cook_book[dish_name].append({'ingredient_name': ingrid_list[0],
                                             'quantity': ingrid_list[1], 'measure': ingrid_list[2]})
        f.readline()


print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    for i in range(len(dishes)):
        for ingrid in cook_book[dishes[i]]:
            if ingrid['ingredient_name'] not in shop_dict.keys():
                shop_dict[ingrid['ingredient_name']] = {'measure': ingrid['measure'],
                                                        'quantity': int(ingrid['quantity']) * int(person_count)}
            else:
                temp_dict = shop_dict.get(ingrid['ingredient_name'])
                temp_dict['quantity'] += (int(ingrid['quantity']) * int(person_count))


    return print(f'Для приготовления {person_count} порций {dishes} необходимо купить:\n{shop_dict}\n')


get_shop_list_by_dishes(['Фахитос', 'Шаурма по-хвостовски'], 1)  # тут отработаны повторящиеся значения
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
