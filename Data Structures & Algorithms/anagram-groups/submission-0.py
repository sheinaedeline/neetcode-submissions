from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort the list in order of length of strings
        sortedList = sorted(strs)
        sortedDict = defaultdict(list)

        for word in sortedList:
            # Make key
            key = "".join(sorted(word))

            # Add word into appropriate key
            if key in sortedDict:
                #print(key, word, sortedDict[key])
                sortedDict[key].append(word)
            # Add key, word to dict
            else:   
                sortedDict[key] = [word]
        
        # Return values of dict
        return list(sortedDict.values())
