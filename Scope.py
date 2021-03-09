class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference
    # Add your code here
    def computeDifference(self):
        maxDiff = 0
        for i in range(len(self.__elements)-1):
            for j in range(i+1, len(self.__elements)):
                dif = self.__elements[i] - self.__elements[j]
                if maxDiff <= dif:
                    maxDiff = dif
        self.maximumDifference = maxDiff

    def maximumDifference(self):
        return self.maximumDifference

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)