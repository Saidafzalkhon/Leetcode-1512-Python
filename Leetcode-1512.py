nums = list(map(int,input().split()))
son = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            son+=1
print(son)