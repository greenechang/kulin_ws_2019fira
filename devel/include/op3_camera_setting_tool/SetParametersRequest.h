// Generated by gencpp from file op3_camera_setting_tool/SetParametersRequest.msg
// DO NOT EDIT!


#ifndef OP3_CAMERA_SETTING_TOOL_MESSAGE_SETPARAMETERSREQUEST_H
#define OP3_CAMERA_SETTING_TOOL_MESSAGE_SETPARAMETERSREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <op3_camera_setting_tool/CameraParams.h>

namespace op3_camera_setting_tool
{
template <class ContainerAllocator>
struct SetParametersRequest_
{
  typedef SetParametersRequest_<ContainerAllocator> Type;

  SetParametersRequest_()
    : params()  {
    }
  SetParametersRequest_(const ContainerAllocator& _alloc)
    : params(_alloc)  {
  (void)_alloc;
    }



   typedef  ::op3_camera_setting_tool::CameraParams_<ContainerAllocator>  _params_type;
  _params_type params;





  typedef boost::shared_ptr< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SetParametersRequest_

typedef ::op3_camera_setting_tool::SetParametersRequest_<std::allocator<void> > SetParametersRequest;

typedef boost::shared_ptr< ::op3_camera_setting_tool::SetParametersRequest > SetParametersRequestPtr;
typedef boost::shared_ptr< ::op3_camera_setting_tool::SetParametersRequest const> SetParametersRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace op3_camera_setting_tool

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'op3_camera_setting_tool': ['/home/robotis/Kulin_ws/src/ROBOTIS-OP3-Tools/op3_camera_setting_tool/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4ae71cfda3f5edf19cfb9ef891d039e8";
  }

  static const char* value(const ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4ae71cfda3f5edf1ULL;
  static const uint64_t static_value2 = 0x9cfb9ef891d039e8ULL;
};

template<class ContainerAllocator>
struct DataType< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "op3_camera_setting_tool/SetParametersRequest";
  }

  static const char* value(const ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "CameraParams  params\n\
\n\
================================================================================\n\
MSG: op3_camera_setting_tool/CameraParams\n\
# This represents the parameters of usb camera\n\
\n\
uint32  brightness 							# 0 - 255\n\
uint32  contrast                            # 0 - 255\n\
uint32  saturation                          # 0 - 255\n\
uint32  sharpness                           # 0 - 255\n\
uint32  gain                                # 0 - 255\n\
bool    focus_auto                          #\n\
int32  focus_absolute                       # -1 - 255\n\
uint32  exposure_auto                       #\n\
uint32  exposure_absolute                   # 0 - 255\n\
bool    white_balance_temperature_auto      #\n\
uint32  white_balance_temperature           # 4000 - 6500\n\
";
  }

  static const char* value(const ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.params);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetParametersRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::op3_camera_setting_tool::SetParametersRequest_<ContainerAllocator>& v)
  {
    s << indent << "params: ";
    s << std::endl;
    Printer< ::op3_camera_setting_tool::CameraParams_<ContainerAllocator> >::stream(s, indent + "  ", v.params);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OP3_CAMERA_SETTING_TOOL_MESSAGE_SETPARAMETERSREQUEST_H
