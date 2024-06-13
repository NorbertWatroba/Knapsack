from item import Item


def dynamic_knapsack(knapsack_capacity: int, items: list[Item]) -> (int, list[Item]):
    amount_of_items = len(items)

    # creating 1 based matrix for packed items
    matrix = [[0 for _ in range(knapsack_capacity + 1)] for _ in range(amount_of_items + 1)]

    for item in range(1, amount_of_items + 1):
        w, v = items[item - 1].worth, items[item - 1].volume
        for capacity in range(knapsack_capacity + 1):
            if capacity >= items[item - 1].volume:
                matrix[item][capacity] = max(matrix[item - 1][capacity], matrix[item - 1][capacity - v] + w)
            else:
                matrix[item][capacity] = matrix[item - 1][capacity]

    max_worth = matrix[-1][-1]
    packed_items = []

    c = knapsack_capacity
    for item in range(amount_of_items, 0, -1):
        if matrix[item][c] != matrix[item - 1][c]:
            packed_items.append(items[item - 1])
            c -= items[item - 1].volume

    return max_worth, packed_items
