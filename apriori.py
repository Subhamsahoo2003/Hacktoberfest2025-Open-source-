from collections import Counter

def apriori(transactions, min_support):
    
    items = set()
    for transaction in transactions:
        items.update(transaction)
    items = sorted(items)

    
    c1 = Counter()
    for item in items:
        for transaction in transactions:
            if item in transaction:
                c1[item] += 1

    l1 = Counter()
    for item, count in c1.items():
        if count >= min_support:
            l1[frozenset([item])] = count

    frequent_itemsets = dict(l1)
    current_itemsets = l1
    k = 2

    while current_itemsets:
        # Step 3: Generate candidate k-itemsets
        nc = set()
        temp = list(current_itemsets.keys())
        for i in range(len(temp)):
            for j in range(i + 1, len(temp)):
                union = temp[i].union(temp[j])
                if len(union) == k:
                    nc.add(union)

        
        c = Counter()
        for candidate in nc:
            for transaction in transactions:
                if candidate.issubset(transaction):
                    c[candidate] += 1

     
        l = Counter()
        for candidate, count in c.items():
            if count >= min_support:
                l[candidate] = count

        frequent_itemsets.update(l)
        current_itemsets = l
        k += 1

    return frequent_itemsets


transactions = [
    ['milk', 'bread', 'butter'],
    ['bread', 'butter'],
    ['milk', 'butter'],
    ['milk', 'bread'],
    ['bread', 'butter', 'beer']
]

min_support = 2
frequent_itemsets = apriori(transactions, min_support)

print("Frequent Itemsets:")
for itemset, support in frequent_itemsets.items():
    print(f"{set(itemset)}: {support}")
