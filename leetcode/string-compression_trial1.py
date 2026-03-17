class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0 
        w = 0

        while i < len(chars):
            ch = chars[i]
            count = 0 

            while i < len(chars) and chars[i]==ch:
                i+=1
                count+=1
            chars[w] = ch
            w+=1

            if count>1:
                for v in str(count):
                    chars[w] = v
                    w+=1
        return w
                
            

        