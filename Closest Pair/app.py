import math


def truncate(f):
    n = 3
    return math.floor(f * 10 ** n) / 10 ** n


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def compareX(a, b):
    p1 = a
    p2 = b
    return (p1.x - p2.x)


def compareY(a, b):
    p1 = a
    p2 = b
    return (p1.y - p2.y)


def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y))


def bruteForce(P, n):
    min_dist = [dist(P[0], P[1]), P[0], P[1]]
    for i in range(n):
        for j in range(i+1, n):
            if dist(P[i], P[j]) < min_dist[0]:
                min_dist[0] = dist(P[i], P[j])
                min_dist[1] = P[i]
                min_dist[2] = P[j]
    return min_dist


def min(x, y):
    return x if x < y else y


def stripClosest(strip, size, d):
    min_dist = d
    strip = sorted(strip, key=lambda point: point.y)

    for i in range(size):
        for j in range(i+1, size):
            if (strip[j].y - strip[i].y) >= min_dist[0]:
                break
            if dist(strip[i], strip[j]) < min_dist[0]:
                min_dist[0] = dist(strip[i], strip[j])
                min_dist[1] = strip[i]
                min_dist[2] = strip[j]
    return min_dist


def closestUtil(P, n):
    if n <= 3:
        return bruteForce(P, n)
    mid = n//2
    midPoint = P[mid]
    dl = closestUtil(P, mid)
    dr = closestUtil(P[mid:], n - mid)
    if(dl[0] > dr[0]):
        d = dr
    else:
        d = dl
    strip = []
    for i in range(n):
        if abs(P[i].x - midPoint.x) < d[0]:
            strip.append(P[i])
    m = stripClosest(strip, len(strip), d)
    if (d[0] > m[0]):
        return m
    else:
        return d

def closest(P, n):
	P = sorted(P, key=lambda point: point.x)
	return closestUtil(P, n)


if __name__ == "__main__":
    n = int(input())
    P = []
    for i in range(0, n):
        z = input().split()
        x = int(z[0])
        y = int(z[1])
        P.append(Point(x, y))
    res = closest(P, n)
    print(truncate(res[0]))
    print(res[1].x, res[1].y)
    print(res[2].x, res[2].y)
