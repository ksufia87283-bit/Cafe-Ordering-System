print('Welcome to the cofafia Cafe!!')
drinks={
    101:'Espresso:$7',
    102:'Fruit bowl:$5',
    103:'Cappuccino:$7',
    104:'Latte:$8',
    105:'Mocha:$11',
    106:'Hot Chocolate:$3'}
snacks={
    201:'Cheese Sandwich:$10',
    202:'Veg Puff:$8',
    203:'Chicken Roll:$11',
    204:'Garlic bread:$8'}
desserts={
    301:'Chocolate Muffin:$7.67',
    302:'Blueberry Cheesecake:$8.92',
    303:'Brownie with Ice Cream:$4'

}
menu={}
menu.update(drinks)
menu.update(desserts)
menu.update(snacks)
print("\n========== MENU ==========\n")
print(drinks,"\n")
print(snacks,"\n")
print(desserts,"\n")
print("\n========== MENU ==========\n")
cart={}
while True:
    print("choose an action")
    print("1 - Buy")
    print("2 - Change Order")
    print("3 - Add More Items ")
    print("4 - Cancel Order")
    print("5 - Show Order")
    print("6 - Exit\n")
    action=int(input('Choose action: '))
    match action:
        case 1:
            print('Place a new order: ')
            item_code=int(input('Enter the item code what you would like to add in your cart: '))
            if item_code in menu:
                quantity=int(input('How many? '))
                cart[menu[item_code]]=quantity
                print('Sucessfully added!')
                print(cart)
            else:
                print('Out of stock!')
        case 2:
            print('Update your existing order: ')
            item_code=int(input('Enter the item code which you want to update or change: '))
            if menu[item_code] in cart:
                quantity=int(input('How many? '))
                cart[menu[item_code]]=quantity
                print('Sucessfully updated')
                print(cart)
            else:
                print('Item is not found!')
        case 3:
            print('Add more items:')
            item_code=int(input('Enter the item code what you would like to add more to your cart: '))
            if item_code in menu and item_code not in cart:
                quantity=int(input('How many? '))
                cart[menu[item_code]]=quantity
                print('Sucessfully added that items also!')
                print(cart)
        case 4:
            print('Cancel item: ')
            question=str(input('Do you want to cancel a particular item(p) or the full order(f)?' ))
            if question=='p':
                item_code=int(input('What do you want to delete? '))
                if menu[item_code] in cart:
                    cart.pop(menu[item_code])
                    print(menu[item_code],'is sucessfully deleted!')
                    print(cart)
                else:
                    print('Item is not available in the cart.')
            elif question=='f':
                cart.clear()
                print('Succesfully canceled order!')
                print(cart)
            else:
                print('Please select correct option.')

        case 5:
            print('Checking your order')
            total=0
            for menu[item_code],quantity in cart.items():
                item_name,price=menu[item_code].split(":")
                price=float(price.strip().replace('$',''))
                cost=quantity*price
                print(f"{item_name} x {quantity} = ${cost}")
                total=total+cost
            print(f'The total amount is {total}')
        case 6: 
            print('Thanks for visiting Cafafia Cafe!')
            break
        case _:
            print('Please enter a valid action')
    print('Regards Sufia!!')


# 1. Welcome message
# 2. drinks, Snacks and desserts
# 3. Menu creation
# 4. Show Menu 
# 5. Loops 6 cases
# 6. 1 Case - Place a new order
# 7. with Quantity and add in the cart
# 8. 2 Case - Update your existing order and quantity and add in the cart
# 9. 3 Case - add more items with quantity and add in the cart
# 10. 4 Case - Cancel item - (a) Cancel particular thing (b) Cancel full order
# 11. 5 Case - Show Cart with each item prices and total price
# 12. 6 Case - Break 
# 13. Default Case


# 1. Welcome message
print('Welcome to the cofafia Cafe!!')
# 2. drinks, Snacks and desserts
drinks={
    101:'Espresso:$7',
    102:'Fruit bowl:$5',
    103:'Cappuccino:$7',
    104:'Latte:$8',
    105:'Mocha:$11',
    106:'Hot Chocolate:$3'}
