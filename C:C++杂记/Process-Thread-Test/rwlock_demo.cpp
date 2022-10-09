//
// Created by 文若 on 2020/9/5.
//

#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <vector>

// 临界资源
int num = 0;

pthread_rwlock_t rwlock = PTHREAD_RWLOCK_INITIALIZER;

void *reader(void *) {
    int times = 1000000;
    while (times--) {
        // 读前加读锁
        pthread_rwlock_rdlock(&rwlock);
        if (times % 1000 == 0) {
            usleep(10); // 睡眠10微妙查看性能
        }
        pthread_rwlock_unlock(&rwlock);
    }
}

void *writer(void *) {
    int times = 1000000;
    while (times--) {
        // 写前写锁
        pthread_rwlock_wrlock(&rwlock);
        num += 1;
        pthread_rwlock_unlock(&rwlock);
    }
}

int main() {

    pthread_t thread1, thread2, thread3;
    pthread_create(&thread1, NULL, &reader, NULL);
    pthread_create(&thread2, NULL, &reader, NULL);
    pthread_create(&thread3, NULL, &writer, NULL);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    pthread_join(thread3, NULL);
    printf("临界资源：%d\n", num);


    return 0;
}

