import os


def removefile(filePath):
	if os.path.exists(filePath):
		for file in os.scandir(filePath):
			os.remove(file.path)

if __name__ == "__main__":
    removefile('/home/pi/runs/detect/exp/crops')
