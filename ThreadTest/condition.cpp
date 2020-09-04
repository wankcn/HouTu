#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <unistd.h>
#include <pthread.h>

int MAX_BUF = 20;
int num = 0;


pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void* producer(void*){
    while(true){
        pthread_mutex_lock(&mutex);
        while (num >= MAX_BUF){
            // 等待
            printf("缓冲区满了, 等待消费者消费...\n");
            pthread_cond_wait(&cond, &mutex);
        }
        num += 1;
        printf("生产一个产品，当前产品数量为：%d\n", num);
        sleep(1); // 生产产品需要的时间
        pthread_cond_signal(&cond);
        printf("通知消费者...\n");
        pthread_mutex_unlock(&mutex);
        sleep(1); // 生产产品的频率
    }

}

void* consumer(void*){
    while(true){
        pthread_mutex_lock(&mutex);
        while (num <= 0){
            // 等待
            printf("缓冲区空了, 等待生产者生产...\n");
            pthread_cond_wait(&cond, &mutex);
        }
        num -= 1;
        printf("消费一个产品，当前产品数量为：%d\n", num);
        sleep(1);
        pthread_cond_signal(&cond);
        printf("通知生产者...\n");
        pthread_mutex_unlock(&mutex);
    }
}

int main(){
    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, &consumer, NULL);
    pthread_create(&thread2, NULL, &producer, NULL);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    return 0;
}