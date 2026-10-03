#===============================================
#              SELECTION SORT 
#===============================================
#ALGORITHM SelectionSort(A[0..n − 1])
#Sorts a given array by selection sort
#Input: An array A[0..n − 1] of orderable elements
#Output: Array A[0..n − 1] sorted in nondecreasing order

"""
What the algorithm does:
Scans the entire given list to find its smallest element and exchange it
with the first element, putting the smallest element in its final position 
in the sorted list.
"""
#for i ← 0 to n − 2 do
#min ← i
#for j ← i + 1 to n − 1 do
#if A[j ] <A[min] min ← j
#swap A[i] and A[min]

#n = the input size (the size of the array)
#range (a,b) where a is included and its stops at b-1

def selection_sort(A):
 for i in range (len(A) - 2):
    mini = i 
    for j in range (i+1, len(A)):
      if A[j] < A[mini]:
        mini = j
    A[i] , A[mini] = A[mini], A[i] #int (x,y) = (0,1)
      
 return A

A = [89, 45, 68, 90, 29, 34, 17]

print (selection_sort(A))




