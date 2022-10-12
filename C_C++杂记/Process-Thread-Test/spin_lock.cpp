//#include <stdio.h>
//#include <stdlib.h>
//#include <unistd.h>
//#include <pthread.h>
//#include <vector>
//
//pthread_spinlock_t spin_lock;
//
//int num = 0;
//
//void *producer(void *) {
//    int times = 10000000;
//    while (times--) {
//        pthread_spin_lock(&spin_lock);
//        num += 1;
//        pthread_spin_unlock(&spin_lock);
//    }
//}
//
//void *comsumer(void *) {
//    int times = 10000000;
//    while (times--) {
//        pthread_spin_lock(&spin_lock);
//        num -= 1;
//        pthread_spin_unlock(&spin_lock);
//    }
//}
//
//
//int main() {
//
//    pthread_spin_init(&spin_lock, 0);
//    pthread_t thread1, thread2;
//    pthread_create(&thread1, NULL, &producer, NULL);
//    pthread_create(&thread2, NULL, &comsumer, NULL);
//    pthread_join(thread1, NULL);
//    pthread_join(thread2, NULL);
//    printf("临界资源： %d\n", num);
//    return 0;
//}
//
