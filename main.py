from itertools import permutations

with open('data/simplewords.txt', 'r') as file:
    for permutations in file:
        permutations = permutations.strip()

        def permu(data):
            return data == data[::-1]

        display = permu(permutations.strip())

        if display:
            print("this is permutations")
        else:
            print("this is not permutations")