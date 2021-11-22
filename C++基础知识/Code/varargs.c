//
// Created by 文若 on 2021/11/10.
//

#include <stdio.h>
#include <stdarg.h>

// 先传长度，然后传个数
void HandleVarargs(int count, ...) {
    va_list args;  // 定义va_list获取变长参数

    // 开始遍历
    va_start(args, count);
    // 取出对应的参数
    for (int i = 0; i < count; ++i) {
        int arg = va_arg(args, int);
        printf("%d\n", arg);
    }
    // 结束遍历
    va_end(args);
}

int main() {
    HandleVarargs(5, 2, 3, 4, 5, 6);
    return 0;
}

