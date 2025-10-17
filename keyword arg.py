def key(**abc):
    print(abc)
key(a=1,b=2,c=3)



# def print_details(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key:} {value}")
# print_details(name="alice",age="30",city="palakkad")


# def display_name(**abc):
#     return f"name is {abc['name']}and my age is {abc['age']}and my place is{abc['place']}"
# print(display_name(name="john",age=22, place="palakkad"))

# def a(*args,**kwargs):
#     print("string",args)
#     print("num",kwargs)
# print(a(1,2,3,name="john",age="30",place="palakkad"))    
