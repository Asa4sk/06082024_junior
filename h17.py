import requests

import json

url = "https://dummyjson.com/products?limit=200"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print("Помилка завантаження даних:", response.status_code)
    exit()

techgear_ids = [product["id"] for product in data["products"] if product["brand"] == "TechGear"]
print("ID продуктів бренду TechGear:", techgear_ids)

product_id_135 = next((product for product in data["products"] if product["id"] == 135), None)

if product_id_135:
    image_url = product_id_135["thumbnail"]
    img_response = requests.get(image_url)
    if img_response.status_code == 200:
        with open("phone.png", "wb") as img_file:
            img_file.write(img_response.content)
        print("Картинка збережена як phone.png")
    else:
        print("Не вдалося завантажити картинку:", img_response.status_code)
else:
    print("Продукт із ID 135 не знайдено.")

premium_products = [product for product in data["products"] if product["price"] > 800]
total_value = sum(product["price"] * product["stock"] for product in premium_products)
print("Загальна вартість преміальних товарів:", total_value)
