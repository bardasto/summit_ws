cmake_minimum_required(VERSION 3.5)
project(summit_description)

# Найти зависимости ROS 2
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(xacro REQUIRED)
find_package(rclpy REQUIRED)
find_package(gazebo_ros REQUIRED)

# Установка файлов описания робота
install(
  DIRECTORY urdf meshes launch config
  DESTINATION share/${PROJECT_NAME}
)

# Экспортировать пакет
ament_package()
