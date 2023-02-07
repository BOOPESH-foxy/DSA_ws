
def containsDup(nums):
    return not len(nums) == len(set(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
num2 = [1,2,3,4]
value = containsDup(nums)
value2 = containsDup(num2)
print(value,"\n",value2)