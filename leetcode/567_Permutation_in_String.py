class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Goal: Check whether s1 is the permutation of s2.

        Approach:
        1. sort s1, iterate and compare size of s1 window in s2.
        2. Return True if one matches.

        Rutnime: O(2N or (LogN)N) O(N^2)
        Spacetime O(K)

        Dictionary
        [a:1, b:1]
        [e:1, i:1]

        [i:1, d:1]

        [e:1, i:1]
        [i:1, d:1]

        """

        # memo = {}
        # for i in range(len(s1)):
        #     if s1[i] not in memo:
        #         memo[s1[i]] = 1
        #     else:
        #         memo[s1[i]] += 1

        match = True

        for i in range(len(s2)-len(s1)+1):
            temp = s2[i:i+len(s1)]
            for ele in s1:
                if ele not in temp:
                    match = False
                    break

            if match and sorted(s2[i:i+len(s1)]) == sorted(s1): return True
            else: match = True

        return False