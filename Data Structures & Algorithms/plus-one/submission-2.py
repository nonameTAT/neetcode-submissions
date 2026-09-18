class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        acc=1
        for i in range(len(digits)-1,-1,-1):
            if acc==0:
                break
            curr_digit=digits[i]
            curr_digit+=acc
            
            if curr_digit>=10:
                acc=1
                curr_digit=curr_digit-10
            else:
                acc=0
            digits[i]=curr_digit

        if acc==1:
            digits.insert(0,1)
        return digits