class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def check_prefix(str1: str, str2: str) -> bool:
            return str2.startswith(str1) and (len(str2) == len(str1) or str2[len(str1)] == '/')

        folder.sort()
        prefixes = []

        for str1 in folder:
            if not prefixes or not check_prefix(prefixes[-1], str1):
                prefixes.append(str1)
    
        return prefixes
        