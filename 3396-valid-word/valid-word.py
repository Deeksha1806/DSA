class Solution:
    def isValid(self, word: str) -> bool:
        v=0
        c=0
        if(len(word)<3):
            return False
        for i in word:
            if not i.isalnum():
                return False
            
        for i in word:
            if i.isalpha():
                if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or      i=='E' or i=='I' or i=='O' or i=='U'):
                    v+=1
                else:
                    c+=1
        if(v<=0 or c<=0):
            return False
        else:
            return True

                
        

        