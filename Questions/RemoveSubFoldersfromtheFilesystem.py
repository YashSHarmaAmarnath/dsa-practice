class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        return (q:='_') and [q:=s for s in sorted(folder) if s.find(q+'/')]
