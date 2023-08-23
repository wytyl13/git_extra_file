project(SECOND)


include_directories("./include")
aux_source_directory(./src SRC_DIR)
add_compile_options(-Wall -fexec-charset=GBK -std=c++11)

# 这个不需要生成库文件，直接执行编译，然后添加第一个微服务的库文件即可
add_executable(${PROJECT_NAME} ${SRC_DIR})

# 将第一个库文件添加到这个项目
target_link_libraries(${PROJECT_NAME} FIRST)