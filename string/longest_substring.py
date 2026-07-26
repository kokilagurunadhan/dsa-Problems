class Solution(object):
    def lengthOfLongestSubstring(self, s):
       l=0
       hash_map={}
       max_len=0
       for r in range(len(s)):
        if(s[r] in hash_map):
            l=max(l,hash_map[s[r]]+1)
        hash_map[s[r]]=r
        max_len=max(max_len,r-l+1)
       return max_len
