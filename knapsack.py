"""
Items: [ { "weight": 5, "value": 10 }, { "weight": 4, "value": 40 }, { "weight": 6, "value": 30 }, { "weight": 4, "value": 50 } ]
Knapsack Limit: 10
"""
items = [ { "weight": 5, "value": 10 }, { "weight": 4, "value": 40 }, { "weight": 6, "value": 30 }, { "weight": 4, "value": 50 } ]
limit = 10

def bountiful_loot(limit, items):
    n = len(items)
    table = [[0 for x in range(n+1)] for y in range(limit+1)]
    # print(table)

    for i in range(n-1, -1, -1):
        for j in range(1, limit+1):
            if items[i]["weight"] <= j:
                # print(items[i]["value"], table[j-items[i]["weight"]][i+1],  table[j][i+1])
                table[j][i] = max(items[i]["value"] + table[j-items[i]["weight"]][i+1], table[j][i+1])
            else:
                table[j][i] = table[j][i+1]
    # print(table[limit])
    return table[limit][0]

bountiful_loot(limit, items)

