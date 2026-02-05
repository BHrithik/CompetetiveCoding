class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = {}
        # actually a thing i have been thinking about for a long time
        def convert_str_int(word):
            sum = ""
            items = sorted(Counter(word).items())
            for key,value in items:
                sum += chr(value)+key
            return sum

        for word in strs:
            str_key = convert_str_int(word)
            if str_key not in new_dict:
                new_dict[str_key] = []
            new_dict[str_key].append(word)
        return list(new_dict.values())