def age_assignment(*args, **kwargs):
    dictionary = {}

    for name in args:
        if name not in dictionary:
            dictionary[name] = 0
        for char, age in kwargs.items():
            if name.startswith(char):
                dictionary[name] = age
    return dictionary
        
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
