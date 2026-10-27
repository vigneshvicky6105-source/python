train_name = 'Rajdhani Express'
train_number = 12951
source_station = 'Mumbai'
destination_station = 'Delhi'
ticket_price = 2450.75
print("welcome to Indian Railway Reservation System")
print("Train Name:",train_name)
print("train number:",train_number)
print("source station:",source_station)
print("Destination station:",destination_station)

#float covert to int
ticket_price_int=int(ticket_price)
print(type(ticket_price_int))
print(ticket_price_int)

#int convert to str
train_number_str= str(train_number)
print(type(train_number_str))
print(train_number_str)


#printing railway ticket
passenger_name = 'rahul sharma'
seat_number = 'b2-45'
confirmation_status = 'confirmed'
print("-"*7,"Railway Ticket","-"*7)
print("passenger Name:", passenger_name)
print("seat number:", seat_number)
print("ticket status:",confirmation_status)
print("-"*30)

#budget
print("-"*7,"budget","-"*7)
salary=25000
food=2000
mobile=1000
groceries=3000
dress=1000
eb_bill=1000
fuel=2000
expense=(food+mobile+groceries+dress+eb_bill+fuel)
print("income=",salary)
print("expense=",expense)
print("balance=",salary-expense)
print("-"*22)
