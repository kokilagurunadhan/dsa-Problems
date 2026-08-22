class Solution(object):
    def findAnagrams(self, s, p):
        hm1={}
        ans=[]
        for i in p:
            hm1[i]=hm1.get(i,0)+1
        
        hm2={}
        for r in range(len(s)):
            hm2[s[r]]=hm2.get(s[r],0)+1
            if r>=len(p):

                hm2[s[r-len(p)]]-=1
                if hm2[s[r-len(p)]] == 0:
                    del hm2[s[r-len(p)]]
            if hm1==hm2:
                ans.append(r-len(p)+1)
            
                 
        return ans
            




        

        s