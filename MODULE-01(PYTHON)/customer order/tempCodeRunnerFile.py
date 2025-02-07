import random

class customer_details:
    __current_ordersid=[]
    __completed_ordersid=[]
    def _init_(self):
        self.__customer_id = "cus"+str(random.randint(123456789,987654321))
    def set_current_orders(self,items):
        self.__current_ordersid.append(items)
    def get_customer_id(self):
        return self.__customer_id
    def update_order_status(self,order_id):
        if order_id in self.__current_ordersid:
            self.__completed_ordersid.append(order_id)
            self.__current_ordersid.remove(order_id)
        else:
            print("The order id is wrong")
    def get_customer_current_orders(self):
        return self.__current_ordersid
    def get_customer_completed_orderid(self):
        return self.__completed_ordersid
    
class order_details:
    def _init_(self, customer):
        self.__customer_id = customer.get_customer_id()
        self.__order_id = "ref" + str(random.randint(123456789, 987654321))

    def get_order_id(self):
        return self.__order_id

    def get_customer_id(self):
        return self.__customer_id
    
#create 2 customers
def create_new_customer():
    return customer_details()
# customer1=customer_details()
# customer2=customer_details()
def create_new_order(customer):
    temp =order_details(customer)    
    customer.set_current_orders(temp.get_order_id())
    return temp

def main():
    customers_list = []
    orders_list = []
    
    while True:
        print("\n1. Create new customer.")
        print("2. Create new order for customer.")
        print("3. Mark order as delivered.")
        print("4. View customer orders.")
        print("5. Exit")
        
        choice = int(input("Enter the operation you want to perform: "))
        
        if choice == 1:
            new_customer = create_new_customer()
            customers_list.append(new_customer)
            print(f"Customer created with ID: {new_customer.get_customer_id()}")
        
        elif choice == 2:
            customer_id = input("Enter the customer ID: ")
            customer = None
            for cust in customers_list:
                if cust.get_customer_id() == customer_id:
                    customer = cust
                    break
            if customer:
                new_order = create_new_order(customer)  
                orders_list.append(new_order)
                print(f"Order created with ID: {new_order.get_order_id()} for customer {customer_id}")
            else:
                print("Customer not found.")
        
        elif choice == 3:
            order_id = input("Enter the order ID to mark as delivered: ")
            order_found = False
            for order in orders_list:
                if order.get_order_id() == order_id:
                    for customer in customers_list:
                        if customer.get_customer_id() == order.get_customer_id():
                            customer.update_order_status(order_id)
                            print(f"Order {order_id} marked as delivered.")
                            order_found = True
                            break
                    break
            
            if not order_found:
                print("Order ID not found.")
        
        elif choice == 4:
            for customer in customers_list:
                print(f"Customer {customer.get_customer_id()} - Current Orders: {customer.get_customer_current_orders()} Completed Orders: {customer.get_customer_completed_orderid()}")
        
        elif choice == 5:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if _name_ == "_main_":
    main()