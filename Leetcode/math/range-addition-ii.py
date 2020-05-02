class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        m_max, n_max = m, n
        for i in ops:
            m_max = min(m_max,i[0])
            n_max = min(n_max,i[1])
        
        return m_max * n_max
        