import subprocess
import sys

def install():
	subprocess.check_call([sys.executable, "-m", "pip", "install", "dlib"])
	subprocess.check_call([sys.executable, "-m", "pip", "install", "face-recognition"])
	subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python"])
	subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy==1.19.3"])

if __name__ == '__main__':
	install()