# Import Library
import datetime

# Store Information
store_name = "Mo's"
store_street = "1 Bond St, London W1 XXX"
store_phone_number = "0900 8742 823"
cashier_name = "Mikel Arteta"

now = datetime.datetime.now()
date_time = now.strftime("%D/ %H:%M:%S")

#Product name and price 
p1_name, p1_price = "A5 Wagyu Beef", 1000
p2_name, p2_price = "Doughnut ", 7.50
p3_name, p3_price = "Tomato ", 12.00
p4_name, p4_price = "Vanilla Sauce", 5.00
p5_name, p5_price = "Apple", 1.99
p6_name, p6_price = "Orange Juice", 3.50
p7_name, p7_price = "Strawberries", 6.99
p8_name, p8_price = "Burger", 20.00
items_sold = 8

#Calculation for sub total
sub_total = p1_price + p2_price + p3_price + p4_price + p5_price + p6_price + p7_price + p8_price

#Calculation for value added tax
vat = (sub_total * 0.2)

#Calculation for total
total = sub_total + vat

#Receipt footer message
message = "Thank you for shopping at Mo's, see you again soon!"

print("*" * 52)
print(f"\t\t\t{store_name.title()}")
print(f"\t     {store_street}")
print(f"\t\t  {store_phone_number}")
print("=" * 52)
print(f"Cashier: {cashier_name}")
print(f"{date_time[3:6] + date_time[0:3] + date_time[6:8]}\t\t\t\t   {date_time[9:]}")
print("=" * 52)
print("PRODUCTS")
print(" ")
print(f"{p1_name.upper()}\t\t\t\t  £{p1_price: ,.2f}")
print(f"{p2_name.upper()}\t\t\t\t      £{p2_price: .2f}")
print(f"{p3_name.upper()}\t\t\t\t\t     £{p3_price: .2f}")
print(f"{p4_name.upper()}\t\t\t\t      £{p4_price: .2f}")
print(f"{p5_name.upper()}\t\t\t\t\t      £{p5_price: .2f}")
print(f"{p6_name.upper()}\t\t\t\t      £{p6_price: .2f}")
print(f"{p7_name.upper()}\t\t\t\t      £{p7_price: .2f}")
print(f"{p8_name.upper()}\t\t\t\t\t     £{p8_price: .2f}")
print(" ")
print("=" * 52)
print(f"Subtotal\t\t\t\t   £{sub_total: .2f}")
print(f"VAT (20%)\t\t\t\t    £{vat: .2f}")
print(f"Total\t\t\t\t\t   £{total: .2f}")
print("=" * 52)
print(" ")
print(f"Total number of items bought \t\t\t   {items_sold}")
print(" ")
print(" ")
print(f" {message}")