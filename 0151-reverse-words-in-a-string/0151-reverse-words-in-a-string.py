class Solution:
    def reverseWords(self, s: str) -> str:
        l=0
        r=0
        new=[]
        n=len(s)
        while  l <n:
            if s[l]==" ":
                l+=1
                r+=1
            elif s[l]!=" "  : 
                while r<n and s[r]!=" " :
                    r+=1
                new.append(s[l:r])  
                l=r
        new=new[::-1] 
        
        t=" ".join(new)
        return t        


        
           
          
               



                   
                

        
        
        
        