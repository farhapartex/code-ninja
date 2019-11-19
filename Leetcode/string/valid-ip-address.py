class Solution:
    def is_ipv4(self,str):
        data = str.split(".")
        if len(data) != 4:
            return "Neither"
        for d in data:
            if len(d)>3 or d.startswith('-'):
                return "Neither"
            if d.startswith('0') and len(d)>1:
                return 'Neither'
            try:
                y = int(d)
                if y<0 or y > 255:
                    return "Neither"
            except:
                return "Neither"
        return "IPv4"

    def is_ipv6(self,str):
        data = str.split(":")
        if len(data) != 8:
            return "Neither"
        for d in data:
            if len(d)>4 or d.startswith('-'):
                return "Neither"
            try:
                y = int(d,16)
                if y < 0 or y > 65535:
                    return "Neither"
            except:
                return "Neither"
        return "IPv6"
    
    def validIPAddress(self, IP: str) -> str:
        if "." in IP:
            return self.is_ipv4(IP)
        elif ":" in IP:
            return self.is_ipv6(IP)
        else:
            return "Neither"
        