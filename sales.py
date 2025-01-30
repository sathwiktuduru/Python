class customer_details(self):
    def __init__(self,c_id):
        self.c_id=c_id
    
    def first_name(self, name):
        self.name=name
        
    def last_name(self,l_name):
        self.l_name=l_name
    
    def phone(self, phone):
        self.phone=phone
        
    def email_id(self, email):
        self.email=email
        
    def street(self, street_name):
        self.street_name=street_name
        
    def city(self, city_name):
        self.city_name=city_name
        
    def state(self, state_name):
        self.state_name=state_name
    
    def zip_code(self, zipcode):
        self.zipcode=zipcodex
        
class order_details:
    def __init__(self,order_id):
        self.order_id=order_id
    
    def order_status(self,status):
        self.status=status
    def order_date(self, ordered_date):
        self.ordered_date=ordered_date
    def shipped_date(self, ship_date):
        self.ship_date=ship_date
    def store_id(self, storeid):
        self.storeid=storeid

