from yaml import load, Loader

productsStream = open("C:/Users/user/Documents/telegram bot/telegram-webapp-bot-main/webapp-backend/config/products.yml", "r")
products = load(productsStream, Loader=Loader)

def get_product_price(product_id):
    return products[product_id]['price']

def get_delivery_price():
    return 40
