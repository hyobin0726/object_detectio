import video
import retext
import pickle

global food
food = dict()
food[video.name]=[retext.result]
print(food)
with open('data_dict.pkl','wb') as f:
	pickle.dump(food,f)

