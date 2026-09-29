
"""
What did you see on line 1?
7, 6, 10, and 18
What was the smallest number you could have seen, what was the largest?
5 and 20
What did you see on line 2?
9, 7, 3,and 3
What was the smallest number you could have seen, what was the largest?
3 and 9
Could line 2 have produced a 4?
No, because the first possible number is 3, and randrange has a step of 2.
What did you see on line 3?
3.6774056530466446, 4.491802046879959, 4.367926250434581, 4.339537518211378, and 2.8804766213480892
What was the smallest number you could have seen, what was the largest?
2.5 and 5.5
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
import random
print(random.randint(1, 100))