from random import randint, random
from mergealgorithum import mergeSort
from time import time 


averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)
 
def test_BubbleWorst():
    start= time()
    assert mergeSort(worstcase) == bestcase
    print("worst")
    print(time()-start)
 
def test_BubbleBest():
    start= time()
    assert mergeSort(bestcase) == bestcase
    print("best")
    print(time()-start)
 
def test_BubbleAvg():
    start= time()
    assert mergeSort(averagecase) == bestcase
    print("age")
    print(time()-start)

test_BubbleWorst()
test_BubbleBest()
test_BubbleAvg()