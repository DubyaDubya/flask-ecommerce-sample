class Transaction:
    columns =['index','Transaction_id','customer_id','Date','Product','Gender','Device_Type','Country','State','City','Category','Customer_Login_type','Delivery_Type', 'Quantity' ,'Transaction Start','Transaction_Result',"Amount US$","Individual_Price_US$","Year_Month","Time"]
    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))
