cmake_minimum_required(VERSION 3.0)

project(OPENCV_TEST)

aux_source_directory(src SRC_DIR)

add_executable(${PROJECT_NAME} ${SRC_DIR})

# 下面我们添加opencv的lib和include路径到本项目，因为编译的时候需要添加库文件和头文件

# 这个是cmake的一个规则，然后每个第三方库在编写cmakelist文件的时候都会对应的编写一个特定格式的文件
# 让cmake可以使用find_package找到它的库文件和头文件，这个文件一般是在项目的根目录下，我们需要制定
# opencv项目的这个文件的目录，要不它找不到
# OpenCVConfig.cmake应该是这个文件，find_package会根据这个文件去定义
# OpenCV_LIBS和OpenCV_INCLUDE_DIR这两个变量，因为lib库有很多，所以我们一个个往里面添加会很麻烦
# 所以opencv再编写的时候它会自己去生成。
# 我们只需要将install这个目录定义为OpenCV_DIR这个变量，find_package就可以找到这个路径下的cmake后缀的文件
# 可以看到这块报错了
set(OpenCV_DIR "D:\\libtorch_yolo_tools\\opencv\\build\\install")

# 和opencv一样，首先定义libtorch的项目路径，然后找。这个路径下面应该包含cmake文件
# 添加自动扫描好的路径（头文件和库文件）到编译器
set(Torch_DIR "D:\\libtorch_yolo_tools\\libtorch\\share\\cmake\\Torch")
find_package(OpenCV REQUIRED)
find_package(Torch REQUIRED)
if (Torch_FOUND)
    message(STATUS "Torch library found!")
    message(STATUS "include path: ${TORCH_INCLUDE_DIRS}" \n)
    message(STATUS "library path: ${TORCH_LIBRARIES}" \n)
    include_directories(${TORCH_INCLUDE_DIRS})
    target_link_libraries(${PROJECT_NAME} ${TORCH_LIBRARIES})
else ()
    message(FATAL_ERROR "Could not locate Torch" \n)
endif()
if((OpenCV_FOUND))
    #add the include path
    message("WHOAMI")
    include_directories(${OpenCV_INCLUDE_DIR})
    #add the lib
    target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})
    message("have found opencv include: ${OpenCV_INCLUDE_DIRS}")
    message("have found opencv libs: ${OpenCV_LIBS}")
else()
    message(FATAL_ERROR "not found opencv!")
endif()

# 我忘记了，我们从之前的项目中找下这个书写规范