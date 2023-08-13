def create_dict():
    dictionary = {}

    entries = int(input("How many entries would you like to input? "))
    for pair in range(entries):
        key = input("Enter a key name: ")
        a = input(f"Is {key} housing a list? ")

        if a == "yes":
            ls = []
            elems = int(input(f"How many elements does '{key}' have? "))

            for e in range(elems):
                val = input(f"Enter a value for '{key}' @ place {e + 1}: ")
                ls.append(val)
            dictionary[key] = ls
                   
			else:
            val = input(f"Enter a value for '{key}': ")
            dictionary[key] = val


    print(dictionary)
    return dictionary

def dict_manipulation():
    current_dict = create_dict()

    print(f"The dictionary currently has the ffg pairs: {current_dict}")
    ans = input("Would like to update any entries? ")

    if ans == "yes":
        key = input("Which key: ")
        val = input(f"What value would you like to enter for '{key}': ")
        current_dict[key] = val

        print(f"Updated dictionary: {current_dict}")
    else:
        ans = input("Would like to delete any pair? ")

        if ans == "yes":
            key = input("Which key: ")
            del current_dict[key]
            print(f"Updated dictionary: {current_dict}")

create_dict()
# dict_manipulation()
