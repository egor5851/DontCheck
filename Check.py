import os

os.system("nvidia-smi")
os.system("wget -nv -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
os.system("unzip -n ngrok-stable-linux-amd64.zip")
os.system("./ngrok authtoken 1rGMQTuyZINkpxj5DuXioj7Er7e_883WpSvfqfPkU91RbNUDy")
os.system("./ngrok tcp 22")
