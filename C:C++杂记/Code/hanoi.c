//
// Created by 文若 on 2021/11/11.
// 汉诺塔问题 递归
//
#include <stdio.h>

void Move(int n, char src, char dest, char tmp) {
    if (n == 0) return;
    else if (n == 1) printf("%c --> %c\n", src, dest);
    else {
        Move(n - 1, src, tmp, dest);
        Move(1, src, dest, tmp);
        Move(n - 1, tmp, dest, src);
    }
}

int main() {
    Move(3, 'A', 'C', 'B');
    return 0;
}