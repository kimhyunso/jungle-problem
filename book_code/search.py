def seq_search_while(nums, key):
    index = 0
    while True:
        if nums[index] == key:
            return 1
        if len(nums) == index:
            return -1
        index += 1

def seq_search_for(nums, key):
    for i in range(len(nums)):
        if nums[i] == key:
            return 1
        if len(nums) == i:
            return -1





