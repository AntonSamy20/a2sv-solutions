class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for i in s:
            if i.isalnum():
                lst.append(i.lower())
        i = 0
        j = len(lst)-1
        while i<j:
            if lst[i] != lst[j]:
                return False
            else : 
                i+=1
                j-=1
        return True


        