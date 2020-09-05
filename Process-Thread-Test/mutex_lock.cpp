#include <stdio.h>
#include <pthread.h>
#include <vector>

// 使用互斥量解决线程同步问题 初始化互斥量
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

// 临界资源
int num = 0;

// 生产者
[[noreturn]] void *producer(void *) {
    int times = 1000000;
    while (times--) {
//        pthread_mutex_lock(&mutex);
        num += 1;
//        pthread_mutex_unlock(&mutex);
    }
}

// 消费者
void *comsumer(void *) {
    int times = 1000000;
    while (times--) {
//        pthread_mutex_lock(&mutex);
        num -= 1;
//        pthread_mutex_unlock(&mutex);
    }
}

int main() {
    time_t start,stop;
    start = time(NULL);
    for (int i = 0; i < 10; ++i) {
        pthread_t thread1, thread2;
        pthread_create(&thread1, NULL, &producer, NULL);
        pthread_create(&thread2, NULL, &comsumer, NULL);
        pthread_join(thread1, NULL);
        pthread_join(thread2, NULL);
        printf("临界资源：%d\n", num);
    }
    stop = time(NULL);
    printf("Use Time:%ld\n",(stop-start));
    return 0;
}

