// Generated by gencpp from file robotis_controller_msgs/LoadOffsetRequest.msg
// DO NOT EDIT!


#ifndef ROBOTIS_CONTROLLER_MSGS_MESSAGE_LOADOFFSETREQUEST_H
#define ROBOTIS_CONTROLLER_MSGS_MESSAGE_LOADOFFSETREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace robotis_controller_msgs
{
template <class ContainerAllocator>
struct LoadOffsetRequest_
{
  typedef LoadOffsetRequest_<ContainerAllocator> Type;

  LoadOffsetRequest_()
    : file_path()  {
    }
  LoadOffsetRequest_(const ContainerAllocator& _alloc)
    : file_path(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _file_path_type;
  _file_path_type file_path;





  typedef boost::shared_ptr< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> const> ConstPtr;

}; // struct LoadOffsetRequest_

typedef ::robotis_controller_msgs::LoadOffsetRequest_<std::allocator<void> > LoadOffsetRequest;

typedef boost::shared_ptr< ::robotis_controller_msgs::LoadOffsetRequest > LoadOffsetRequestPtr;
typedef boost::shared_ptr< ::robotis_controller_msgs::LoadOffsetRequest const> LoadOffsetRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace robotis_controller_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'robotis_controller_msgs': ['/home/robotis/Kulin_ws/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a1f82596372c52a517e1fe32d1e998e8";
  }

  static const char* value(const ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa1f82596372c52a5ULL;
  static const uint64_t static_value2 = 0x17e1fe32d1e998e8ULL;
};

template<class ContainerAllocator>
struct DataType< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robotis_controller_msgs/LoadOffsetRequest";
  }

  static const char* value(const ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string file_path\n\
";
  }

  static const char* value(const ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.file_path);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct LoadOffsetRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robotis_controller_msgs::LoadOffsetRequest_<ContainerAllocator>& v)
  {
    s << indent << "file_path: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.file_path);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOTIS_CONTROLLER_MSGS_MESSAGE_LOADOFFSETREQUEST_H
