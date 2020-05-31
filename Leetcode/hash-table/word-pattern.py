class Solution:
    def wordPattern(self, pattern: str, st: str) -> bool:
        data = {}
        st = st.split()
        if len(pattern) != len(st):
            return False
        for index,p in enumerate(pattern):
            if p not in data:
                if not st[index] in data.values():
                    data[p] = st[index]
                else:
                    return False
            elif data[p] != st[index]:
                return False
        print(data)
        return True