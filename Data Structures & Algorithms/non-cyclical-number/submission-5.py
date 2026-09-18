class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            return sum(int(i)*int(i) for i in str(num))
        slow=n
        fast=get_next(n)
        while fast!=1 and fast!=slow:
            fast=get_next(get_next(fast))
            slow=get_next(slow)
        return fast==1