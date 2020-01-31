import requests, json

response = requests.get("https://us-central1-psel-clt-ti-junho-2019.cloudfunctions.net/psel_2019_get")
content = json.loads(response.content)

response_a = []
ids_a = []
response_b = []
response_c = 0

for post in content["posts"]:
 if 'promocao' in post['title']:
        if post['product_id'] not in ids_a:
            response_a.append({'product_id': post['product_id'], 'price_field': post['price']})
            ids_a.append(post['product_id'])
            
if post['likes'] > 700 and post['media'] == 'instagram_cpc' :
        response_b.append({'post_id': post['post_id'], 'price_field': post['price']})
        
if post['date'][3:5] == '05':
        response_c += post['likes']
        
        
response_a = sorted(response_a, key=lambda k: k['product_id'])
response_b = sorted(response_b, key=lambda k: k['post_id'])
