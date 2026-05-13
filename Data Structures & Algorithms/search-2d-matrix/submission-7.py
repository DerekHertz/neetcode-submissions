class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check first element of each row, determine which direction to go
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1


        l_rows = 0
        row_to_parse = 0

        # find what row target could be in
        while l_rows <= rows:
            m_row = (rows + l_rows) // 2

            m_0 = matrix[m_row][0]
            m_n = matrix[m_row][cols]

            # check first and last element of row
            if target == m_0 or target == m_n:
                return True

            # target is in previous row
            elif target < m_0:
                rows = m_row - 1

            # target is in next row
            elif target > m_n:
                l_rows = m_row + 1

            # target is greater than row[0] but less than last element, should be in this row
            else:
                row_to_parse = m_row
                break
                
        l_cols = 0
        # parse row
        while l_cols <= cols:
            m_col = (cols + l_cols) // 2
            print(f"middle col of row {row_to_parse}: {m_col}")

            if target == matrix[row_to_parse][m_col]:
                return True

            # target is in left side of row
            elif target < matrix[row_to_parse][m_col]:
                cols = m_col - 1

            # target is in right side of row
            elif target > matrix[row_to_parse][m_col]:
                l_cols = m_col + 1
        
        # not found
        return False
            