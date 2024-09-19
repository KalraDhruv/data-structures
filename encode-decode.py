class Solution:

    def encode(self, strs: List[str]) -> str:
        var=""
        for s in strs:
            var += s + ":;"
        return var


    def decode(self, s: str) -> List[str]:
        i =0
        n=0
        collection=[]
        while i < len(s)-1:
            if(s[i]+s[i+1] ==":;"):
                word =""
                while n < i:
                    word+=s[n]
                    n+=1
                collection.append(word)   
                n+=2
            i+=1
        return collection
