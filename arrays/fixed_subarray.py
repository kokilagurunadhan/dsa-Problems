class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        window_sum=sum(arr[:k])
        ans=0
        if window_sum >=threshold *k:
                ans+=1
        for r in range(k,len(arr)):
            window_sum+=arr[r]
            window_sum-=arr[r-k]
            if window_sum >=threshold *k:
                ans+=1
        return ans

        