class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        acc=1
        for i in range(len(digits)-1,-1,-1):
            curr_digit=digits[i]
            curr_digit+=acc
            acc=0
            if curr_digit>=10:
                acc=1
                curr_digit=curr_digit-10
            digits[i]=curr_digit

        if acc==1:
            digits.insert(0,1)
        return digits