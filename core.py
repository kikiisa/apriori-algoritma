from apriori_python import apriori

itemSetList = [['eggs', 'bacon', 'soup'],
                ['eggs', 'banana', 'apple'],
                ['soup', 'banana', 'banana'],
                ['Mangga', 'Banana', 'Rol'],
                ['soup', 'Banana', 'apple'],
                ['soup', 'bacon', 'banana'],
                ]
freqItemSet, rules = apriori(itemSetList, minSup=0.5, minConf=0.5)
# print(freqItemSet)
for(k, v) in freqItemSet.items():
    print(k, v)



    # freqItemSet, rules = apriori(getData, minSup=0.5, minConf=0.5)
        # # print(rules)
        # formatted_response = []
        # for rule in rules:
        #     antecedent, consequent, confidence = rule
        #     formatted_rule = {
        #         'antecedent': list(antecedent),
        #         'consequent': list(consequent),
        #         'confidence': confidence
        #     }
        #     formatted_response.append(formatted_rule)
        #     # print(formatted_response)