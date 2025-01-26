class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        
        Goal: find the longest substring containing the same letter you can get after performing k letter replacements.

        The longest substring length is at least k+1 size.

        Approach:
        Inorder to count the number of each element in the current window => dictionary

        """

        from collections import Counter

        my_dict = {}
        # Create a Counter object from the dictionary
        counter = Counter(my_dict)

        most_common, longest = 0, 0

        for i in range(len(s)):
            counter[s[i]] += 1

            most_common = max(most_common, counter[s[i]])
            if longest - most_common >= k:
                counter[s[i - longest]] -= 1
            else:
                longest += 1

        return longest
