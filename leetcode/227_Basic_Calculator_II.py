class Solution:
    def calculate(self, s: str) -> int:
        """

        Goal: Evaluate the given expression.

        Caution:
        There are empty spaces in the string

        Appraoch: Stack
        1. Push all the integer and operators in separate stack. Skip spaces.
        2. Calculate all the multiplication and divisions.

        stack [3,4]
        opeator: [+,*]
        2*2

        [3,2]
        [/]

        Appracoh:
        1. Check if the current index value is not an empty space.
        2. If it is an integer, get the full number and append it to a stack.
        3. If operator is not empty, calculate the new sum and append to the stack.
        4. Get a operator variable that only stores division and multiplication.

        Runtime: O(N)
        Spacetime: O(K) 

        """

        i, stack, operator = 0, [], []

        while i < len(s):
            if s[i] != " ":
                if s[i].isdigit():
                    l = i
                    r = i
                    while r+1 < len(s) and s[r+1].isdigit():
                        r += 1
                        i += 1
                    if s[l-1] == "-":
                        stack.append(-int(s[l:r+1]))
                    else:
                        stack.append(int(s[l:r+1]))

                # Calculate the new sum when sees a division or multiplication
                if operator:
                    op = operator.pop()
                    y = stack.pop()
                    x = stack.pop()

                    if op == '*':
                        stack.append(x*y)
                    else:
                        if x//y >= 0:
                            stack.append(x//y)
                        else:
                            stack.append(-(abs(x)//y))
                
                if s[i] == '*' or s[i] == '/':
                    operator.append(s[i])
            i += 1

        return sum(stack)
        
