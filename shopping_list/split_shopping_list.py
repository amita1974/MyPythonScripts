    # (num_prefered, 'item', amount, price_per_unit),
test_shopping_list = [
    [1, 'GAMBA 1KG', 1, 8],
    [1, 'Buns', 5, 14],
    [0, 'Pitot', 2, 12],
    [0, 'Cucambers 2KG', 1, 20],
    [0, 'Sweet Potatos 3KG', 1, 15],
    [0, 'Tuna 3 pcs', 5, 15],
    [0, 'Garlic 3 pcs', 1, 10],
    [1, 'Chicken 2KG', 2, 60],
    [0, 'Onion 6pcs', 1, 10],
    [1, 'Rice', 1, 10],
    [0, 'Marshmelow 3 pcs', 1, 25],
    [0, 'White Cheese', 6, 9],
    [0, 'MIMRACH', 1, 12],
    [0, 'GAVNATZ 400gr.', 3, 20],
    [0, 'גבינה לבנה', 3, 2],
    [1, 'ממרח ריבה', 3, 2],
    [0, 'לאבנה', 12, 2]
]

# (num_prefered, 'item', amount, price_per_unit),
shopping_list1 = [
    [0, 'a', 2, 3],
    [0, 'b', 1, 16],
    [0, 'c', 4, 7],
    [0, 'd', 7, 5],
    [0, 'e', 4, 2],
    [0, 'f', 2, 9],
    [1, 'g', 3, 12],
    [0, 'h', 2, 30],
    [1, 'i', 4, 8],
    [1, 'j', 8, 3],
    [0, 'k', 6, 2]
]

# (num_prefered, 'item', amount, price_per_unit),
real_list = [
    [0, '1 קילו פלפל גמבה', 2, 10],
    [0, '2.5 קילו מלפפונים', 1, 15],
    [0, '3 קילו עגבניות', 1, 14],
    [0, 'כרוב ירוק', 2, 10],
    [1, '1.5 קילו אבוקדו', 1, 20],
    [0, '4 ראשי שום', 1, 10],
    [0, '12 בצל לבן', 1, 13],
    [0, '1 חבילה גזר', 2, 10],
    [1, '6 בטטות לפויקה', 1, 16],
    [1, '500 גרם גרגרי חומוס מושרים במים לאורך לילה (עבור הפויקה)', 2, 5.5],
    [0, '5 חצילים', 1, 16],
    [0, 'פטרוזיליה צרור', 1, 3],
    [1, 'שקית לימונים', 1, 10],
    [0, 'שק תפוחי אדמה', 2, 25],
    [0, '20 לחמניות', 4, 30],
    [0, 'חבילת 10 פיתות', 4, 12],
    [0, 'כיכר לחם', 5, 12],
    [0, '3 טונה', 8, 16],
    [0, '3 מלפפונים חמוצים במלח', 1, 24],
    [0, 'טחינה גולמית 250 גרם', 2, 10],
    [0, 'ממרח שוקולד השחר / נוטלה', 2, 15],
    [0, 'סוכר 1 קג', 1, 7],
    [0, 'מלח דק במלחיה', 1, 3],
    [0, 'מלח גס במגרסה', 1, 6],
    [0, 'תבלינים שונים לבישול ולתיבול סלטים (מלח, פלפל שחור גרוס, פפריקה, כורכום, עלי דפנה)', 1, 10],
    [0, 'לאבנה', 2, 20],
    [0, 'גבינה לבנה 500 גרם', 4, 10],
    [0, 'גבינה למריחה (לא לבנה רגילה)', 5, 12],
    [0, 'גבנצ 400 גרם', 4, 25],
    [1, 'ממרח חומוס 500 גרם', 3, 12],
    [0, '2 מטבוחה', 1, 17],
    [0, 'חלב קרטון', 7, 6],
    [0, 'משקה אורז / סויה', 2, 15],
    [0, '2.5 קג עוף', 2, 88],
    [0, 'תבנית 12 ביצים', 6, 12],
    [0, 'בקבוק שמן זית כ 750 מל', 1, 35],
    [0, 'שמן חמניות או  קנולה', 1, 14],
    [1, 'פשטידה', 4, 25],
    [2, 'פחמימה (פסטה / תפוא / אחר לבחירה (לא אורז))', 6, 16],
    [0, 'אורז מלא (מבושל)', 1, 9],
    [1, 'אורז לבן רגיל (מבושל)', 1, 7],
    [0, 'ירקות מבושלים / אפויים', 2, 22],
    [0, 'תבשיל ללא גלוטן', 1, 25],
    [0, 'קפה נמס', 1, 20],
    [0, 'קפה שחור', 1, 15],
    [0, 'שוקולית', 1, 14],
    [0, 'תה', 1, 15],
    [0, 'עוגה קנויה/ מוכנה', 4, 35],
    [0, 'עוגיות', 3, 15],
    [0, 'קורנפלקס / דומה', 4, 25],
    [0, '3 חבילות מרשמלו', 2, 20],
    [1, 'שיפודים מעץ למרשמלו', 2, 5]
]

