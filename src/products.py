import json

# Create jsonl file from json file
with open('data/products.json', 'r') as f:
    data = json.load(f)
with open('data/product.jsonl', 'w') as f:
    if isinstance(data, list):
        for item in data:
            json.dump(item, f)
            f.write('\n')
    else:
        json.dump(data, f)
        f.write('\n')
