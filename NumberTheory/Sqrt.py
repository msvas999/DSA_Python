class Sqrt:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x
        mid = 0
        res = 0
        while (start <= end):
            mid = start + (end - start) // 2
            if(mid * mid == x):
                res = mid
                return res
            elif(mid * mid > x):
                end  = mid - 1
            else:
                res = mid
                start = mid + 1
        return res
obj = Sqrt()
res = obj.mySqrt(17)
print("Sqrt is ",res)
