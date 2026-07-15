class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        if len(strs)==0:
            return []
        newlist=[]
        for i in strs:
            newlist.append("".join(sorted(i)))
        result={}
        for i in range(len(newlist)):
            if newlist[i] not in result:
                result[newlist[i]]=[i]
            else:
                result[newlist[i]].append(i)
        final=[]
        for i in result.values():
            new=[]
            for k in i:
                new.append(strs[k])
            final.append(new)
        return final