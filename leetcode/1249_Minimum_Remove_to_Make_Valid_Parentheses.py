class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """

        Goal: return valid string or valid parentheses from the given string s.

        Property:
        - character and valid parentheses should remain in the output

        Easy case:
        If the size of string s is equals to 1, return s if s[0] is a letter, otherwise, return an empty string

        Iteration methods:
        - left to right
        - right to left
        - left and right from the mid point/element
        - left to right and right to left

        Approach 1:
        1. Iterate the string s from left to right, store the open brakets to a list variable.
        2. If a closing braket is found, check if the open brakets list is empty or not, pop the last item from the list if is not empty.
        3. Create a output list to modify output in place.
        4. Keep track of the closing braket positions to perform necessary deletion.

        Approach 2:
        1. Iterate the string s from left and right until they intersect.
        2. Left pos ignore all closing brakets, if it sees a open braket, jump to the right pos.
        3. Right pos ignore all open brakets, if it sees a closing braket, jump to the left pos.
        4. Store all letters to the left or right string variable.
        5. Combine the left and right string to form the final output.

        Runtime: O(N+S^2+C)
        Spacetime: O(2N)

        right: )de)
        lee(t(co
        lee(t(co)de)

        Approach 3:
        1. Iterate left to right, create another 

        lee(t(c)o)de
        
        Approach 4:
        Modify in place, remove (s.replace) the unwanted open or closing braket in the string s.
        1. Iterate the string s from left to right
        2. Modify the string in place
            - store the open braket index into a variable 
            - check open when sees a closing braket, pop the last index from the varible if it is not empty
            Otherwise, replace the closing braket with empty character
        3. Replace all left over indxes in the variable with empty character
        
        Runtime: O(N)
        Spacetime: O(I)

        lee(t(c)o)de)
        index: 

        """

        #Easy case
        #if len(s) == 1: return "" if s == '(' or s == ')' else s

        index_var = []
        i = 0
        
        # Remove the unwanted symbols fron string s
        for c in s:
            if c == '(': index_var.append(i)
            elif c == ')':
                if len(index_var) > 0:
                    index_var.pop()
                else:
                    s = s[:i] + s[i+1:]
                    # s = s.replace(s[i],"")
                    i -= 1
            i+=1
        
        # Remove the extra open brakets that can not make up valid parethesis
        while index_var:
            x = index_var.pop()
            s = s[:x] + s[x+1:]
            # s = s.replace(s[x],"")

        
        return s