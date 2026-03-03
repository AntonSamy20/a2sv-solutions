class Solution:
    def frequencySort(self, s: str) -> str:
        d ={}
        for ch in s:
            d[ch] = d.get(ch,0) + 1
        
        return "".join(k*v for k,v in sorted(d.items(),key=lambda x:x[1] , reverse=True))



        