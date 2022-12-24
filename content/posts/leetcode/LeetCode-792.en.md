---
title: "LeetCode 792"
date: 2022-12-24T21:13:27+08:00
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

同[LeetCode-392](https://blog.zhangmengyang.tk/posts/leetcode/leetcode-392/)，就是比较多个字符串

### 代码

```java
class Solution {
    public int numMatchingSubseq(String s, String[] words) {
        int n = s.length();
        Map<Character, List<Integer>> index = new HashMap<>();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (!index.containsKey(c)) {
                index.put(c, new ArrayList<>());
            }
            index.get(c).add(i);
        }
        int res = 0;
        for (String word : words) {
            int j = 0, i = 0;
            for (; i < word.length(); i++) {
                char c = word.charAt(i);
                List<Integer> arr = index.get(c);
                if (arr == null) {
                    break;
                }
                int pos = left_bound(arr, j);
                if (pos == -1) {
                    break;
                }
                j = arr.get(pos) + 1;
            }
            if (i == word.length()) {
                res++;
            }
        }
        return res;
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

#### 1. [匹配子序列的单词数](https://leetcode.cn/problems/number-of-matching-subsequences/)
