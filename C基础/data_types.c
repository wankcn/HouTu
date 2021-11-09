//
// Created by 文若 on 2021/11/8.
//

#include <stdio.h>
#include <limits.h>

int main() {
    short short_i = 0;
    int i = 0;
    long long_i = 0;
    long long longlong_i = 0;
    unsigned int unsigned_i = 123;

    // d decimal
    // x hex
    // o oct
    // %hd short decimal
    // %d decimal
    // %ld long decimal
    // %lld long long decimal
    // %hu unsigned short decimal
    // ...


    // decimal
    printf("short int : %d\n", sizeof(short));
    printf(" int : %d\n", sizeof(int));
    printf("long int : %ld\n", sizeof(long));
    printf("long long int : %lld\n", sizeof(long long));
    printf("uint : %u\n", sizeof(unsigned int));

    // 2的31次 最高位用作符合
    printf("Max int : %d, Min int : %d\n", INT_MAX, INT_MIN);
    printf("Max uint : %u, Min uint : %u\n", UINT_MAX, 0);
    return 0;
}