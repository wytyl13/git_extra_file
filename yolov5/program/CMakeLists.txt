
# 定义cmakelists管理文件
# 要求最低cmake版本
cmake_minimum_required(VERSION 3.0)

# 定义项目名称，注意最好不要和对应的文件夹名称重合，一般文件夹小写，这个项目名称大写
# 这个项目名称仅适用于Cmake来管理项目
project(PROGRAM)
# 管理文件不做任何操作，只添加子项目。。就是一个个微服务。但是他可以定义每一个微服务
# 被编译的顺序，比如first微服务是一个库文件，那么他就应该在second微服务之前
# 否则second会调用静态库失败
# 

add_subdirectory(FIRST)
add_subdirectory(SECOND)
# 注意管理文件到这就完了，不需要在家什么了，其实还可以加一个限制C++的版本
# 忘记怎么编写了。







