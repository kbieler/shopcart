def go_shopping():
    shop_cart = []
    active = True
    print('Welcome to your shopping cart!') 
    while active:
        print('You may choose from the following:\n A - Add to cart\n B - Review cart\n C - Remove item from cart\n D - Quit\n')
        selection = input('What would you like to do? ')
        if selection.lower() == 'a':
            item = input('What would you like to add to your cart? ')
            shop_cart.append(item)
            
        elif selection.lower() == 'b':
            
            print(shop_cart)
        elif selection.lower() == 'c':
            
            print(shop_cart)
            erase = input('Which item would you like to remove? ')
            shop_cart.remove(erase)
        elif selection.lower() == 'd':
            
            active = False
        else:
            print('\nInvalid input. Please try again. ')
    print(f'Your shopping cart is complete:\n {shop_cart}\n Have a nice day!')

go_shopping()
