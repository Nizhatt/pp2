from itertools import permutations

def get_permutations(s):
    return [''.join(p) for p in permutations(s)]

user_input = input("Введите строку: ")

permutations_list = get_permutations(user_input)

for perm in permutations_list:
    print(perm)