//
// Created by 文若 on 2021/11/10.
//

#include <stdio.h>

int Add(int, int);

int main() {

    int c = Add(3, 7);
    printf("%d", c);
    return 0;
}

int Add(int a, int b) {
    return a + b;
}

