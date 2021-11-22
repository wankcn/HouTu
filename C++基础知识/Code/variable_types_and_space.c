//
// Created by 文若 on 2021/11/10.
//
#include <stdio.h>

void PassByMemory(int para) {
    printf("%d\n", para);
}

void PassByRegister(register int para) {
    printf("%d\n", para);
}

int main() {

    return 0;
}