class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        """
        
        [      l  
            [1,2, 3, 4], 
          e [5,6, 7, 8], 
            [9,10,11,12] s
                   r   
        ]
        
        
        [    l
             i
           [ 1, 2, 3 ], 
         e [ 4, 5, 6 ], 
           [ 7, 8, 9 ] s
                   r
        ]
        
        thinking of it like below is probably easier
        although end and start are equal here
        
        [    l
         e [ 1, 2, 3 ], s
                   r
        ]
        
        
        """
        if (matrix == []):
            return []
        
        # initialize pointers
        left_col = 0
        right_col = len(matrix[0]) - 1
        
        start_row = 0
        end_row = len(matrix) - 1
        
        direction = 'right'
        
        spiral = []
        
        while(left_col <= right_col and start_row <= end_row):
            if (direction == 'right' and start_row <= end_row):
                for i in range(left_col, right_col + 1):
                    # row is static, col changing
                    spiral.append(matrix[start_row][i])
                start_row += 1
                direction = 'down'

            if (direction == 'down' and start_row <= end_row):
                for i in range(start_row, end_row + 1):
                    # you want the rows to change so i, and the last val at each row so right_col
                    spiral.append(matrix[i][right_col])
                right_col -= 1
                direction = 'left'
                
            if (direction == 'left' and start_row <= end_row):
                for i in range(right_col, left_col - 1, -1):
                    # you want row to be static
                    spiral.append(matrix[end_row][i])
                end_row -= 1
                direction = 'up'
            
            if (direction == 'up' and left_col <= right_col):
                for i in range(end_row, start_row - 1, -1):
                    # row changing column static
                    spiral.append(matrix[i][left_col])
                left_col += 1
                direction = 'right'
            
        
        return spiral
            
            