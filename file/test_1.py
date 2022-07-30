from random import randint, random
from bubble1 import bubblesort
from time import time 

averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)
 
def test_BubbleWorst():
    start= time()
    assert bubblesort(worstcase) == bestcase
    print("worst")
    print(time()-start)
 
def test_BubbleBest():
    start= time()
    assert bubblesort(bestcase) == bestcase
    print("best")
    print(time()-start)
 
def test_BubbleAvg():
    start= time()
    assert bubblesort(averagecase) == averagecase
    print("age")
    print(time()-start)

test_BubbleWorst()
test_BubbleBest()
test_BubbleAvg()