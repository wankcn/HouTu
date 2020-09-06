#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <strings.h>
#include <string.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <unistd.h>

#include <iostream>

// 域套接字
#define SOCKET_PATH "./domainsocket" // 定义路径
#define MSG_SIZE 2048 // 定义信息最大长度

int main()
{
    int socket_fd, accept_fd;
	int ret = 0;
	socklen_t addr_len;
	char msg[MSG_SIZE];
	struct sockaddr_un server_addr;

    // 1. 创建域套接字
	socket_fd = socket(PF_UNIX,SOCK_STREAM,0); // 类别，信息流格式
	// -1创建失败
	if(-1 == socket_fd){
		std::cout << "Socket create failed!" << std::endl;
		return -1;
	}
    // 移除已有域套接字路径
	remove(SOCKET_PATH);
    // 内存区域置0
	bzero(&server_addr,sizeof(server_addr));
	server_addr.sun_family = PF_UNIX;
	strcpy(server_addr.sun_path, SOCKET_PATH);

    // 2. 绑定域套接字
    std::cout << "Binding socket..." << std::endl;
    // 创建的域套接字，服务端地址，服务端大小
	ret = bind(socket_fd,(sockaddr *)&server_addr,sizeof(server_addr));

	if(0 > ret){
		std::cout << "Bind socket failed." << std::endl;
		return -1;
	}
	
    // 3. 监听套接字
    std::cout << "Listening socket..." << std::endl;
	ret = listen(socket_fd, 10);
	if(-1 == ret){
		std::cout << "Listen failed" << std::endl;
		return -1;
	}
    std::cout << "Waiting for new requests." << std::endl;
    accept_fd = accept(socket_fd, NULL, NULL);
    
    bzero(msg,MSG_SIZE);

    while(true){
        // 4. 接收&处理信息
        recv(accept_fd, msg, MSG_SIZE, 0);
        std::cout << "Received message from remote: " << msg <<std::endl;
    }

    close(accept_fd);
	close(socket_fd);
	return 0;
}

