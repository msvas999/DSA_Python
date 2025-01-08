class UnionOfArrays:
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        res  = list(set(a + b))

        return len(res)