from item import Item
from dynamic import dynamic_knapsack
from brute_force import brute_force


def solution_printer(solution: tuple):
    print(f'Max worth: {solution[0]}')
    print(' Id | Worth | Weight ')
    print('---------------------')
    for item in solution[1]:
        print(f'{item.item_id:^4}|{item.worth:^7}|{item.volume:^8}')


if __name__ == '__main__':
    with open('input_file.txt') as file:
        knapsack_capacity = int(file.readline().strip())
        items: list[Item] = []
        item_id = 0
        while line := file.readline():
            item_id += 1
            items.append(Item(item_id, *map(int, line.split())))
        amount_of_items = len(items)

    print('Dynamic Solution:')
    solution_printer(dynamic_knapsack(knapsack_capacity, items))
    print('Brute Force Solution:')
    solution_printer(brute_force(knapsack_capacity, items))
