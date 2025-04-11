cmake_minimum_required(VERSION 3.8)
project(velocity_publisher)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

install(
    DIRECTORY scripts launch  
    DESTINATION share/${PROJECT_NAME}/
)

install(
    PROGRAMS
    scripts/robot_control_cmd_vel.py
    scripts/move_robot_service.py
    DESTINATION lib/${PROJECT_NAME}
)

install(
    PROGRAMS
    launch/brazo_rover_control.launch.py
    DESTINATION lib/${PROJECT_NAME}
)

ament_package()
