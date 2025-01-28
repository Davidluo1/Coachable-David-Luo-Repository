class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """

        Goal: return all combinations of well-formed parethenses of n paris.

        Known:
        - Input N
        - Parethenses "()"

        Must have:
        - All open bracket with all close bracket
        - One parentheses covers all other parentheses
        - All single parentheses
        
        Always checks its opposite sturcture
        Add to the output if it is not in the output.

        Recursion calls

        Runtime: O(N^2)
        Spacetime: O(N^2)

        """


        def dfs(open_b, close_b, cur_s):
            if open_b >= close_b >= n:
                output.append(cur_s)
                return

            if open_b < n:
                dfs(open_b+1, close_b, cur_s + "(")
            if close_b < open_b:
                dfs(open_b, close_b+1, cur_s + ")")

        
        open_b, close_b, cur_s, output = 0, 0, "", []
        dfs(open_b, close_b, cur_s)


        return output