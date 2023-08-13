class listcomp:
    def list_of_tups():
        the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        coord_tuple_list = [(x, x**2) for x in the_list]
        print(f"List of coordinates: {coord_tuple_list}")

    list_of_tups()

    def list_flattening():
        vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        new_vector = []

        for x in vec:
            for y in x:
                new_vector.append(y)

        # Alternate representation: List comprehension
        new_vector = [y for x in vec for y in x]

        print(new_vector)

    list_flattening()

    def create_matrix():
        matrix = []
        x = 0
        rows = 4
        columns = 3

        for r in range(rows):
            row = []
            for c in range(columns):
                x += 1
                row.append(x)
            matrix.append(row)
        print(f"First matrix: {matrix}")

        # let's retry the matrix using a list comprehension
        lc_matrix = [[c+1 for c in range(columns)] for r in range(rows)]
        print(f"List comp matrix: {lc_matrix}")

    create_matrix()