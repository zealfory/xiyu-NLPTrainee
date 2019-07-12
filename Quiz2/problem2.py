class Solution:
    def validIPAddress(self, IP: str) -> str:
        ans = ""
        def validIPv4(ip):
            """ 验证IPv4 """
            ans = "IPv4"
            ip_l = ip.split('.')
            if len(ip_l) != 4:
                ans = "Neither"
            else:
                for i in ip_l:
                    if 0 <= len(i) <= 3:
                        for item in i:
                            if item in ('','0','1','2','3','4','5','6','7','8','9'):
                                continue
                            else:
                                ans = "Neither"
                        try:
                            if (len(i) > 0 and i[0] != '0' and int(i) <= 255) or len(i) == 1:
                                continue
                            else:
                                ans = "Neither"
                        except ValueError:
                            ans = "Neither"
                    else:
                        ans = "Neither"
            return ans
        
        def validIPv6(ip):
            """ 验证IPv6 """
            ans = "IPv6"
            ip_l = ip.split(':')
            if len(ip_l) != 8:
                ans = "Neither"
            else:
                for i in ip_l:
                    if 0 < len(i) <= 4:
                        for item in i:
                            if item in ('0','1','2','3','4','5','6','7','8','9',
                                        'a','b','c','d','e','f','A','B','C','D','E','F'):
                                continue
                            else:
                                ans = "Neither"
                    else:
                        ans = "Neither"
            return ans  
        if IP.find('.') != -1:
            ans = validIPv4(IP)
        else:
            ans = validIPv6(IP)
        return ans
            

                        
        
            
            