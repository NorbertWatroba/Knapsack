from item import Item
from dynamic import dynamic_knapsack


if __name__ == '__main__':
    with open('input_file.txt') as file:
        knapsack_capacity = int(file.readline().strip())
        items: list[Item] = []
        while line := file.readline():
            items.append(Item(*map(int, line.split())))
        amount_of_items = len(items)

    print(dynamic_knapsack(knapsack_capacity, items))
