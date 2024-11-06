import requests

url = "https://dummyjson.com/products?limit=200"
response = requests.get(url)
data = response.json()

techgear_products = []
total_value = 0
product_id_to_save = 135

for product in data['products']:
    if product.get('brand') == 'TechGear':
        techgear_products.append(product['id'])

    if product['id'] == product_id_to_save:
        image_url = product['thumbnail']
        img_data = requests.get(image_url).content
        with open('phone.png', 'wb') as handler:
            handler.write(img_data)
        print(f"Image of product with ID {product_id_to_save} saved as phone.png")

    if product['price'] > 800:
        total_value += product['price'] * product['stock']

print("TechGear product ID:", techgear_products)
print(f"Total value of premium products: ${total_value}")
