//
// Created by 文若 on 2020/9/5.
//

#include <iostream>
#include <unistd.h>

using namespace std;

int main() {
    // 定义进程id
    pid_t pid;
    int num = 666;
    pid = fork();

    // 对返回进行判断
    if (pid == 0) {
        cout << "这是一个子进程||";
        cout << "子进程中的num：" << num << endl;
        for (int i = 0; i < 5; ++i) {
            num += 1;
            cout << num << " ";
        }
    } else if (pid > 0) {
        cout << "这是一个父进程||" << "子进程id" << pid << "||父进程中的num：" << num << endl;
        for (int i = 0; i < 5; ++i) {
            num -= 1;
            cout << num << " ";
        }
        cout << endl;
    } else {
        cout << "创建进程失败" << endl;
    }
    return 0;
}
