class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        maxDiff = 0
        for i in range(len(a)-1):
            for j in range(i+1, len(a)):
                dif = abs(a[i] - a[j])
                if maxDiff <= dif:
                    maxDiff = dif
        Difference.maximumDifference = maxDiff

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)  # doesn't work correctly
