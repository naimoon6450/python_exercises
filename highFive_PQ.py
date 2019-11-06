"""
/*
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.


Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

PriorityQueue class

new PriorityQueue(capacity)
min-heap
push() adds element to pq
pop() returns and removes the root node of pq
isEmpty() boolean
size() integer

https://docs.python.org/3/library/queue.html#Queue.PriorityQueue
*/

heapq.heappush(pq, 10)
print(heapq.heappop(pq))

"""


import heapq
from functools import reduce

def highFive(matrix):
  # init dict for students
  studentDict = {}
  for i in range(len(matrix)):
      if (matrix[i][0] in studentDict):
        heapq.heappush(studentDict[matrix[i][0]], matrix[i][1])
      else:
        pq = []
        heapq.heappush(pq, matrix[i][1])
        studentDict[matrix[i][0]] = pq
        
  for ind in studentDict:
    while len(studentDict[ind]) > 5:
      heapq.heappop(studentDict[ind])
  
  
  


highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])
   
  
  
   