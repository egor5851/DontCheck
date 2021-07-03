import os,time
from threading import Thread
os.system("nvidia-smi")
os.system("wget -nv -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
os.system("unzip -n ngrok-stable-linux-amd64.zip")
os.system("./ngrok authtoken 1ujaauIyCmljt8UDkrQDL5O7ul2_6HuTjpKvtabGtbZJJuw7z")
def ngrok(num)
    print("ng")
    os.system("./ngrok http 25568")
def jupiter(num)
    print("ju")
    os.system("jupyter notebook --ip 0.0.0.0 --port 25568")
thread1 = Thread(target=ngrok, args=(200))
thread2 = Thread(target=jupiter, args=(200))
thread1.start()
thread2.start()
while 5<6:
  time.sleep(5)
  print('Marat')
