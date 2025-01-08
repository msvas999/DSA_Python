class MinMax:
    def get_min_max(self, arr):
        min_ele = arr[0]
        max_ele = arr[0]
        for num in arr:
            if num < min_ele:
                min_ele = num
            if num > max_ele:
                max_ele = num
        return min_ele,max_ele
obj = MinMax()
arr = [1, 345, 234, 21, 56789]
min,max = obj.get_min_max(arr)
print(min,max)