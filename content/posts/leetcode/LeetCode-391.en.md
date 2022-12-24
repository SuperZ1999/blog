---
title: "LeetCode 391"
date: 2022-12-24T20:03:34+08:00
categories: ["leetcode"]
tags: ["leetcode"]
description: ""
weight:
slug: ""
draft: false
disableShare: false
cover:
    image: ""
    caption: ""
    alt: ""
    relative: false
---

### 思路

从「面积」和「顶点」两个维度来判断：

1、判断面积，通过完美矩形的理论坐标计算出一个理论面积，然后和 `rectangles` 中小矩形的实际面积和做对比。

2、判断顶点，`points` 集合中应该只剩下 4 个顶点且剩下的顶点必须都是完美矩形的理论顶点。

详见代码

### 代码

```java
class Solution {
    public boolean isRectangleCover(int[][] rectangles) {
        int n = rectangles.length;
        Set<String> points = new HashSet<>();
        int X1 = Integer.MAX_VALUE, X2 = Integer.MIN_VALUE, Y1 = Integer.MAX_VALUE, Y2 = Integer.MIN_VALUE, area = 0;
        for (int i = 0; i < n; i++) {
            X1 = Math.min(X1, rectangles[i][0]);
            X2 = Math.max(X2, rectangles[i][2]);
            Y1 = Math.min(Y1, rectangles[i][1]);
            Y2 = Math.max(Y2, rectangles[i][3]);
            area += (rectangles[i][2] - rectangles[i][0]) * (rectangles[i][3] - rectangles[i][1]);

            String p1 = rectangles[i][0] + "," + rectangles[i][1];
            String p2 = rectangles[i][2] + "," + rectangles[i][3];
            String p3 = rectangles[i][0] + "," + rectangles[i][3];
            String p4 = rectangles[i][2] + "," + rectangles[i][1];
            for (String p : new String[]{p1, p2, p3, p4}) {
                if (points.contains(p)) {
                    points.remove(p);
                } else {
                    points.add(p);
                }
            }
        }
        if (area != (X2 - X1) * (Y2 - Y1)) {
            return false;
        }
        if (points.size() != 4) {
            return false;
        }
        if (!points.contains(X1 + "," + Y1)) {
            return false;
        }
        if (!points.contains(X1 + "," + Y2)) {
            return false;
        }
        if (!points.contains(X2 + "," + Y1)) {
            return false;
        }
        if (!points.contains(X2 + "," + Y2)) {
            return false;
        }
        return true;
    }
}
```

### References

---

#### 1. [完美矩形](https://leetcode.cn/problems/perfect-rectangle/)
