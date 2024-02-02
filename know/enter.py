import video
import retext
import middle_mian.stt as stt
import quickstart3
import pickle
import playsound

def main():
	global fooddate1
	stt.main()
	with open('data_dict.pkl','rb') as f:
		food1=pickle.load(f)
	want = stt.transcript
	for key in food1.keys():
		if(key == want):
			fooddate = food1.get(key)
			fooddate1= fooddate.pop(0)
			quickstart3.main()
		else:
			print("dd")
			
if __name__=="__main__":
    main()
