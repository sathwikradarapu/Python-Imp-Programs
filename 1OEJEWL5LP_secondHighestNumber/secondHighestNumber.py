def second_highest(nums):
    nums=sorted(nums,reverse=True)
    print(nums[1])
nums=list(map(int,input().split(",")))
second_highest(nums)