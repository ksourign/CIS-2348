#Kaitlyn Sourignosack
#1824497

class ItemToPurchase:
    def __init__ (self, item_name = "none", item_price = 0, item_quantity = 0):

        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
       
    def print_item_cost(self):
        cost = self.item_quantity * self.item_price
        print (self.item_name, self.item_quantity, '@', f'${self.item_price} = ${cost}')
        self.cost = cost

if __name__ == '__main__':

    print ('Item 1')

    item1name = str (input('Enter the item name:'))
    print ()
    item1price = int (input ('Enter the item price:'))
    print ()
    item1quantity= int (input ('Enter the item quantity:'))

    print ()
    print ()

    print ('Item 2')
    item2name = str (input('Enter the item name:'))
    print ()
    item2price = int (input ('Enter the item price:'))
    print ()
    item2quantity= int (input ('Enter the item quantity:'))
    print ()
    print ()

    item1 = ItemToPurchase (item1name, item1price, item1quantity)
    item2 = ItemToPurchase (item2name, item2price,item2quantity)

    print ('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print ()
    print ('Total:', f'${(item1.cost + item2.cost)}')