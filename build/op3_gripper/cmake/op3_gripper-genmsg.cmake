# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "op3_gripper: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iop3_gripper:/home/robotis/Kulin_ws/src/op3_gripper/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(op3_gripper_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/robotis/Kulin_ws/src/op3_gripper/msg/GripperPosition.msg" NAME_WE)
add_custom_target(_op3_gripper_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "op3_gripper" "/home/robotis/Kulin_ws/src/op3_gripper/msg/GripperPosition.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(op3_gripper
  "/home/robotis/Kulin_ws/src/op3_gripper/msg/GripperPosition.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/op3_gripper
)

### Generating Services

### Generating Module File
_generate_module_cpp(op3_gripper
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/op3_gripper
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(op3_gripper_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(op3_gripper_generate_messages op3_gripper_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robotis/Kulin_ws/src/op3_gripper/msg/GripperPosition.msg" NAME_WE)
add_dependencies(op3_gripper_generate_messages_cpp _op3_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(op3_gripper_gencpp)
add_dependencies(op3_gripper_gencpp op3_gripper_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS op3_gripper_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(op3_gripper
  "/home/robotis/Kulin_ws/src/op3_gripper/msg/GripperPosition.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/op3_gripper
)

### Generating Services

### Generating Module File
_generate_module_eus(op3_gripper
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/op3_gripper
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(op3_gripper_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(op3_gripper_generate_messages op3_gripper_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robotis/Kulin_ws/src/op3_gripper/msg/GripperPosition.msg" NAME_WE)
add_dependencies(op3_gripper_generate_messages_eus _op3_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(op3_gripper_geneus)
add_dependencies(op3_gripper_geneus op3_gripper_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS op3_gripper_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(op3_gripper
  "/home/robotis/Kulin_ws/src/op3_gripper/msg/GripperPosition.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/op3_gripper
)

### Generating Services

### Generating Module File
_generate_module_lisp(op3_gripper
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/op3_gripper
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(op3_gripper_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(op3_gripper_generate_messages op3_gripper_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robotis/Kulin_ws/src/op3_gripper/msg/GripperPosition.msg" NAME_WE)
add_dependencies(op3_gripper_generate_messages_lisp _op3_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(op3_gripper_genlisp)
add_dependencies(op3_gripper_genlisp op3_gripper_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS op3_gripper_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(op3_gripper
  "/home/robotis/Kulin_ws/src/op3_gripper/msg/GripperPosition.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/op3_gripper
)

### Generating Services

### Generating Module File
_generate_module_nodejs(op3_gripper
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/op3_gripper
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(op3_gripper_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(op3_gripper_generate_messages op3_gripper_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robotis/Kulin_ws/src/op3_gripper/msg/GripperPosition.msg" NAME_WE)
add_dependencies(op3_gripper_generate_messages_nodejs _op3_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(op3_gripper_gennodejs)
add_dependencies(op3_gripper_gennodejs op3_gripper_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS op3_gripper_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(op3_gripper
  "/home/robotis/Kulin_ws/src/op3_gripper/msg/GripperPosition.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/op3_gripper
)

### Generating Services

### Generating Module File
_generate_module_py(op3_gripper
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/op3_gripper
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(op3_gripper_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(op3_gripper_generate_messages op3_gripper_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/robotis/Kulin_ws/src/op3_gripper/msg/GripperPosition.msg" NAME_WE)
add_dependencies(op3_gripper_generate_messages_py _op3_gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(op3_gripper_genpy)
add_dependencies(op3_gripper_genpy op3_gripper_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS op3_gripper_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/op3_gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/op3_gripper
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/op3_gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/op3_gripper
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/op3_gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/op3_gripper
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/op3_gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/op3_gripper
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/op3_gripper)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/op3_gripper\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/op3_gripper
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()