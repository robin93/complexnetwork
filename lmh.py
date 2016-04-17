import codecs
import random

'''
Function for turning text file to user rating list which has a positive rating
Returns a list of lists, like =
[userid,[song1id,song2id,...]]
'''
def user_rat(filepath):
    ratinglist = []
    with codecs.open(filepath, "r", "utf16") as infile:
        lines = infile.readlines()
        for line in lines:
            userlist = []
	    print line
            songlist = []
            mytext = line.encode('ascii', 'ignore')
            userid = mytext.split("\t")[0]
            songlist = mytext.split("\t")[1].replace("[","").replace("]","")
            songs = songlist.split("', '")
            songlist = []
            for song in songs:
                songid = int(song.split(",")[0].replace("'",""))
                rating = float(song.split(",")[1].replace("'",""))
                if (rating>0):
                    songlist.append(songid)
            userlist = [userid,songlist]
            ratinglist.append(userlist)
    return(ratinglist)

'''
Function for calculating pairwise similarity
Returns a dictionary, like =
{(12654,28767): 0.75}
'''
def similarity(user_song_list):
    random.shuffle(user_song_list)
    similarity = {}
    count = 0
    for user in range(0,len(user_song_list)):
        count += 1
	print count,len(user_song_list)
	#if count > 10:
	#	break
	songs = user_song_list[user][1]
        for i in range(0,len(songs)):
            for j in range(i+1,len(songs)):
                if not(similarity.has_key((songs[i],songs[j])) or similarity.has_key((songs[j],songs[i]))):
                    similarity[(songs[j],songs[i])] = similarity[(songs[i],songs[j])] = 1-((user+1)/len(user_song_list))
    return similarity

'''
Eror inbound: MEMORY Insufficeient
'''
userlist = user_rat("smallint1.txt")
print userlist
sim = similarity(userlist)
output_file = open("local_sensitive_similarity_output.txt", "w+")
for key in sim.keys():
	output_line = str(key[0])+(",")+str(key[1])+("\t")+str(sim[key])+("\n")
	#print output_line
	#print str(key)
	output_file.writelines(output_line)
