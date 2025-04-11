import os
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():
    # Ruta absoluta al archivo .xacro
    xacro_file = "/home/aristizabal/microros_ws/src/brazo_robert/urdf/brazo_robert.xacro"

    # Comando para convertir Xacro a URDF
    robot_description = Command(["xacro ", xacro_file])


    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            output="screen",
            parameters=[{"robot_description": robot_description}]),  
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            name="joint_state_publisher_gui",
            output="screen"),
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            output="screen"),
    ])

