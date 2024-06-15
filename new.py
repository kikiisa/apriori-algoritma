from apyori import apriori
transactions = [
    ['beer', 'nuts', 'cheese'],
    ['beer', 'cheese', 'milk'],
    ['milk', 'nuts', 'beer'],
    ['milk', 'cheese', 'nuts'],
    ['milk', 'beer', 'nuts']

]
results = list(apriori(transactions))

print(results[0])

for result in results:
    items = result.items
    support = result.support
    print(f"Items: {items}, Support: {support}")

for rule in result.ordered_statistics:
        antecedent = rule.items_base
        consequent = rule.items_add
        confidence = rule.confidence
        lift = rule.lift

        print(f"  Rule: {antecedent} => {consequent}, Confidence: {confidence}, Lift: {lift}")