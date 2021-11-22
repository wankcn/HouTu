#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {

    for (int i = 0; i < 10; i++) //产生10个随机数
    {
        printf("%d\n", rand());
    }
    return 0;
}