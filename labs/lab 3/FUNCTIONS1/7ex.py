def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

user_input = input("Введите массив чисел: ")
nums = list(map(int, user_input.split()))
print(has_33(nums))

