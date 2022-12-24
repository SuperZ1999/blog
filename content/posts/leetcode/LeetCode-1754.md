---
title: "LeetCode 1754"
date: 2022-12-24T21:51:19+08:00
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

贪心算法，每次选择字典序较大的字符串的第一个字符拼接到merge后即可，唯一要记住的点是字符串比较大小的方式，见零碎部分

### 代码

```java
class Solution {
    public String largestMerge(String word1, String word2) {
        StringBuilder sb1 = new StringBuilder(word1);
        StringBuilder sb2 = new StringBuilder(word2);
        StringBuilder merge = new StringBuilder();
        while (sb1.length() != 0 || sb2.length() != 0) {
            if (sb1.toString().compareTo(sb2.toString()) > 0) {
                merge.append(sb1.charAt(0));
                sb1.deleteCharAt(0);
            } else {
                merge.append(sb2.charAt(0));
                sb2.deleteCharAt(0);
            }
        }
        return merge.toString();
    }
}
```

### References

---

#### 1. [构造字典序最大的合并字符串](https://leetcode.cn/problems/largest-merge-of-two-strings/description/)
