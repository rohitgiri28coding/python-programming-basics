# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda fn

#       SYNTAX
#               dictionary = {key: expression for (key, value) in iterable}
#               dictionary = {key: expression for (key, value) in iterable if condition}
#               dictionary = {key: if/else for (key, value) in iterable}
#               dictionary = {key: function(value) for (key, value) in iterable}


temp_in_C = {'New Delhi': 25, 'Patna': 34, 'Jamshedpur': 27, 'Ootacamund': 17, 'Hanumangarh': 35}
print(temp_in_F := {key: str((value*1.8)+32) + 'F' for (key, value) in temp_in_C.items()})
print(temp_in_K := {key: str(value + 273) + 'K' for (key, value) in temp_in_C.items()})


weather = {'New Delhi': 'Barsat', 'Patna': 'dhoop', 'Hyderabad': 'Barsat', 'Gaya': 'dhoop'}
print(sunny_weather := {key: value for (key, value) in weather.items() if value == 'dhoop'})
print(rainy_weather := {key: value for (key, value) in weather.items() if value == 'Barsat'})

print(mausam_ka_haal :=
      {key: "Gand tod garmi" if value > 30 else 'suhana mausam' for (key, value) in temp_in_C.items()})


def check_temp(value):
    if value > 30:
        return 'Gand tod garmi'
    elif 20 < value < 30:
        return 'suhana mausam'
    else:
        return 'Thandu lag rha hai'


print(Mausam_ka_haal := {key: check_temp(value) for (key, value) in temp_in_C.items()})
