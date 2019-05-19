#include "serial_parser.hpp"

serial_parser::serial_parser{
    ros::NodeHandle n_arg_("~");
    port_name_ = "/dev/ttyACM0";
    baud_rate_ = 9600;
    //param
    n_arg_.getParam("port",port_name_);
    n_arg_.getParam("baudrate",baud_rate_);
    pub_enc_ = n_.advertise<std_msgs::Int64MultiArray>("/encoder_raw", 10);


	port_.set_option(serial_port_base::baud_rate(baudrate_));
	port_.set_option(serial_port_base::character_size(8));
	port_.set_option(serial_port_base::flow_control(serial_port_base::flow_control::none));
	port_.set_option(serial_port_base::parity(serial_port_base::parity::none));
	port_.set_option(serial_port_base::stop_bits(serial_port_base::stop_bits::one));

	thr_io_ = new boost::thread(boost::bind(&io_service::run, &io_));

	port_.async_read_until( buffer(rbuf_),';',boost::bind(&serial_parser::serial_read_CB_,this, _1, _2 ));

	// port_.async_write_some( buffer(wbuf), boost::bind(&write_callback, _1, _2));

}

serial_parser::serial_read_CB_(const boost::system::error_code& e, std::size_t size, boost::array r){
    std_msgs::Int64MultiArray encdatas;
    std::vector<std::string> result;
    char *e;
    boost::algorithm::split(result, rbuf_.data(), boost::is_any_of(",")); // カンマで分割
    for(std::string s : result ){
        encdatas.data.push_back(strtol(s,&e,10))
    }

    pub_enc_.publish(encdatas);
}