---
title: "LeetCode 43"
date: 2022-12-20T11:35:00+08:00
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

就是大整数乘法，用列式计算的方式计算两个字符串的乘积，如下图所示：

![img](https://labuladong.gitee.io/algo/images/%e5%ad%97%e7%ac%a6%e4%b8%b2%e4%b9%98%e6%b3%95/4.gif)

详见：<https://labuladong.gitee.io/algo/4/33/126/>

### 代码

```java
class Solution {
    public String multiply(String num1, String num2) {
        char[] n1 = num1.toCharArray();
        char[] n2 = num2.toCharArray();
        int l1 = n1.length, l2 = n2.length;
        int[] res = new int[l1 + l2];
        for (int i = l1 - 1; i >= 0; i--) {
            for (int j = l2 - 1; j >= 0; j--) {
                int mul = (n1[i] - '0') * (n2[j] - '0');
                int sum = mul + res[i + j + 1];
                res[i + j + 1] = sum % 10;
                res[i + j] += sum / 10;
            }
        }
        int offset = 0;
        while (offset < res.length && res[offset] == 0) {
            offset++;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = offset; i < res.length; i++) {
            sb.append(res[i]);
        }
        return sb.length() == 0 ? "0" : sb.toString();
    }
}
```

### References

---

#### 1. [字符串相乘](https://leetcode.cn/problems/multiply-strings/)
