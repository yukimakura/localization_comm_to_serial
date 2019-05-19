#include "serial_parser.hpp"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "serial_parser_node");
    serial_parser ser_parse();

    ros::spin();

    return 0;
}