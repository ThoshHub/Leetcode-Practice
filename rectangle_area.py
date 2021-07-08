# Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
# The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).
# The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    area1 = (ax2-ax1)*(ay2-ay1)
    area2 = (bx2-bx1)*(by2-by1)
    l = max(min(ax2, bx2) - max(ax1, bx1), 0)
    
    h = max(min(ay2, by2) - max(ay1, by1), 0)
    print(str(area1) + ", " + str(area2))
    print(str(l) + ", " + str(h))
    area3 = l*h
    return area1 + area2 - area3

ax1 = -3
ay1 = 0

ax2 = 3
ay2 = 4

bx1 = 0
by1 = -1

bx2 = 9
by2 = 2

r = computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
print(r)

