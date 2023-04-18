
def split_shopping_list(shopping_list, num_families):
    total_cost = sum(amount * price for _, amount, price in shopping_list)
    avg_cost_per_family = total_cost / num_families
    print (f"total_cost: {total_cost}, avg_cost_per_family: {avg_cost_per_family}, num_families: {num_families}")
    #print (f"עלות כוללת: {total_cost}, עלות ממוצעת למשפחה: {avg_cost_per_family}, מספר משפחות {num_families}")
    shopping_list.sort(key=lambda x: x[2]/x[1], reverse=True) # sort by price/amount ratio
    items_per_family = [[] for _ in range(num_families)]
    family_costs = [0] * num_families


    for item, amount, price in shopping_list:
        while amount > 0:
            best_family = min(range(num_families), key=lambda x: family_costs[x])
            found = False
            if len(items_per_family[best_family]) == 0:
                items_per_family[best_family].append([item, 1, price])
            else:
                for j in range(len(items_per_family[best_family])):
                    if item == items_per_family[best_family][j][0]:
                        items_per_family[best_family][j][1] += 1
                        found = True
                if found == False:
                    items_per_family[best_family].append([item, 1, price])
            family_costs[best_family] += price
            amount -= 1

    for family_idx in range(num_families):
        print (f"family {family_idx} will pay {family_costs[family_idx]}")
        #print(f"עלות למשפחה {family_idx + 1}: {family_costs[family_idx]} שח.")
    return items_per_family


    # ('item', amount, price_per_unit),
test_shopping_list = [
    ('GAMBA 1KG', 1, 8),
    ('Buns', 5, 14),
    ('Pitot', 2, 12),
    ('Cucambers 2KG', 1, 20),
    ('Sweet Potatos 3KG', 1, 15),
    ('Tuna 3 pcs', 5, 15),
    ('Garlic 3 pcs', 1, 10),
    ('Chicken 2KG', 2, 60),
    ('Onion 6pcs', 1, 10),
    ('Rice', 1, 10),
    ('Marshmelow 3 pcs', 1, 25),
    ('White Cheese', 6, 9),
    ('MIMRACH', 1, 12),
    ('GAVNATZ 400gr.', 3, 20),
    ('גבינה לבנה', 3, 2),
    ('ממרח ריבה', 3, 2),
    ('לאבנה', 12, 2)
]

# ('item', amount, price_per_unit),
shopping_list1 = [
    ['a', 2, 3],
    ['b', 1, 16],
    ['c', 4, 7],
    ['d', 7, 5],
    ['e', 4, 2],
    ['f', 2, 9],
    ['g', 3, 12],
    ['h', 2, 30],
    ['i', 4, 8],
    ['j', 8, 3],
    ['k', 6, 2]
]

#shopping_list = [('apple', 4, 1.5), ('banana', 2, 2.0), ('orange', 3, 1.0), ('grape', 1, 3.0)]
#shopping_list = shopping_list1
shopping_list = test_shopping_list

num_families = 6
items_per_family = split_shopping_list(shopping_list, num_families)
for i, items in enumerate(items_per_family):
    print(f"Family {i+1} should buy:")
    #print(f"משפחה {i+1} צריכה לקנות:")
    for item, amount, price in items:
        print(f"- {amount} x {item} ({price:.2f} ILS each = {amount * price}")
        #print(f"- {amount} יחידות {item} {price:.2f} שח ליחידה = {amount * price} שח")

