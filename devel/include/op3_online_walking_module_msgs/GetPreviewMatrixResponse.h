// Generated by gencpp from file op3_online_walking_module_msgs/GetPreviewMatrixResponse.msg
// DO NOT EDIT!


#ifndef OP3_ONLINE_WALKING_MODULE_MSGS_MESSAGE_GETPREVIEWMATRIXRESPONSE_H
#define OP3_ONLINE_WALKING_MODULE_MSGS_MESSAGE_GETPREVIEWMATRIXRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <op3_online_walking_module_msgs/PreviewResponse.h>

namespace op3_online_walking_module_msgs
{
template <class ContainerAllocator>
struct GetPreviewMatrixResponse_
{
  typedef GetPreviewMatrixResponse_<ContainerAllocator> Type;

  GetPreviewMatrixResponse_()
    : res()  {
    }
  GetPreviewMatrixResponse_(const ContainerAllocator& _alloc)
    : res(_alloc)  {
  (void)_alloc;
    }



   typedef  ::op3_online_walking_module_msgs::PreviewResponse_<ContainerAllocator>  _res_type;
  _res_type res;





  typedef boost::shared_ptr< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GetPreviewMatrixResponse_

typedef ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<std::allocator<void> > GetPreviewMatrixResponse;

typedef boost::shared_ptr< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse > GetPreviewMatrixResponsePtr;
typedef boost::shared_ptr< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse const> GetPreviewMatrixResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace op3_online_walking_module_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'op3_online_walking_module_msgs': ['/home/robotis/Kulin_ws/src/ROBOTIS-OP3-msgs/op3_online_walking_module_msgs/msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7d75f439dc091946b1653b9d97860045";
  }

  static const char* value(const ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7d75f439dc091946ULL;
  static const uint64_t static_value2 = 0xb1653b9d97860045ULL;
};

template<class ContainerAllocator>
struct DataType< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "op3_online_walking_module_msgs/GetPreviewMatrixResponse";
  }

  static const char* value(const ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "op3_online_walking_module_msgs/PreviewResponse res\n\
\n\
\n\
================================================================================\n\
MSG: op3_online_walking_module_msgs/PreviewResponse\n\
int32 K_row\n\
int32 K_col\n\
float64[] K\n\
int32 P_row\n\
int32 P_col\n\
float64[] P\n\
";
  }

  static const char* value(const ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.res);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetPreviewMatrixResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::op3_online_walking_module_msgs::GetPreviewMatrixResponse_<ContainerAllocator>& v)
  {
    s << indent << "res: ";
    s << std::endl;
    Printer< ::op3_online_walking_module_msgs::PreviewResponse_<ContainerAllocator> >::stream(s, indent + "  ", v.res);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OP3_ONLINE_WALKING_MODULE_MSGS_MESSAGE_GETPREVIEWMATRIXRESPONSE_H
