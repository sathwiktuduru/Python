# class order_details:
#     def __init__(self):
#         self.order_id=order_id
#         self.status=status
#         self.ordered_date=ordered_date
#         self.ship_date=ship_date
#         self.storeid=storeid


import random



class Customer:
    def __init__(self, **kwargs):
        self._customer_id = random.randint(1000, 9999)  
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.phone = kwargs.get('phone')
        self.email = kwargs.get('email')
        self.street = kwargs.get('street')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')
        self.zip_code = kwargs.get('zip_code')

    def display_details(self):
        print("\n")
        print("Customer Details")
        print(f'Customer ID: {self._customer_id}')
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Phone: {self.phone}')
        print(f'Email: {self.email}')
        print(f'Street: {self.street}')
        print(f'City: {self.city}')
        print(f'State: {self.state}')
        print(f'Zip Code: {self.zip_code}')




class Orders:
    def __init__(self, customer, **kwargs):
        self._order_id = random.randint(10000, 99999)  
        self.customer = customer  
        self.order_status = kwargs.get('order_status')
        self.order_date = kwargs.get('order_date')
        self.required_date = kwargs.get('required_date')
        self.shipped_date = kwargs.get('shipped_date')
        self.store_id = kwargs.get('store_id')
        self.staff_id = kwargs.get('staff_id')

    def display_order_details(self):
        print("\nOrder Details")
        print(f'Order ID: {self._order_id}')
        print(f'Customer ID: {self.customer._customer_id}')
        print(f'Order Status: {self.order_status}')
        print(f'Order Date: {self.order_date}')
        print(f'Required Date: {self.required_date}')
        print(f'Shipped Date: {self.shipped_date}')
        print(f'Store ID: {self.store_id}')
        print(f'Staff ID: {self.staff_id}')




class OrderItems:
    def __init__(self, order, **kwargs):
        self._item_id = random.randint(100000, 999999)  
        self.order = order  
        self.product_id = kwargs.get('product_id')
        self.quantity = kwargs.get('quantity')
        self.list_price = kwargs.get('list_price')
        self.discount = kwargs.get('discount')

    def display_order_item_details(self):
        print("\nOrder Item Details ")
        print(f'Item ID: {self._item_id}')
        print(f'Order ID: {self.order._order_id}')
        print(f'Customer ID: {self.order.customer._customer_id}')
        print(f'Product ID: {self.product_id}')
        print(f'Quantity: {self.quantity}')
        print(f'List Price: {self.list_price}')
        print(f'Discount: {self.discount}')

    def calculate_total(self):
        total_price = self.quantity * self.list_price
        discounted_price = total_price - (total_price * (self.discount / 100))
        return discounted_price



customer_1 = Customer(
    first_name="Sai",
    last_name="Kumar",
    phone="1234567890",
    email="temp@gmail.com",
    street="ABC Street",
    city="Hyderabad",
    state="Telangana",
    zip_code="500032"
)

order_1 = Orders(
    customer=customer_1, 
    order_status="Processing",
    order_date="2024-01-29",
    required_date="2024-02-05",
    shipped_date="2024-02-02",
    store_id="S123",
    staff_id="ST456"
)

order_item_1 = OrderItems(
    order=order_1,  
    product_id="P001",
    quantity=2,
    list_price=500.00,
    discount=10.00
)

customer_1.display_details()
order_1.display_order_details()
order_item_1.display_order_item_details()

total_price = order_item_1.calculate_total()
print(f"Final Amount Payable (After Discount): ₹{total_price}")