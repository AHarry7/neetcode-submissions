class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        encode strings so the decoder always knows where one string ends 
        and another begins?

        "Hello" → length is 5
        "World" → length is 5

        encoded: "5#Hello5#World"
        """
        
        encStr = ""

        for s in strs:
            encStr += f"{len(s)}#{s}"
        
        return encStr



    def decode(self, s: str) -> List[str]:
        """
        encoded: "5#Hello5#World"
        read till # -> get len -> read that many chars -> next string
        """
        i = 0
        result = []

        while i < len(s):
            j = s.index("#",i)
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            result.append(word)
            i = j + 1 + length
        
        return result









