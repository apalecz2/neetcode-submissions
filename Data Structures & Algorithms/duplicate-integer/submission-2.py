class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        st = set()

        for n in nums:
            if n in st:
                return True
            else:
                st.add(n)
            
        return False