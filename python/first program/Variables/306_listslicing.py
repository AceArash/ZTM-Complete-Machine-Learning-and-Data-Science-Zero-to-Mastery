# LIST SLICING

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes',
    'tablet',
    'mac'
]
amazon_cart[0] = 'googles'
new_cart = amazon_cart[0:4]
print(amazon_cart)
print(new_cart)
print(amazon_cart[0:3])
print(amazon_cart[1:])
print(amazon_cart[:3])