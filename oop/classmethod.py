# class Iphone:
#     def __init__(self,model,year,version):
#         self.model = model
#         self.year = year
#         self.version = version

#     def __str__(self):
#         return f"your {self.model} {self.year} your model release year is {self.version}"

# Iphone1 = Iphone("iphone13","2022","ios18.3.1")
# print(Iphone1.__str__())
# print(Iphone1)
 
# print(type(Iphone1))



class Lenovo:
    def __init__(self,models,spec,size):
        self.models = models
        self.spec = spec
        self.size = size

    def __str__(self):
        return f"your {self.models}is good {self.spec}latest grapihics {self.size}"

Lenovo1 = Lenovo("Lenovo","2025","intel i7")
print(Lenovo1)
# print(Lenovo1.__str__())


