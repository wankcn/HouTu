cmake_minimum_required(VERSION 3.10.2)

# 拿到当前文件所在目录的名字
get_filename_component(ProjectID ${CMAKE_CURRENT_SOURCE_DIR} NAME)

# 如果目录中包含空格替换成"_"
string(REPLACE " " "_" ProjectID ${ProjectID})

project(${ProjectID} C)

set(CMAKE_C_STANDARD 11)

# 获取目录下所有的.C文件存入files里
file(GLOB files "${CMAKE_CURRENT_SOURCE_DIR}/*.c")

# 遍历files把它们添加成可执行程序
foreach (file ${files})
    get_filename_component(name ${file} NAME)
    add_executable(${name} ${file} hanoi.c)
endforeach ()

