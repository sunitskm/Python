def subset(nums, total):
    subset_helper(nums,total,choices=[])
def subset_helper(nums,total,choices=[]):
    if(total==0):
        print(choices)
    elif(total<0 or len(nums)==0):
        return
    else:
        choices.append(nums[0])
        subset_helper(nums[1:],total-nums[0],choices)
        del choices[-1]
        subset_helper(nums[1:],total,choices)
subset([5,10,12,13,15,18], 30)
