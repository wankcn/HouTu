//
// Created by 文若 on 2021/11/9.
//

#include <stdio.h>

void print_bin(int n) {
    int l = sizeof(n) * 8;//总位数。
    int i;
    if (i == 0) {
        printf("0");
        return;
    }
    for (i = l - 1; i >= 0; i--)//略去高位0.
    {
        if (n & (1 << i)) break;
    }

    for (; i >= 0; i--)
        printf("%d", (n & (1 << i)) != 0);

    printf("\n");
}

int main() {
    // 与位有关的运算符
    // &   按位与   ｜  按位或  ^ 按位异或    ~  按位取反

    // 按位运算符是把两个操作数分别转换成二进制数，如果两个二进制数长度不一样，在短的左边补0，补到一样的长度，然后对两个二进制数按对应的位进行运算
    // & 相同是1为1 不同为0  1&1=1；1&0=0；0&1=0；0&0=0
    // | 有1为1 全0为0
    // ^ 不同为1 相同为0
    // ～ 1得0 0得1


#define FLAG_VISIBLE 0x1     // 0001
#define FLAG_TRANSPARENT 0x2 // 0010
#define FLAG_TRANSPARENT_1 1 << 1 // 0010   等同1左移动1位
#define FLAG_RESIZABLE 0x4   // 0100

    int window_flag = FLAG_RESIZABLE | FLAG_TRANSPARENT;  // 0110
    int resizable = window_flag & FLAG_RESIZABLE;         // 0100 & 0110     0100


    printf("window_flag : %d\n", window_flag);
    printf("resizable : %d\n", resizable);

    print_bin(window_flag);
    print_bin(resizable);

    // 左移 *2 右移/2
    int x = 1000;
    x <<= 2;
    printf("左移,%d\n", x);

    // 逗号运算符 x = 4000
    x = x / 2, x += 300;
    printf("逗号运算符取逗号后面,%d\n", x);
    return 0;
}

