import random
shopping_cart = {'eggs', 'flour', 'apples', 'milk'}
print ('-' * 50)
print('Shopping cart: ')
print('-' * 50)
for items in shopping_cart:
   print(items)
print('-' * 50)
while True:
   number = int(input( '''   1.Add more items in the cart
   2.Remove items from cart
   3.View items in cart
   4.Calculate the price
   5.Exit
--------------------------------------------------   
Enter the number of the function you would like to do: \n'''))

   if number == 1:
      item_add = input('Please enter the items you want to add. Only one at a time: \n').lower()
      shopping_cart.add(item_add)
      print('Updated shopping cart: ')
      print ('-' * 50)
      for item in shopping_cart:
         print(item)
      print ('-' * 50)
      print('Items have been successfully added to cart')
      print('-' * 50)


   elif number == 2:
      item = input('Please enter the items you want to remove. Only one at a time: \n').lower()

      if item in shopping_cart:
        shopping_cart.remove(item)
        print('Updated shopping cart')
        print('-' * 50)
        for items in shopping_cart:
           print(items)
        print('-' * 50)
        print('Item has been successfully removed from the cart')
        print('-' * 50)

      else:
          print('Sorry this item does not exist in your cart')
          print('-' * 50)

   elif number == 3:
      print('Shopping cart')
      print('-' * 50)
      for items in shopping_cart:
         print(items)
      print('-' * 50)

   elif number == 4:
       number_of_items = len(shopping_cart)
       print('There are', number_of_items, 'items in the shopping cart.')
       if number_of_items <= 5:
           cost = random.randint(3,15)
           print(f'Please proceed to PayPal and pay {cost} USD.')
           print('-' * 50)
       elif number_of_items > 5 or number_of_items < 15:
           cost = random.randint(15,50)
           print(f'Please proceed to PayPal and Pay {cost} USD.')
           print('-' * 50)
       elif number_of_items > 15 or number_of_items <= 50:
           cost = random.randint(50,200)
           print(f'Please proceed to PayPal and pay {cost} USD.')
           print('-' * 50)
       else:
           print("Sorry we cannot process orders over 50 items.")
           print('-' * 50)
   elif number == 5:
      print("Exiting the shop!!!")
      break
   else:
       print("Invalid number!!")


