my_dict = {
    "Ваня" : 2024,
    "Игорь" : 1990
}
print(my_dict)
print(my_dict.get("Ваня"))
print(my_dict.get("asd"))
my_dict.update({'John' : 2000,
                      'Rita' : 1999})
my_dict.pop("Ваня")
print(my_dict)


my_set = {1, 'Яблоко', 42.314, (1, 2, 3)}
print(my_set)
my_set.add("new_str")
my_set.remove((1,2,3))
print(my_set)