# class Car:
#     def __init__(self,make,model,year,price):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.price = price

# def display_info(self):
#     return f"{self.year} {self.make} {self.model} -${self.price:,.2f}"

# Car1 =Car("tata","nano","2022","2500")
# print(Car1.make)
# print(Car1.year)


class Iphone:
    def __init__(self,model,year,version):
        self.model = model
        self.year = year
        self.version = version

    def __str__(self):
        return f"your {self.model} battery health is{self.year} your model release year is{self.version}"

Iphone1 = Iphone("iphone13","2022","ios18.3.1")
# print(Iphone1.display_info())
print(Iphone1)
