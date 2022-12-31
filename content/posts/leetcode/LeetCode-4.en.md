---
title: "LeetCode 4"
date: 2022-12-31T15:08:00+08:00
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

三种思路：

#### 简单朴素版

跟两个有序的数组合并思路一样，谁小就取谁，这样找到中间的那个就行了

#### 二分查找

其实这道题就是查找第k小的元素，那么我们每次从两个数组各取k/2个元素，比较第k/2个元素的大小，小的那个数组可以排除前k/2个元素了，然后再在剩下的元素里找第k/2小元素，循环往复，直到找第1小元素即可

#### 划分数组

就是每次对较短的那个数组二分，同时根据元素总数计算另一个数组应该怎么划分，保证左边的元素数量等于右边的，为了找到中位数，所以必须保证左边的最大值小于右边的最小值，如果不满足就根据左边右边的大小关系对较短数组再次二分，直到满足左边与右边元素数量相等，并且左边元素都小于右边元素，此时就找到了中位数

### 代码

#### 简单朴素版

```java
class Solution {
    public double findMedianSortedArrays(int[] A, int[] B) {
        int m = A.length;
        int n = B.length;
        int len = m + n;
        int left = -1, right = -1;
        int aStart = 0, bStart = 0;
        for (int i = 0; i <= len / 2; i++) {
            left = right;
            if (aStart < m && (bStart >= n || A[aStart] < B[bStart])) {
                right = A[aStart++];
            } else {
                right = B[bStart++];
            }
        }
        if ((len & 1) == 0)
            return (left + right) / 2.0;
        else
            return right;
    }
}
```

#### 二分查找

```java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        if ((m + n) % 2 == 0) {
            return (getKth(nums1, 0, nums2, 0, (m + n) / 2) + getKth(nums1, 0, nums2, 0, (m + n) / 2 + 1)) / 2.0;
        } else {
            return getKth(nums1, 0, nums2, 0, (m + n) / 2 + 1);
        }
    }

    private int getKth(int[] nums1, int start1, int[] nums2, int start2, int k) {
        if (start1 == nums1.length) {
            return nums2[start2 + k - 1];
        }
        if (start2 == nums2.length) {
            return nums1[start1 + k - 1];
        }
        if (k == 1) {
            return Math.min(nums1[start1], nums2[start2]);
        }

        int i = Math.min(nums1.length - 1, start1 + k / 2 - 1);
        int j = Math.min(nums2.length - 1, start2 + k / 2 - 1);
        if (nums1[i] > nums2[j]) {
            return getKth(nums1, start1, nums2, j + 1, k - (j - start2 + 1));
        } else {
            return getKth(nums1, i + 1, nums2, start2, k - (i - start1 + 1));
        }
    }
}
```

#### 划分数组

```java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        if (m > n) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int iMin = 0, iMax = m;
        while (iMin <= iMax) {
            int i = (iMax + iMin) / 2;
            int j = (m + n + 1) / 2 - i;
            if (j != 0 && i != m && nums1[i] < nums2[j - 1]) {
                iMin = i + 1;
            } else if (i != 0 && j != n && nums1[i - 1] > nums2[j]) {
                iMax = i - 1;
            } else {
                int maxLeft = 0;
                if (i == 0) {
                    maxLeft = nums2[j - 1];
                } else if (j == 0) {
                    maxLeft = nums1[i - 1];
                } else {
                    maxLeft = Math.max(nums1[i - 1], nums2[j - 1]);
                }
                if ((m + n) % 2 == 1) {
                    return maxLeft;
                }
                int minRight = 0;
                if (i == m) {
                    minRight = nums2[j];
                } else if (j == n) {
                    minRight = nums1[i];
                } else {
                    minRight = Math.min(nums1[i], nums2[j]);
                }
                return (maxLeft + minRight) / 2.0;
            }
        }
        return -1;
    }
}
```

### References

---

#### 1. [寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/)
