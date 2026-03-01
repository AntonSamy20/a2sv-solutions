class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output = []
        arr2_set = set(arr2)
        st = [x for x in arr1 if x not in arr2_set]
        st.sort()

        for i in arr2:
            for j in arr1:
                if j==i:
                    output.append(i)
        return output+st
            

        