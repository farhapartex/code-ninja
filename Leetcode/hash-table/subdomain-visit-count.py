class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        data, res = {}, []
        for domain in cpdomains:
            n, domain = domain.split()
            n = int(n)
            while len(domain) > 0:
                if domain not in data:
                    data[domain] = n
                else:
                    data[domain] += n
                
                domain = ".".join(domain.split(".")[1:])
        
        
        for key, value in data.items():
            res.append("{0} {1}".format(value, key))
        
        
        return res
        