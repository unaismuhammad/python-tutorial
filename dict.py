# dict={
#     "name": "jamsheed",
#     "age": "20",
#     "place": "palakkad",
#     "gender": "male",
#     "status": "single",

# }
# print(dict)

# dict={"name":"jamshi",
#       "age":"20",
#       "place":"palakkad",


# }
# print(dict["name"])

# dict={"name":"jamshi",
#       "age":"20",
#       "place":"palakkad",


# }
# print(dict.get("age"))

# my_dict ={"name":"jamshi","age":"20","palce":"palakkad"}
# my_dict["age"]= 31
# print(my_dict)

# my_dict ={"name":"jamshi","age":"20","palce":"palakkad"}
# my_dict["place"]="malappuram"
# print(my_dict)

# nested_dict = {
#     person1 :{"name": "jamshi", "age": "30"},
#     person2 :{"name": "sreenu", "age": "21"}
# }
# print(nested_dict["person1"]["name"])

# my_dict={"name":"jamshi","age":"20"}
# city= my_dict.setdefault("city","thiruvegappura")
# print(city)
# print(my_dict)



my_dict={"name":"jamshi","age":"20"}
my_dict.update({"city":"palakkad","age":"22"})
print(my_dict)

