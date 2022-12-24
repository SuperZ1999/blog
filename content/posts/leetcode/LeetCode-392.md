---
title: "LeetCode 392"
date: 2022-12-24T20:35:03+08:00
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

将t中的字符及其位置都存到一个map中去，然后判断s中的字符是否都存在于该map中，并且该字符在t中的位置在前一个字符在t中的位置的后面，为了快速找到该位置的字符，可以用二分查找，因为位置在数组中是递增有序的，详见代码

### 代码

```java
class Solution {
    public boolean isSubsequence(String s, String t) {
        int m = s.length(), n = t.length();
        Map<Character, List<Integer>> index = new HashMap<>();
        for (int i = 0; i < n; i++) {
            char c = t.charAt(i);
            if (!index.containsKey(c)) {
                index.put(c, new ArrayList<>());
            }
            index.get(c).add(i);
        }
        int j = 0;
        for (int i = 0; i < m; i++) {
            char c = s.charAt(i);
            List<Integer> arr = index.get(c);
            if (arr == null) {
                return false;
            }
            int pos = left_bound(arr, j);
            if (pos == -1) {
                return false;
            }
            j = arr.get(pos) + 1;
        }
        return true;
    }

    private int left_bound(List<Integer> nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (target <= nums.get(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        if (nums.get(left) < target) {
            return -1;
        }
        return left;
    }
}
```

### References

---

#### 1. [判断子序列](https://leetcode.cn/problems/is-subsequence/)
