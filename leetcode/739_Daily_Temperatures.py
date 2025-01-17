class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """

        Goal: return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.   

        Approach:
        1. Have a right and left index pointer and iterate through the temperatures array from left to right.
        2. Compare each two elements from the left, if the next day is colder, record the difference or put 1 otherwise.
        However, if there is not future warmer days availble by iterating the right index pointer, put a 0 instead.

        Runtime: O(N^2)
        Spacetime: O(N)

        Approach 2:
        1. Iterate and Compare each two elements from the left, if the next day is colder, record the difference or put 1 otherwise.
        2. Check if there is any furture day that is warmer than the current day.

        Runtime: O(N^2)
        Spacetime: O(N)

        Known range and the unknown range

        Record j index value that has an output zero.

        Stack storage and iterate through the array.
        Runtime: O(N)
        Spacetime:O(2N)

        
        """

        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                position = stack.pop()
                res[position] = i - position
            stack.append(i)

        return res



        output, bingo = [], []

        for i in range(len(temperatures)-1):
            if temperatures[i] in bingo: 
                output.append(0)
                continue
            
            if temperatures[i] < temperatures[i+1]:
                output.append(1)
                continue

            j = i+2
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                j += 1

            if j >= len(temperatures):
                output.append(0)
                bingo.append(temperatures[i])
            else:
                output.append(j-i)

        output.append(0)
        return output
