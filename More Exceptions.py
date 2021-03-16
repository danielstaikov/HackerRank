#Write your code here
class Calculator:

    def power(self, number, power):
        result = 1
        if number >= 0 and power >= 0:
            for i in range(power):
                result = result*number
            return result
        else:
            raise TypeError("n and p should be non-negative")


myCalculator = Calculator()
T=int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
