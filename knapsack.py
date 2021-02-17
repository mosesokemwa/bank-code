"""
Items: [ { "weight": 5, "value": 10 }, { "weight": 4, "value": 40 }, { "weight": 6, "value": 30 }, { "weight": 4, "value": 50 } ]
Knapsack Limit: 10
"""
import json

def bountiful_loot(limit, items):
    n = len(items)
    table = [[0 for x in range(n+1)] for y in range(limit+1)]

    for i in range(n-1, -1, -1):
        for j in range(1, limit+1):
            if items[i]["weight"] <= j:
                table[j][i] = max(items[i]["value"] + table[j-items[i]["weight"]][i+1], table[j][i+1])
            else:
                table[j][i] = table[j][i+1]
    return table[limit][0]


if __name__ == '__main__':
    weights = input('List of Knapsack weights: ')
    limit = input('Knapsack Limit: ')
    items = json.loads(weights)
    s = bountiful_loot(int(limit), items)
    print(f'Knapsack value: {s}')

