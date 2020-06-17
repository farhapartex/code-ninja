class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split()
        data, res = {}, []
        for txt in text:
            if len(txt) not in data:
                data[len(txt)] = [txt]
            else:
                data[len(txt)].append(txt)
        
        keys = sorted(data.keys())
        for key in keys:
            res.extend(data[key])
        
        return " ".join(res).capitalize()