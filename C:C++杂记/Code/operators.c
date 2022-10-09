//
// Created by 文若 on 2021/11/9.
//
#include <stdio.h>

int main() {
    int first = 0;
    int second;
    int third;

    // 嵌套表示式
    third = second = first;

    int left, right;
    left = 2;
    right = 3;

    int quotient = left / right;           // 0
    // *1.0f 格式化float型 分子必须float
    float quotient_float = left * 1.f / right;   // 0

    printf("quotient,%d\n", quotient);
    printf("quotient_float,%.2f\n", quotient_float);

    // C99开始增加了布尔类型 0假非零真
    printf("3>2:%d\n", 3 > 2); // 1
    printf("3<2:%d\n", 3 < 2); // 0

    int i = 1;
    int j = i++; // j=1;i=2;
    int k = ++i; // k =3;i =3;
    return 0;
}
