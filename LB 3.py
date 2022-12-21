from itertools import permutations
import time
start1 = time.time()
array = []


def permutation(s, n):
    i = 0

    def fill(o):
        start2 = time.time()
        u = 0
        while o >= u:
            array.append(u)
            u += 1
        end2 = time.time() - start2
        print("Total time for fill:", end2)
    fill(n)
    for a in list(s):
        i += 1
        print(a)
    print("Total elements:", i)
    return


permutation(array, 4)
arr = permutations(array)
permutation(arr, 0)
end1 = time.time() - start1
print("Total time:", end1)
