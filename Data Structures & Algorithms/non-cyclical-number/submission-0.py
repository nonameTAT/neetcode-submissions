class Solution:
    def isHappy(self, n: int) -> bool:
        tries=0
        while n != 1:
            temp=n
            n=0
            while temp>0:
                digit=temp%10
                n+=(digit*digit)
                temp=temp//10
            tries+=1
            if tries>1000:
                return False

        return True