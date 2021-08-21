# D-Wave-Number-Partitioning
Partitioning of a set of integer numbers in two sets of equal sum

## Problem:
Given a set of N positive numbers S = {N1, . . . , Nm}, is there a partition of this set of numbers into two disjoint subsets
R and S − R, such that the sum of the elements in both sets is the same?

## Solution:
1. Sum all the integers in the set and divide the result by 2, call it K.
1. Associate a QUBO varible Xi to each element of S.
1. Xi set to 0 means that the corresponding integer belongs to first set, while Xi set to 1 means that it belongs to the second set.
1. The solution to the problem requires that the sum of all the number corresponding to set 1 (or 2) equals to K.
1. This can be encoded in the following QUBO formula:

     Q = (Sum(Ni*Xi) - K)^2

1. Expanding the formula we got:
     1. Linear terms: (Ni^2 - 2 * Ni * K) * Xi
     1. Quadratic terms: 2 * Ni * Nj * Xi * Xj