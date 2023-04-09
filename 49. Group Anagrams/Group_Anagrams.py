class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groupedWords = collections.defaultdict(list)
        results = []

        for word in strs:
            groupedWords["".join(sorted(word))].append(word)

        for i in groupedWords.values():
            results.append(i) 
        return results