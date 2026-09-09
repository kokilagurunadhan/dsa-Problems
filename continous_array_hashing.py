class Solution(object):
    def findMaxLength(self, nums):
        b=0
        hm={0:-1}
        ans=0
        for i in range(len(nums)):
            if nums[i]==0:
                b-=1
            else:
                b+=1
            if b in hm:
                ans=max(ans,i-hm[b])
            else:
                hm[b]=i
        return ans