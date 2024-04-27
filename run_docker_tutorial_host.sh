docker run -it --rm --device=/dev/ttyUSB0 --name matsya_ros2 \
 --net=host\
 --env="DISPLAY"\
 --env ROS_DOMAIN_ID=79\
 --workdir="/home/docker/colcon_ws"\
 --volume=$(pwd)/colcon_ws:"/home/docker/colcon_ws"\
 --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw"\
 --volume="/dev/shm:/dev/shm"\
  abhilashiit/matsya_ros2:1.0 bash
