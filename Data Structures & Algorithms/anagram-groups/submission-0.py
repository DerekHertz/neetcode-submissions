class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            print('count 1: ', count)
            for c in word:
                count[ord(c) - ord('a')] += 1
                print('count 2: ', count)
            res[tuple(count)].append(word)
            print('res', res)

        return list(res.values())



