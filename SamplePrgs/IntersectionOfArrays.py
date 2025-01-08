class Solution:
    #Function to return a list containing the intersection of two arrays.
    def intersection(self, a, b):
        Intersection = []
        i = j = 0
        n = len(a)
        m = len(b)

        while i < n and j < m:
            if a[i] == b[j]:

                if len(Intersection) > 0 and Intersection[-1] == a[i]:
                    i+= 1
                    j+= 1
                else:
                    Intersection.append(a[i])
                    i+= 1
                    j+= 1

            elif a[i] < b[j]:
                i+= 1
            else:
                j+= 1

        return Intersection