class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        res=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        keys_d = list(sorted_d.keys())
        for i in range(k):
            res.append(keys_d[i])
        return res
        