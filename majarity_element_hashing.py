class Solution(object):
    def majorityElement(self, nums):
        hm={}
        ans=0
        maxcount=0
        for i in nums:
            hm[i]=hm.get(i,0)+1
        for i in nums:
            if hm[i]>maxcount:
                maxcount=hm[i]
                ans=i
            
        return ans
        