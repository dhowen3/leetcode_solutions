class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        r = 0
        for i in range(n):
            x1, y1 = points[i]
            d = dict()
            c = 0
            for j in range(i+1,n):
                x2, y2 = points[j]
                m,b = 0,0
                if x2 == x1:
                    m = 'inf'
                    b = x1
                else:
                    m = round((y2 - y1) / (x2 - x1), 8)
                    b = round(y2 - m * x2, 3)
                print(m,b)
                try: d[(m,b)] += 1
                except: d[(m,b)] = 1
                r = max(r, d[(m,b)])
        return r + 1
