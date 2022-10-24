#Kaitlyn Sourignosack
#1824497

class ItemToPurchase:
    def __init__ (self, item_name = "none", item_price = 0, item_quantity = 0, item_description = 'none'):

        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        cost = self.item_quantity * self.item_price
        print (self.item_name, self.item_quantity, '@', f'${self.item_price} = ${cost}')
        self.cost = cost

    def print_item_description(self):
        print (f'{self.item_name}: {self.item_description}')

    def get_itemquantity (self):
        return self.item_quantity

    def get_itemcost(self):
        cost = self.item_quantity * self.item_price
        self.cost = cost
        return cost

    def get_itemname(self):
        return self.item_name

    def change_quantity (self,quantity):
        self.item_quantity = quantity




class ShoppingCart:
    def __init__ (self, customer_name = 'none', current_date = 'January 1, 2016', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):
        self.cart_items.append (ItemToPurchase)


    def remove_item(self, ItemToPurchase):
        count = 0
        for i in self.cart_items:
            if i.get_itemname() == ItemToPurchase:
                self.cart_items.remove(i)
                count += 1
            elif i.get_itemname() != ItemToPurchase:
                continue
        if count == 0:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, ItemToPurchase, quantity):
        count = 0
        for i in self.cart_items:
            if i.get_itemname() == ItemToPurchase:
                i.change_quantity(quantity)
                count += 1
            elif i.get_itemname() != ItemToPurchase:
                continue
        if count == 0:
            print('Item not found in cart. Nothing modified.')


    def get_num_items_in_cart(self):
        c = 0
        for i in self.cart_items:
            c += i.get_itemquantity()
        return c

    def get_cost_of_cart(self):
        costofcart = 0
        for i in self.cart_items:
            costofcart += i.get_itemcost()

        return costofcart

    def print_total (self):

        if self.get_num_items_in_cart() == 0:
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print('Number of Items:', self.get_num_items_in_cart())
            print()
            print ("SHOPPING CART IS EMPTY")
            print()
            print (f'Total: ${self.get_cost_of_cart()}')

        else:
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print ('Number of Items:', self.get_num_items_in_cart())
            print ()

            for i in self.cart_items:
                i.print_item_cost()

            print ()
            print (f'Total: ${self.get_cost_of_cart()}')


    def print_descriptions(self):
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print ()
        print ('Item Descriptions')
        for i in self.cart_items:
            i.print_item_description ()



if __name__ == '__main__':
    listofinputs = []
    listofvalidchar = ['a', 'r', 'c', 'i', 'o']

    def print_menu(ShoppingCart):

        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')

        print()

        menu = str (input ('Choose an option:'))
        listofinputs.append (menu)
        print ()
        while menu not in listofvalidchar:
            if menu == 'q':
                break
            menu = str(input('Choose an option:'))
            listofinputs.append (menu)
            print ()

        if menu!= 'q':
            while menu != 'q':

                # a input (add players)
                if menu == 'a':
                    print ('ADD ITEM TO CART')
                    itemname = str(input('Enter the item name:'))
                    print()
                    itemdescription = str(input('Enter the item description:'))
                    print()
                    itemprice = int (input ('Enter the item price:'))
                    print ()
                    itemquantity = int (input ('Enter the item quantity:'))
                    print ()
                    new_item = ItemToPurchase(itemname, itemprice, itemquantity, itemdescription)
                    cart1.add_item (new_item)

                # o input (ROSTER)
                elif menu == 'r':
                    print('REMOVE ITEM FROM CART')
                    itemtoremove = str (input ('Enter name of item to remove:'))
                    print ()
                    cart1.remove_item (itemtoremove)


                # d input (delete jersey num)
                elif menu == 'c':
                    print ('CHANGE ITEM QUANTITY')
                    itemname_changequantity = (str(input('Enter the item name:')))
                    print ()
                    newquantity = (int (input ('Enter the new quantity:')))
                    print ()
                    cart1.modify_item(itemname_changequantity, newquantity)

                elif menu == 'i':
                    print ('OUTPUT ITEMS\' DESCRIPTIONS')
                    cart1.print_descriptions()


                elif menu == 'o':
                    print ('OUTPUT SHOPPING CART')
                    cart1.print_total()


                print()
                print('MENU')
                print('a - Add item to cart')
                print('r - Remove item from cart')
                print('c - Change item quantity')
                print('i - Output items\' descriptions')
                print('o - Output shopping cart')
                print('q - Quit')
                print()
                menu = str(input('Choose an option:'))
                print ()
                listofinputs.append (menu)


    #outside def print_menu() method
    customername = str(input('Enter customer\'s name:'))
    print()
    todaysdate = str(input('Enter today\'s date:'))
    print()
    print()
    cart1 = ShoppingCart(customername, todaysdate)
    print(f'Customer name: {customername}')
    print(f'Today\'s date: {todaysdate}')

    print()

    print_menu(cart1)