snacks={
    201:'Cheese Sandwich:$10',
    202:'Veg Puff:$8',
    203:'Chicken Roll:$11',
    204:'Garlic bread:$8'}
desserts={
    301:'Chocolate Muffin:$7.67',
    302:'Blueberry Cheesecake:$8.92',
    303:'Brownie with Ice Cream:$4'

}
# 3. Menu creation
menu={}
menu.update(drinks)
menu.update(desserts)
menu.update(snacks)
print("\n========== MENU ==========\n")
print(drinks,"\n")
print(snacks,"\n")
print(desserts,"\n")
print("\n========== MENU ==========\n")
# 4. Show Menu
print(menu) 
# 5. Loops 6 cases
cart={}
while True:
        print("choose an action")
        print("1 - Buy")
        print("2 - Change Order")
        print("3 - Add More Items ")
        print("4 - Cancel Order")
        print("5 - Show Order")
        print("6 - Exit\n")
        action=int(input('CHoose an action: '))
        # 6. 1 Case - Place a new order
        match action:
            case 1:
                print('Place a new order')
                # 7. with Quantity and add in the cart
                quantity=int(input('How many?: '))
                cart[item_code]=quantity
                print('Succesfully added!')
                # 8. 2 Case - Update your existing order and quantity and add in the cart
            case 2:
                print('Update your existing order!')
                quantity=int(input('How many?: '))
                cart[menu[item_code]]=quantity
                print('Succesfully updated!')
                # 9. 3 Case - add more items with quantity and add in the cart
            case 3:
                print('Add more items')
                quantity=int(input('How many?: '))
                cart[menu[item_code]]=quantity
                print('Succesfully added!')
                # 10. 4 Case - Cancel item - (a) Cancel particular thing (b) Cancel full order
            case 4:
                print('Cancel order')
                question=str(input('Do you want to cancel an particular order(a) or full order(b)?'))
                if question=='a':
                    item_code=int(input('Which item do you wan to cancel: '))
                    if menu[item_code] in cart:
                        cart.pop(menu[item_code])
                    print('Succesfully canceled!')
                elif question=='b':
                    cart.clear()
                    print(cart)
                else:
                    print('Please try again')
                    # 11. 5 Case - Show Cart with each item prices and total price
            case 5:
                print('Checking your order!')
                total=0
                for menu[item_code],quantity in cart.items():
                    item_name,price=menu[item_code].split(':')
                    price=float(price.strip().replace('$',''))
                    cost=quantity*price
                    print(f'The cost of item {item_name} x {quantity} = {cost}')
                    total=total+cost
                    print(f'The total cost is {total}')
                # 12. 6 Case - Break 
            case 6:
                print('Thanks for comming by!')
                break
            case _:
                print('ENter a valid answer')           
# 13. Default Case









# cart={}
# total=0
# while True:
#     match action:
#         case 1:
#             print('Place a new order:')
#             item_code=int(input('Enter the item code that you want to add in your cart: '))
#             if item_code in menu:
#                 quantity=int(input('How many: '))
#                 cart[item_code]=quantity
#                 print('Succesfully added to cart!')
#             else:
#                 print('This item is out of stock!')
#         case 2:
#             item_code=int(input('Enter the item code that you want to update: '))
#             if item_code in cart:
#                 quantity=int(input('How many: '))
#                 cart[item_code]=quantity
#                 print('Succesfully updated!')
#             else:

#         case 3:
#             item_code=int(input('Enter the item code that you want to add in your cart: '))
#             if item_code in menu and item_code not in cart:
#                 quantity=int(input('How many: '))
#                 cart[item_code]=quantity
#                 print('Succesfully added to cart!')
#             else
#         case 4:
#             question=str(input('Do you want to cancel an partitcular item(p) or full order(t)?: '))
#             if question=='p':
#                 item_code=int(input('Enter the item code that you cancel: '))
#                 if item_code in cart:
#                     cart.pop(item_code)
#             if question=='t':
#                 cart.clear()
#             else:
#         case 5:
#             item_name,price=menu[item_code].split(':')
#             price=float(price.replace('$','').strip())
#             cost=quantity*price
#             print(cost)
#             total=total+cost


            


                
