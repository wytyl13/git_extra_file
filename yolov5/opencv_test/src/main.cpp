#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/opencv.hpp>
#include <torch/torch.h>
#include <torch/script.h>
#include <iostream>


int main(int argc, char const *argv[])
{

    std::cout << torch::cuda::is_available() << std::endl;
    cv::Mat image = cv::imread("c:/users/80521/desktop/1.png");
    cv::imshow("window", image);
    cv::waitKey(0);
    system("pause");
    return 0;
}
