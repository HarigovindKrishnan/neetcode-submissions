class TimeMap:

    def __init__(self):
        self.map1={}
        self.map2={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.map1.get(key) is None:
            self.map1[key]=[]
            self.map2[key]=[]

        self.map1[key].append(value)
        self.map2[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if self.map2.get(key) is None:
            return ""
        l=0
        r=len(self.map2[key])-1
        m=0
        ans=0
        while l<=r:
            m=(l+r)//2
            if self.map2[key][m]<=timestamp:
                ans=m
                l=m+1
                continue
            else:
                r=m-1
        if self.map2[key][ans]<=timestamp:
            return self.map1[key][ans]
        else:
            return ""

        
