from typing import List
class BinarySearch:
    def mySearch(self,nums:List[int],target:int):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

nums = [1,2,3,4,5,6,7,8,9]
target = 10
obj = BinarySearch()
res = obj.mySearch(nums,target)
print(target," element found at index ",res)



