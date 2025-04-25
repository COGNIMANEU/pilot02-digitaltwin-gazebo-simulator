FROM ros:humble

ENV DEBIAN_FRONTEND=noninteractive
ENV DISPLAY=:1
ENV CONFIG_DIR=/config
ENV LAUNCH_FILE=gazebo_test.launch.py
ENV VNC_PASSWORD=1234
ENV VNC_PORT=6080
ENV RESOLUTION=1280x800
ENV COL_DEPTH=24

RUN apt-get update && apt-get install -y \
    wget \
    && echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list \
    && wget https://packages.osrfoundation.org/gazebo.key -O - | apt-key add - \
    && apt-get update

    RUN apt-get update && apt-get install -y \
    ros-humble-ros-gz-sim \
    ros-humble-ros-gz-bridge \
    ros-humble-ros-gz-image \
    ros-humble-rviz2 \
    ros-humble-teleop-twist-keyboard \
    ignition-fortress \
    libignition-gazebo6-dev \
    libignition-gazebo6-plugins \
    xfce4 xfce4-goodies \
    x11vnc xvfb \
    novnc websockify \
    net-tools curl \
    libqt5x11extras5 libxcb-xinerama0 libxcb-util1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /test_ws

RUN echo '#!/bin/bash\n\
export GAZEBO_MODEL_PATH=/config/models:$GAZEBO_MODEL_PATH\n\
export GZ_SIM_SYSTEM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/ign-gazebo-6/plugins:$GZ_SIM_SYSTEM_PLUGIN_PATH\n\
rm -f /tmp/.X1-lock\n\
VNC_PASSWD=${VNC_PASSWORD}\n\
Xvfb :1 -screen 0 ${RESOLUTION}x${COL_DEPTH} &\n\
sleep 2\n\
startxfce4 &\n\
x11vnc -display :1 -passwd $VNC_PASSWD -forever -shared -rfbport 5900 &\n\
/usr/share/novnc/utils/launch.sh --vnc localhost:5900 --listen ${VNC_PORT} &\n\
source /opt/ros/humble/setup.bash && ros2 launch ${CONFIG_DIR}/${LAUNCH_FILE}' > /startup.sh \
&& chmod +x /startup.sh

CMD ["/bin/bash", "/startup.sh"]