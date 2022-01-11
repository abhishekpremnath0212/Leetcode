class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=0
        a=a[::-1]
        b=b[::-1]
        res=""
        for i in range(max(len(a),len(b))):
            x=int(a[i]) if i<len(a) else 0
            y=int(b[i]) if i<len(b) else 0
            val=x+y+c
            char=str(val%2)
            res=char+res
            c=val//2
        if c==1:
            res="1"+res
        return res