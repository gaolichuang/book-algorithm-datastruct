

import collections

class Solution(object):
    def canReorderDoubled(self, A):
        count = collections.Counter(A)
        print count
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True



s = Solution()
print s.canReorderDoubled([-1,2])