class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        allowedcharacs = "abcdefABCDEF"
        def isIpV4(ip):
            address = ip.split('.')
            if len(address) == 4:
                for num in address:
                    if num.isdigit() and 0 <= int(num) <= 255:
                        if num[0] == "0" and len(num) > 1:
                            return False
                    else:
                        return False
                return True
            else:
                return False

        def isIpV6(ip):
            address = ip.split(':')
            if len(address) == 8:
                for hexadeci in address:
                    if not (1 <= len(hexadeci) <= 4):
                        return False
                    for char in hexadeci:
                        if (char.isdigit()) or (char.isalpha() and char in allowedcharacs):
                            continue
                        else:
                            return False
                return True
            else:
                return False
        
        if isIpV4(queryIP):
            return "IPv4"
        elif isIpV6(queryIP):
            return "IPv6"
        else:
            return "Neither"