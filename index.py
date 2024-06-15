from flask import Flask,request,jsonify
app = Flask(__name__)
# from apriori_python import apriori
from apyori import apriori
@app.route("/",methods=["GET","POST"])
def hello_world():
    if(request.method == "POST"):
        try:
            data = request.json.get("data")
            results = list(apriori(data))
            print(results)
            response_data = {"frequent_itemsets": [], "association_rules": []}
            for result in results:
                frequent_itemset = {"items": list(result.items), "support": result.support}
                response_data["frequent_itemsets"].append(frequent_itemset)
                for rule in result.ordered_statistics:
                    association_rule = {
                        "antecedent": list(rule.items_base),
                        "consequent": list(rule.items_add),
                        "confidence": rule.confidence,
                        "lift": rule.lift
                    }
                    response_data["association_rules"].append(association_rule)

            return jsonify(response_data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({
            "message":"this method get"
        })

if __name__ == "__main__":
    app.run(port=3000,debug=True)
