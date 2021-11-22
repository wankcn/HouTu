//
// Created by 文若 on 2021/11/9.
//

#include<stdio.h>

#define RED 0xFF0000 // 宏修饰

int main() {
    // volatile只读值
    volatile const int red = 0xFF0000;
    printf("source %d\n", red);

    int *p = &red;
    *p = 0;
    printf("exchange %d\n", red);  // macos保护常量
    printf("define red %d\n", RED);

    return 0;
}