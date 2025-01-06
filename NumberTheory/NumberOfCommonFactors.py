import math
class NumberOfCommonFactors:
    def commonFactors(self, a: int, b: int) -> int:
        gcd_value = math.gcd(a, b)
        return self.count_divisions(gcd_value)

    def count_divisions(self,n: int) -> int:
        count = 0
        for i in range (1, int(n**0.5)+1):
            if n % i == 0:
                if n // i == i:
                    count += 1
                else:
                    count += 2
        return count
obj = NumberOfCommonFactors()
cnt = obj.commonFactors(12,6)
print(cnt)

