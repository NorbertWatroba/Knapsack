from item import Item


def brute_force(knapsack_capacity: int, items: list[Item]):
    amount_of_items = len(items)
    max_worth = 0
    solution = []

    for i in range(1, 2**amount_of_items):
        binary = bin(i)[2:].zfill(amount_of_items)
        packed = [int(bit) for bit in binary]
        packed_volume = sum(items[k].volume for k in range(amount_of_items) if packed[k] == 1)
        if packed_volume <= knapsack_capacity:
            packed_worth = sum(items[k].worth for k in range(amount_of_items) if packed[k] == 1)
            if packed_worth > max_worth:
                max_worth = packed_worth
                solution = packed

    solution = [items[i] for i in range(amount_of_items) if solution[i] == 1]

    return max_worth, solution
