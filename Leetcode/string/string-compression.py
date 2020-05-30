class Solution:
    def set_count_value(self, count, chars, index):
        for n in list(str(count)):
            chars.insert(index, n)
            index += 1
        return index
            
    def compress(self, chars: List[str]) -> int:
        curr, count, index = "", 0, 0
        
        while index < len(chars):
            if curr == "":
                curr = chars[index]
                count += 1
                index += 1
            elif curr == chars[index]:
                count += 1
                chars.pop(index)
            elif curr != chars[index]:
                if count > 1:
                    index = self.set_count_value(count, chars, index)
                curr = chars[index]
                count = 1
                index += 1
        
        if count > 1:
            self.set_count_value(count, chars, index)
        
        return len(chars)