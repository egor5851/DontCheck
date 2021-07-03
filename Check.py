import os,time

os.system("nvidia-smi")
os.system("wget -nv -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
os.system("unzip -n ngrok-stable-linux-amd64.zip")
os.system("./ngrok authtoken 1ujaauIyCmljt8UDkrQDL5O7ul2_6HuTjpKvtabGtbZJJuw7z")
os.system("./ngrok http 25568")
os.system("jupyter notebook --ip 0.0.0.0 --port 25568")
  while 5<6:
    time.sleep(5)
    print('Marat')
