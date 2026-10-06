class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''we can determine what char will be seen based on
        numRows.
        We iterate through rows until the last char is seen
        if it is the first or the last row, we don't alternate
        in diagonal and vertical, only take the letters that are
        in the vertical patterns
        '''
        if numRows == 1:
            return s

        ret_str = []
        curr_letter = 0
        jump = 2*numRows - 2
        while curr_letter < len(s):
            ret_str.append(s[curr_letter])
            #etc
            curr_letter += jump

        curr_row = 1
        #some while iteration
        while curr_row < numRows - 1:
            vertical_pointer = curr_row
            diagonal_pointer = jump - curr_row
            while vertical_pointer < len(s):
                ret_str.append(s[vertical_pointer])
                if diagonal_pointer < len(s):
                    ret_str.append(s[diagonal_pointer])
                vertical_pointer += jump
                diagonal_pointer += jump

            curr_row += 1
        #curr_row = last row after iterating

        vertical_pointer = curr_row
        while vertical_pointer < len(s):
            ret_str.append(s[vertical_pointer])
            vertical_pointer += jump
        #we basically repeat first while loop

        return "".join(ret_str)
if __name__ == "__main__":
    s = Solution()
    a = s.convert(s = "A", numRows = 1)
    print(a)