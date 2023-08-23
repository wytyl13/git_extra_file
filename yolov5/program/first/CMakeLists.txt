
# 项目名称
project(FIRST)

# 头文件
include_directories("./include")
# 定义cpp文件 忘记怎么写了，查下
aux_source_directory(./src SRC_DIR)
add_compile_options(-Wall -fexec-charset=GBK -std=c++11)
# 然后first文件是用来生成静态库的，cmakelist有生成静态库的指令
# 忘记了
# add_library(<name> [STATIC | SHARED | MODULE]
# [EXCLUDE_FROM_ALL]
# [<source>...])

add_library(${PROJECT_NAME} STATIC ${SRC_DIR})

# 然后可以将对应的静态库包含的头文件添加到添加该静态库的项目中，这个很重要
# 这样做的目的是如果我们在其他微服务中包含了该静态库，那么我们可以直接在该微服务中添加该静态库对应的
# 头文件，不需要定义路径，直接include "*.h"即可，因为该静态库的头文件路径已经添加到对应的
# 项目中了
# target_include_directories(<target> [SYSTEM] [AFTER|BEFORE]
#    <INTERFACE|PUBLIC|PRIVATE> [items1...]
#    [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])
# 我忘记了，我查下.ok
target_include_directories(FIRST PUBLIC include)


# 到这其实就完了，因为我们在该静态库中没有包含任何第三方库，也不需要生成可执行文件。

