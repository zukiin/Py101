class python_ds:
    def __init__(self) -> None:
        pass

    matrix = []

    def create_matrix(self):
        global matrix
        matrix = []

        rows = int(input("How many rows do you want? "))
        columns = int(input("How many columns do you want? "))

        for r in range(rows):
            row = []
            for c in range(columns):
                x = int(input("Enter a value you'd like to add to the column: "))
                row.append(x)
            matrix.append(row)
        print(f"This is your matrix: {matrix}")


    def list_to_tuple(self):
        tup = tuple(matrix) #basically typecasting
        x = '`'
        
        # unpack the tuple using a for loop
        for i in range(len(tup)):
            x = chr(ord(x) + 1) #ord flips char to ASCII value, and then chr typecasts it back to char
            y = tup[i]
            print(f"{x}: {y}")

        list_comp_tup = [tuple(matrix[m]) for m in range(len(matrix))]

        print(f"Tuple: {tup}\n")
        print(f"New tuple: {list_comp_tup}\n")

        # create a bigger tuple
        tup = tup * 2
        print(f"Extended tuple: {tup}")

    def list_to_dict(self):
        dictionary = dict(matrix)
        print(f"Dictionary: {dictionary}") 



obj = python_ds()
obj.create_matrix()
obj.list_to_tuple()
# obj.list_to_dict()