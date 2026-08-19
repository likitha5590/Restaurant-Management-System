import mysql.connector as db
con=db.connect(user='root',password='My_MySQL_Password',host='localhost',
              database='Restaurant')
print(con.database)
cur=con.cursor()
print('*'*10,'Welcome to Restaurant','*'*10)
while True:
    print('1.Admin')
    print('2.User')
    print('3.Exit')
    ch=int(input('Choose one Option:'))
    if ch==1:
        Adminname='Likitha'
        password='My_Admin_Password'
        id=input('Enter Admin id:')
        if id==Adminname:
            lock=input('Enter your password:')
            if lock==password:
                print('Login successfully')
                while True:
                    print('1.Add Menu')
                    print('2.Delete Menu')
                    print('3.Modify Menu')
                    print('4.View All Orders Details')
                    print('5.Day wise Profit')
                    print('6.Exit')
                    ch=int(input('Choose one option:'))
                    if ch==1:
                        new_item_id=int(input('Enter new item id:'))
                        if new_item_id<=0:
                            print('item id should be grater than 0')
                        else:
                            new_item=input('Enter new item name:')
                            if new_item.strip()=='':
                                print('item cannot be empty')
                            else:
                                new_catogery=input('Enter new catogery:')
                                if new_catogery.strip()=='':
                                    print('catogery cannot be empty')
                                else:
                                    new_price=int(input('Enter price:'))
                                    new_qty=int(input('Enter quantity:'))
                                    new_costprice=int(input('enter cost price:'))
                                    if new_price<=0:
                                        print('price should be greater than 0')
                                    elif new_qty<=0:
                                        print('quantity should be greater than 0')
                                    elif new_costprice<=0:
                                        print('cost price hsould be greater than 0')
                                    else:
                                        cur.execute('select itemid from menu where itemid=%s',(new_item_id,))
                                        data=cur.fetchone()
                                        if data is not None:
                                            print('Item ID already exists')
                                        else:
                                            cur.execute('insert into Menu values(%s,%s,%s,%s,%s,%s)',
                                                (new_item_id,new_item,new_catogery,new_qty,new_price,new_costprice))
                                            con.commit()              
                                            print('Items Added successfully to Menu')
                    elif ch==2:
                        del_item_id=int(input('Enter item id to delete:'))
                        cur.execute('select * from Menu where itemid=%s',(del_item_id,))
                        data=cur.fetchone()
                        if data is not None:
                            cur.execute('delete from menu where itemid=%s',(del_item_id,))
                            con.commit()
                            print('Item deleted successfully from the menu')
                        else:
                            print('item not found in the menu')
                    elif ch==3:
                        item_id=int(input('Enter item id to update:'))
                        cur.execute('select * from menu where itemid=%s',(item_id,))
                        data=cur.fetchone()
                        if data:
                            new_qty=int(input('Enter new quantity:'))
                            new_price=int(input('Enter new price:'))
                            new_costprice=int(input('enter new cost price:'))
                            cur.execute('update Menu set quantity=%s,price=%s,costprice=%s where itemid=%s',
                                        (new_qty,new_price,new_costprice,item_id))
                            con.commit()
                            print('Item updated successfully')
                        else:
                            print('item not found in the menu')
                    elif ch==4:
                        #cur.execute('alter table orders add constraint fk_tab foreign key(orderid)references cart(cartid);')
                         #cur.execute(
                           # '''select orders.orderid, orders.orderdate, 
                           # cart.cartid, cart.itemname, cart.quantity
                            #from orders inner join cart 
                            #on orders.cartid = cart.cartid''')
                         cur.execute('''select orderid,orderdate,cartid,itemname,quantity,price from orders''')
                         data=cur.fetchall()
                         if data:
                             for i in data:
                                print('+---------------------------------------+')
                                print('|             ORDER DETAILS             |')
                                print('+---------------------------------------+')
                                print('|order id    :',i[0])
                                print('|order date  :',i[1].strftime('%y-%m-%d'))
                                print('|cart id     :',i[2])
                                print('|item name   :',i[3])
                                print('|quantity    :',i[4])
                                print('+---------------------------------------+')
                         else:
                             print('no orders available')
                    elif ch==5:
                        date=input('enter date (YYYY-MM-DD):')
                        cur.execute('''select itemname,quantity,price,costprice from orders
                                    where orderdate=%s''',(date,))
                        data=cur.fetchall()
                        if data:
                            total_profit=0
                            print('+-------------------------------------+')
                            print('|            DAY WISE PROFIT          |')
                            print('+-------------------------------------+')
                            for i in data:
                                item_name=i[0]
                                quantity=i[1]
                                price=i[2]
                                costprice=i[3]
                                if costprice is not None:
                                    costprice=int(costprice)
                                    profit=(price - costprice)*quantity
                                    total_profit=total_profit+profit
                                    print('| item name   :',item_name)
                                    print('| quantity    :',quantity)
                                    print('| profit      :',profit)
                                    print('+-------------------------------------+')
                                else:
                                    print('| item name   :',item_name)
                                    print('| quantity    :',quantity)
                                    print('| profit      : cost price not available')
                                    print('+-------------------------------------+')
                            print('|total profit :',total_profit)
                            print('+-------------------------------------+')
                        else:
                            print('no orders found for this date')
                            
                    elif ch==6:
                        break
                    else:
                        print('Invalid option')
            else:
                print('Incorrect Password')
        else:
            print('Incorrect AdminID')
    elif ch==2:
        user_name=input('Enter your name:')
        mobile_num=input('Enter your mobile num:')
        if len(mobile_num)==10 and mobile_num.isdigit() and mobile_num[0]!='0':
            print('name is:',user_name)
            print('mobile number is:',mobile_num)
            cur.execute('insert into user(username,mobilenum) values(%s,%s)',(user_name,mobile_num))
            con.commit()
        else:
            print('incorrect mobile number')
            continue
        while True:
            print('1.View Menu')
            print('2.Add item to cart')
            print('3.Modify cart')
            print('4.Delete item from cart')
            print('5.View cart')
            print('6.Bill')
            print('7.Exit')
            ch=int(input('Choose one option:'))
            if ch==1:
                print('1.All Menu')
                print('2.veg')
                print('3.non_veg')
                print('4.starters')
                print('5.Cool_Drinks')
                print('6.Shakes')
                ch=int(input('choose category:'))
                if ch==1:
                    cur.execute('select * from menu')
                elif ch==2:
                    cur.execute("select * from menu where catogery='veg'")
                elif ch==3:
                    cur.execute("select * from menu where catogery='non_veg'")
                elif ch==4:
                    cur.execute("select * from menu where catogery='starters'")
                elif ch==5:
                    cur.execute("select * from menu where catogery='Cool_Drinks'")
                elif ch==6:
                    cur.execute("select * from menu where catogery='Shakes'")
                else:
                    print('Invalid choice')
                    continue
                data=cur.fetchall()
                if data:
                    for i in data:
                        print(i)
                else:
                    print('no items available in this menu')
            elif ch==2:
                item_name=input('Enter item name:')
                qty=int(input('Enter quantity:'))
                cur.execute('select quantity from menu where itemname=%s',(item_name,))
                data=cur.fetchone()
                if data is None:
                    print('item not found in the menu')
                elif qty<=0:
                    print('enter a valid quantity')
                elif qty>data[0]:
                    print('not enough quantity available')
                else:
                    cur.execute('select cartid,quantity from cart where itemname=%s',(item_name,))
                    cart_data=cur.fetchone()
                    if cart_data is not None:
                        cart_id=cart_data[0]
                        old_qty=cart_data[1]
                        new_qty=old_qty+qty
                        cur.execute('update cart set quantity=%s where cartid=%s',(new_qty,cart_id))
                    else:
                        cur.execute('insert into cart(itemname,quantity) values(%s,%s)',(item_name,qty))
                    cur.execute('update menu set quantity=quantity-%s where itemname=%s',(qty,item_name))
                        #cur.execute('alter table Cart add constraint fk_it foreign key(user_id)references User(uid)')
                    con.commit()
                    print('Item is added successsfully to cart')
            elif ch==3:
                cart_id=int(input('Enter cart_id to modify:'))
                cur.execute('select itemname,quantity from cart where cartid=%s',(cart_id,))
                data=cur.fetchone()
                if data:
                    item_name=data[0]
                    old_qty=data[1]
                    print('1.increase quantity')
                    print('2.decrease quantity')
                    ch=int(input('choose one option:'))
                    if ch==1:
                        qty=int(input('Enter quantity to increase:'))
                        if qty>0:
                            cur.execute('select quantity from menu where itemname=%s',(item_name,))
                            menu_data=cur.fetchone()
                            if qty<=menu_data[0]:
                                cur.execute('update cart set quantity=quantity+%s where cartid=%s',(qty,cart_id))
                                cur.execute('update menu set quantity=quantity-%s where itemname=%s',(qty,item_name))
                                con.commit()
                                print('quantity of an item is increased successfully')
                            else:    
                                print('not enough quantity available in menu')
                        else:
                            print('enter valid quantity')
                    elif ch==2:
                        qty=int(input('enter quantity to decrease:'))
                        if qty>0:
                            if qty<old_qty:
                                cur.execute('update cart set quantity=quantity-%s where cartid=%s',(qty,cart_id))
                                cur.execute('update menu set quantity=quantity+%s where itemname=%s',(qty,item_name))
                                con.commit()
                                print('quantity decreased successfully')
                            elif qty==old_qty:
                                cur.execute('delete from cart where cartid=%s',(cart_id,))
                                cur.execute('update menu set quantity=quantity+%s where itemname=%s',(qty,item_name))
                                con.commit()
                            else:
                                print('you cannot decrease more than cart quantity')
                        else:
                            print('enter valid quantity')
                    else:
                        print('invalid choice')
                else:
                    print('item not found in the cart')
                            
            elif ch==4:
                cart_id=int(input('Enter cartid to delete an item:'))
                cur.execute('select itemname,quantity from cart where cartid=%s',(cart_id,))
                data=cur.fetchone()
                if data:
                    item_name=data[0]
                    cart_qty=data[1]
                    cur.execute('delete from cart where cartid=%s',
                            (cart_id,))
                    cur.execute('update menu set quantity=quantity+%s where itemname=%s',
                                (cart_qty,item_name))
                    con.commit()
                    print('Item is deleted successfully from the cart')
                else:
                    print('item not found in the cart')
            elif ch==5:
                cur.execute('select * from cart')
                data=cur.fetchall()
                if data:
                    for i in data:
                        print(i)
                else:
                    print('cart is empty')
            elif ch==6:
                cur.execute('''select cart.cartid,cart.itemname,cart.quantity,
                            menu.price, menu.costprice from cart
                            inner join menu on cart.itemname=menu.itemname''')
                data=cur.fetchall()
                if data:
                    total=0
                    print('+------------------------------+')
                    print('|              BILL            |')
                    print('+------------------------------+')
                    for i in data:
                        cart_id=i[0]
                        item_name=i[1]
                        quantity=i[2]
                        price=i[3]
                        #costprice=i[4]
                        amount=price*quantity
                        total=total +amount
                        print('| cartID     :',cart_id)
                        print('| item       :',item_name)
                        print('| quantity   :',quantity)
                        print('| price      :',price)
                        print('| amount     :',amount)
                        print('+------------------------------+')
                    print('| total bill :',total)
                    print('+------------------------------+')
                    confirm=input('Do you want to place the order?(yes/no):')
                    if confirm.lower()=='yes':
                        for i in data:
                            cart_id=i[0]
                            item_name=i[1]
                            quantity=i[2]
                            price=i[3]
                            costprice=i[4]
                            cur.execute('insert into orders(orderdate,cartid,itemname,quantity,price,costprice)values(curdate(),%s,%s,%s,%s,%s)',
                                        (cart_id,item_name,quantity,price,costprice))
                        con.commit()
                        print('order placed successfully')
                        cur.execute('delete from cart')
                        con.commit()
                        print('Cart cleared successfully')
                    else:
                        print('order cancelled')
                else:
                    print('cart is empty')
            elif ch==7:
                break
            else:
                print('invalid option')
    elif ch==3:
        break
    else:
        print('invalid option')        
            
cur.close()
con.close()


















 
