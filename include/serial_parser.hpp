#ifndef   SERIAL_PARSER_HPP
#define   SERIAL_PARSER_HPP
#include "ros/ros.h"
#include "std_msgs/Int64MultiArray.h"

#include <iostream>
#include <boost/asio.hpp>
#include <boost/bind.hpp>
#include <boost/thread.hpp>
#include <boost/algorithm/string/classification.hpp> // is_any_of
#include <boost/algorithm/string/split.hpp>
#include <boost/range/algorithm/for_each.hpp>
#include <boost/array.hpp>
#include <algorithm>



class serial_parser{
    private:
        ros::NodeHandle n_;
        std::string port_name_:
        ros::Publisher pub_enc_;
        
        int baud_rate_;
        boost::thread thr_io_;
        std::string wbuf_;
        boost::array<char, 32> rbuf_;
        boost::asio::io_service io_;
        boost::asio::serial_port port_( io_, port_name_ );
        serial_read_CB_(const boost::system::error_code& e, std::size_t size, boost::array r);


    public:
        serial_parser();
        ~serial_parser();
};

#endif // SERIAL_PARSER_HPP