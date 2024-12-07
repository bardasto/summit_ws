from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch.conditions import IfCondition
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Пути к файлам
    robot_description_path = get_package_share_directory('summit_description') + '/urdf/summit.urdf.xacro'

    # Объявление аргументов
    gui_arg = DeclareLaunchArgument(
        'gui',
        default_value='true',
        description='Flag to enable joint_state_publisher GUI'
    )

    # Возвращаем LaunchDescription с исправлением для использования IfCondition
    return LaunchDescription([
        # Аргументы запуска
        gui_arg,

        # Node для публикации описания робота
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': Command(['xacro ', robot_description_path])
            }]
        ),

        # Node для публикации состояний суставов с условием IfCondition
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
            condition=IfCondition(LaunchConfiguration('gui'))
        ),

        # Node для спавна робота в Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-topic', 'robot_description',
                '-entity', 'summit'
            ],
            output='screen'
        )
    ])
