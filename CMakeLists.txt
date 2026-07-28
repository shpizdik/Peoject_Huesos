cmake_minimum_required(VERSION 3.10)
project(ProjectHuesos)

# Устанавливаем стандарт C++
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# ----------------------------
# 1. GLFW (собираем из исходников)
# ----------------------------
add_subdirectory(external/glfw)

# ----------------------------
# 2. GLAD (просто добавляем файл)
# ----------------------------
add_library(glad STATIC external/glad/src/glad.c)
target_include_directories(glad PUBLIC external/glad/include)

# ----------------------------
# 3. Основной исполняемый файл
# ----------------------------
add_executable(reltih src/engine/reltih.cpp)

# Подключаем заголовки GLAD и GLFW
target_include_directories(reltih PRIVATE
    external/glad/include
    external/glfw/include
)

# Линкуем библиотеки
target_link_libraries(reltih
    glad                # наш статический GLAD
    glfw                # библиотека, собранная из external/glfw
)

# ----------------------------
# 4. Платформозависимые библиотеки
# ----------------------------
if(WIN32)
    target_link_libraries(reltih opengl32)
elseif(APPLE)
    target_link_libraries(reltih
        "-framework OpenGL"
        "-framework Cocoa"
        "-framework IOKit"
    )
else() # Linux
    target_link_libraries(reltih GL)
endif()