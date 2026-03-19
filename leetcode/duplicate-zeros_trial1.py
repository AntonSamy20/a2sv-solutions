class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        index = []
        n = len(arr)

        for i in range(n):
            if arr[i]==0:
                index.append(i)
        for i in reversed(index):
            arr.insert(i+1,0)
            arr.pop()
        
        