# Problem: given a set of N positive numbers S = {n1, . . . , nN},
# is there a partition of this set of numbers into two disjoint subsets
# R and S − R, such that the sum of the elements in both sets is the same?

# ------- Import -------

# Python library import section
from collections import defaultdict

# D-Wave library import section
from dwave.system import DWaveSampler, EmbeddingComposite

# ------- Code section -------

#  ------- Test Data -------

# set1 = { "x0" : 3, "x1" : 4, "x2" : 4, "x3" : 3}

set1 = { "x0" : 7, "x1" : 5, "x2" : 3, "x3" : 4, "x4" : 6, "x5" : 5, "x6" : 2, "x7" : 4 }

set1 = { "x0" : 9, "x1" : 5, "x2" : 3, "x3" : 4, "x4" : 6, "x5" : 5, "x6" : 2, "x7" : 4 }

#  ------- Main -------

# Calculate K = sum(Xi)/2
k = 0
for x in set1:
    k += set1[x]
k= k//2
print(k)

# Initialize the Q matrix
Q = defaultdict(int)

# Set linear weights
for x in set1:
    n = set1[x]
    Q[(x,x)] += (n * n) - (2 * n * k)

# Set quadratic weights
keys = list(set1.keys())
for i in range(len(keys)):
    for j in range ((i+1), len(keys)):
        Q[(keys[i],keys[j])] += 2 * set1[keys[i]] * set1[keys[j]]

print("Final QUBO:")
print(Q)

# Run the QUBO on the solver from your config file
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_qubo(Q,
                               chain_strength=100,   # Arbitrary choice...
                               num_reads=100,
                               label="Set 1")

print ("Response:")
print(response)

# Calculate the sums for the two subsets

# Select first response
firstSample = response.first.sample

# Calculate first sum
sum1 = 0
for x in firstSample:
    if firstSample[x]==1:
        sum1 += set1[x]

# Calculate second sum
sum2 = 0
for x in firstSample:
    if firstSample[x]==0:
        sum2 += set1[x]

print("Sum1 = %d - Sum2 = %d" % (sum1, sum2))
