import random

class Solution:
    """
    [[val,prob]]

    1. Create a list, for each item in the input list, calculate its probability and store as a nested list.


    """

    def __init__(self, w: List[int]):
        self.w = w
        total = sum(self.w)
        for i,ele in enumerate(self.w):
            self.w[i] = [i,ele,ele/total]

    # Randomly picks an index in the w string and return it. Probability: w[i] / sum(w)
    def pickIndex(self) -> int:
        # new_w, total = [], sum(self.w)
        
        # for i,ele in enumerate(self.w):
        #     new_w.append([i,ele,ele/total])

        # Generate a random value based on the probabilities
        random_value = random.choices(self.w, [sublist[2] for sublist in self.w])[0]

        return random_value[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()