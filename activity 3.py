#fruit bill
apple = 240
pinealpple = 150
orange = 100
dragan_fruit = 250

a=input("enter fruit name=")
n=int(input("enter number of kg ="))
if a.lower()=='apple':
    print("price of",a,"=",apple*n)
elif a=='pineapple':
    print("price of",a,"=",pineapple*n)
elif a=='orange':
    print("price of",a,"=",orange*n)
elif a=='dragan_fruit':
    print("price of",a,"=",dragan_fruit*n)
else:
    print("give the proper name and number")

#PERFORM TICKET FARE PRICE
print('-'*7,"TICKET FARE PRICE", '-'*7)
number_of_passengers = 3
ticket_price = 2450
total_fare=number_of_passengers*ticket_price
print("total fare:",total_fare)

#calculate gst on ticket fare
gst_percentage = 5
gst_amount=(total_fare*gst_percentage)/100
print("GST amount:",gst_amount)
final_amount=(total_fare+gst_amount)
print("final payable amount:", final_amount)

#ticket
print("-"*7,"indian railway ticket", '-'*7)
print("passenger name:",)
