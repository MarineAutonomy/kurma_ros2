FROM arm64v8/ros:humble
EXPOSE 9000

LABEL maintainer="Akash"
LABEL version="1.0"
LABEL description="Docker environment for ROS2 implementation on Kurma"
RUN apt-get update
RUN apt-get -y install software-properties-common libsm6 libxext6 libxrender1 libfontconfig1 libgl1 sudo xauth python3-pip htop udev
RUN apt-get -y install vim nano git
RUN apt-get -y install iptables




RUN apt-get -y install python3-pip wget
RUN pip install --upgrade pip
RUN apt install ufw -y
# RUN apt-get update

ENV USERNAME kurma
RUN useradd -m $USERNAME && \
       echo "$USERNAME:$USERNAME" | chpasswd && \
       usermod --shell /bin/bash $USERNAME && \
       usermod -aG sudo $USERNAME && \
       usermod -a -G dialout $USERNAME && \
       echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/$USERNAME && \
       chmod 0440 /etc/sudoers.d/$USERNAME

USER kurma
WORKDIR /home/kurma

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source ./install/local_setup.bash" >> ~/.bashrc
RUN echo "export ROS_DOMAIN_ID=79" >> ~/.bashrc
RUN echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
RUN echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc
RUN pip install digi-xbee
RUN pip install websockets


CMD ["bash"]
