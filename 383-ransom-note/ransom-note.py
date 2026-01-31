class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1=Counter(ransomNote)
        c2=Counter(magazine)
        return not c1-c2