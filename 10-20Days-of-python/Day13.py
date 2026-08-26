class book:
    def __init__(self,book_name):
        self.book_name=book_name

    def display_book(self):
        print(f"{self.book_name}")
    

class book_details:
    def __init__(self,id,author):
        self.id=id
        self.author=author

    def display(self):
        print(f"{self.id}")
        print(f"{self.author}")

class book_price:
    def __init__(self,price):
        self.price=price

    def n_price(self):
        print(f" The book  price is {self.price}")

a=book("Ramayana")
a.display_book()
b=book_details(1,"Chandan")
b.display()
c=book_price(100)
c.n_price()

# class Payment:
#     def pay(self, payment_type):
#         if payment_type == "UPI":
#             print("Payment using UPI")
#         elif payment_type == "Card":
#             print("Payment using Card")
#         elif payment_type == "Cash":
#             print("Payment using Cash")

class payment:
    def payment_type(self):
        pass

class UPI(payment):
    def payment_type(self):
        print("Payment using UPI")
class Card(payment):
    def payment_type(self):
        print("Payment using Card")
class Cash(payment):
    def payment_type(self):
        print("Payment using Cash")
class Paypal(payment):
    def payment_type(self):
        print("Payment using paypal")

a=Paypal()
a.payment_type()

class Notification:
    def send(self, notification_type):
        if notification_type == "email":
            print("Sending Email")
        elif notification_type == "sms":
            print("Sending SMS")

class Notification:
    def send(self):
        pass

class whatsapp(Notification):
    def send(self):
        print("Sending Whatsap sms")
class telegram(Notification):
    def send(self):
        print("Sending Telegram sms")

class Vehicle:
    def start(self):
        print("Vehical starts.")

class car(Vehicle):
    def start(self):
        print("Car started")
class boat(Vehicle):
    def start(self):
        print("Boat started")

def start_vehicle(vehicle):
    vehicle.start()

start_vehicle(car())
start_vehicle(boat())

# DIP Practice: Make a HomeAppliance system where high-level class Remote works with abstract Appliance, and you can pass TV, AC, etc.


class appliance:
    def input_device(self):
        pass
class TV(appliance):
    def input_device(self):
       return "TV is working"
class AC(appliance):
    def input_device(self):
        return "AC is working"

class remote:
    def __init__(self, device: appliance):
        self.device = device

    def get_balance(self):
        return self.device.input_device()


tv=TV()
ac=AC()

r1=remote(tv)
r2=remote(ac)
print(r1.get_balance())
print(r2.get_balance())

try:
    user=int(input("Enter the age:"))
except ValueError:
    print("Invalid input try again.")
else:
    print(f"{100-user} years to reach 100years.")
finally:
    print("Everything worked")

try:
    a=int(input("Enter the frist number:"))
    b=int(input("Enter the second number:"))
except ZeroDivisionError as e:
    print(f"e: The error is {e} ")
except ValueError as e:
    print(f"e: The error is {e} ")
else:
    print(a/b)
finally:
    print("Closing file... (even if error occurred)")

try:
    filename = input("Enter the file name: ")
    file = open(filename, "r")

except FileNotFoundError:
    print("File not found")

else:
    print("File found")
    file.close()

finally:
    print("Program End")


