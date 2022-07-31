from random import randint, random
from selective1 import selectionsort
from time import time 

averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)
 
def test_BubbleWorst():
    start= time()
    assert selectionsort(worstcase) == bestcase
    print("worst")
    print(time()-start)
 
def test_BubbleBest():
    start= time()
    assert selectionsort(bestcase) == bestcase
    print("best")
    print(time()-start)
 
def test_BubbleAvg():
    start= time()
    assert selectionsort(averagecase) == bestcase
    print("age")
    print(time()-start)

test_BubbleWorst()
test_BubbleBest()
test_BubbleAvg()