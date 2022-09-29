---
title: "LeetCode 344"
date: 2022-09-24T15:10:28+08:00
tags: ["leetcode"]
draft: false
---

### 思路

利用左右指针的思想，从两边向中间逼近，同时交换左右的值

### 我的代码

```java
class Solution {
    public void reverseString(char[] s) {
        int left = 0, right = s.length -1 ;

        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
}
```

### References

---

#### 1. [反转字符串](https://leetcode.cn/problems/reverse-string/)
