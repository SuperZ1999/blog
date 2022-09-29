---
title: "LeetCode 151"
date: 2022-09-26T10:45:08+08:00
tags: ["leetcode"]
draft: false
---

### 思路

可以split成单词，再reverse，再拼接，但是不够优雅，会使用了额外的空间，正确做法是先reverse整个数组，然后再reverse各个单词，但要注意一下细节，比如去空格什么的

### 我的代码

```java
class Solution {
    private void reverse(char[] s, int i, int j) {
        int left = i, right = j - 1;
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }

    private void translate(char[] s, int i, int j, int step) {
        for (int k = i; k < j; k++) {
            s[k - step] = s[k];
        }
        for (int k = j - step; k < j; k++) {
            s[k] = ' ';
        }
    }

    public String reverseWords(String s) {
        char[] cs = s.toCharArray();
        reverse(cs, 0, cs.length);

        int left = -1, step = 0;
        for (int i = 0; i < cs.length; i++) {
            if (cs[i] == ' ') {
                if (left != -1) {
                    reverse(cs, left, i);
                    translate(cs, left, i, step);
                    left = -1;
                } else {
                    step++;
                }
            } else {
                if (left == -1) {
                    left = i;
                }
            }
        }

        if (left != -1) {
            reverse(cs, left, cs.length);
            translate(cs, left, cs.length, step);
        }

        return new String(cs).trim();
    }
}
```

### References

---

#### 1. [反转字符串中的单词](https://leetcode.cn/problems/reverse-words-in-a-string/)
