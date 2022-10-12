//
// Created by 文若 on 2021/11/8.
//
#include <stdio.h>
#include <stddef.h>

int main() {

    //--------------------- 窄字符
    char i = 0;
    char a = 'a';

    char char_1 = '1';
    // \后面加一个八进制的数表示一个字符
    char char_49_otc = '\61';
    char char_49_hex = '\x31';

    printf("char a:%d\n", a);
    printf("char_1:%d\n", char_1);
    printf("char i:%d\n", i);

    printf("char_1:%c\n", char_1);
    printf("char_49_otc:%c\n", char_49_otc);
    printf("char_49_hex:%c\n", char_49_hex);

    //--------------------- 宽字符 C95引入
    // 还可以使用 \u+码点表示 \u4e2d
    wchar_t z = L'中';
    wchar_t z2 = L'\u4e2d';
    printf("中：%d\n", z);
    printf("中2：%d\n", z2);

    return 0;
}