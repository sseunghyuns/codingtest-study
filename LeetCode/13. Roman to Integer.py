symbol_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

replace_dict = {
    'IV': 'IIII',
    'IX': 'VIIII',
    'XL': 'XXXX',
    'XC': 'LXXXX',
    'CD': 'CCCC',
    'CM': 'DCCCC'
}

class Solution:
    def romanToInt(self, s: str) -> int:
        # IV: 4 -> IIII
        # IX: 9 -> VIIII
        # XL: 40 -> XXXX
        # XC: 90 -> LXXXX
        # CD: 400 -> CCCC
        # CM: 900 -> DCCCC
        for k,v in replace_dict.items():   
            s = s.replace(k, v)
        
        print(s)
        answer = 0
        for s_ in s:
            answer+= symbol_dict[s_]
        return answer
            