#shopping_list = [('apple', 4, 1.5), ('banana', 2, 2.0), ('orange', 3, 1.0), ('grape', 1, 3.0)]

def split_shopping_list(shopping_list, num_families):
    # step 1: check the tatal cost of all prducts, calculate the avg price per family
    total_cost = sum(amount * price for _, _, amount, price in shopping_list)
    avg_cost_per_family = total_cost / num_families
    print (f"total_cost: {total_cost}, avg_cost_per_family: {avg_cost_per_family}, num_families: {num_families}")
    #print (f"עלות כוללת: {total_cost}, עלות ממוצעת למשפחה: {avg_cost_per_family}, מספר משפחות {num_families}")
    # Preperation for next phase:
    # Sort the shopping list from the most expensive price per unit to the least
    # create empty lists of products and total amount each family will pay - init to 0 for all families
    shopping_list.sort(key=lambda x: x[3], reverse=True) # sort by price per unit
    items_per_family = [[] for _ in range(num_families)]
    family_costs = [0] * num_families


    # choose prefered items
    our_family_idx = 0
    for shopping_list_index, item in enumerate(shopping_list):
        for num_prefered, item, amount, price in [item]:
            if num_prefered:
                # Add the item to my family's shopping list and update the cost it will pay
                items_per_family[our_family_idx].append([item, num_prefered, price])
                family_costs[our_family_idx] += price * num_prefered
                # Reduce amount by 1 in shopping list for selected product
                shopping_list[shopping_list_index][2] -= num_prefered

    for _, item, amount, price in shopping_list:
        while amount > 0:
            # Find the family that so far payed less than others and add the next product to this family
            current_selcted_family = min(range(num_families), key=lambda x: family_costs[x])
            item_already_in_family_shopping_list = False
            if len(items_per_family[current_selcted_family]) == 0:
                items_per_family[current_selcted_family].append([item, 1, price])
            else:
                # The selected family has items to buy - check if it already has this specific item.
                # If yes, increment the number of items it should buy by 1. Else add the item to their list.
                for j in range(len(items_per_family[current_selcted_family])):
                    if item == items_per_family[current_selcted_family][j][0]:
                        items_per_family[current_selcted_family][j][1] += 1
                        item_already_in_family_shopping_list = True
                if item_already_in_family_shopping_list == False:
                    items_per_family[current_selcted_family].append([item, 1, price])
            family_costs[current_selcted_family] += price
            amount -= 1

    for family_idx in range(num_families):
        print (f"family {family_idx + 1} will pay {family_costs[family_idx]}")
        #print(f"עלות למשפחה {family_idx + 1}: {family_costs[family_idx]} שח.")
    return items_per_family

#shopping_list = shopping_list1
#shopping_list = test_shopping_list
shopping_list = real_list

num_families = 12
items_per_family = split_shopping_list(shopping_list, num_families)
for i, items in enumerate(items_per_family):
    print(f"Family {i+1} should buy:")
    #print(f"משפחה {i+1} צריכה לקנות:")
    for item, amount, price in items:
        print(f"- {amount} x {item} ({price:.2f} ILS each = {amount * price})")
        #print(f"- {amount} יחידות {item} {price:.2f} שח ליחידה = {amount * price} שח")

print("\n\n\n\n################################################")
print("################################################")
print("################################################")
print("################################################")
print("################################################")

# print the shopping list
for i, items in enumerate(items_per_family):
    #print(f"\nFamily {i+1}:")
    print(f"\nמשפחה {i+1}:")
    for item, amount, _ in items:
        print(f"{amount}\t({item})")
        #print(f"{amount} x ({item})")
