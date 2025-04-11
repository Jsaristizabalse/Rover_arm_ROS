cmake_minimum_required(VERSION 3.8)
project(brazo_robert)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Encontrar dependencias
find_package(ament_cmake REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# Instalar el archivo URDF pero EXCLUYENDO los .xacro
install(
    DIRECTORY urdf launch rviz worlds config
    DESTINATION share/${PROJECT_NAME}
  #  PATTERN "*.xacro" EXCLUDE
)

ament_package()

