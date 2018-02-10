#created by Austin Kelly on 2/10/18

import random, glob, time
from twitter import *
from pics import *

token = "962243224470302720-3AHLnzO2Wcu8ihnWqPvb6SV5i6Hss29"
token_secret = "wNuxP4xpYUah6SVCifajx26LZemTh4BooyXRDsdMEpHkO"
consumer_key = "VxRP5BYo2bsdX6gx0MS1obhEM"
consumer_secret = "rIZyKVTkjbXYt45oxEv4xk6XfQNU6dL0g5F6hOPCYNfNguP8Wg"

t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

quote_array = ["Let freedom ring!"]
hashtag_array = ["#Patriotism"]
image_list = glob.glob('pics/*.jpg') 

quote_array.append("Take a moment of silence for old glory!")
quote_array.append("God bless America!")
quote_array.append("God bless The United States of America!")
quote_array.append("God bless the USA")
quote_array.append("Today we remember those who live in this great country")
quote_array.append("The greatest country in the entire world")
quote_array.append("Take a moment of silence for our founding fathers")
quote_array.append("With liberty and justice for all!")
quote_array.append("Ole Glory")
quote_array.append("There it is, Ole Glory")
quote_array.append("Nothing wrong with loving your country")
quote_array.append("One nation under God!")
quote_array.append("Waving proudly")
quote_array.append("Look at her wave")
quote_array.append("Standing tall as a reminder")
quote_array.append("A gentle reminder of our great country")
quote_array.append("Americans are the luckiest people on earth")
quote_array.append("Land of the free")
quote_array.append("Home of the brave")
quote_array.append("Land of the free BECAUSE of the brave")
quote_array.append("Land of the free and home of the brave")
quote_array.append("The greatest nation in the world")
quote_array.append("Waving today with pride")
quote_array.append("Please take a moment of silence for our flag")
quote_array.append("Please take a moment of silence for Ole Glory")
quote_array.append("Please take a moment of silence for our country")
quote_array.append("Take a moment of silence for our perfect country")
quote_array.append("How lucky are we to be born in the land of the free?")
quote_array.append("The United States means everything")
quote_array.append("I'd rather be a flag waver than a flag hater")
quote_array.append("Nothing but respect for the flag")
quote_array.append("So much respect for this beautiful piece of cloth")
quote_array.append("Live free or die")
quote_array.append("If this flag offends you, leave!")
quote_array.append("Ole Glory, a symbol of pride")
quote_array.append("What a beautiful sight to see")
quote_array.append("To love one's country is to love the world")
quote_array.append("A symbol of national pride")
quote_array.append("We will do anything for this flag")
quote_array.append("The message this flag stands for is undeniable")
quote_array.append("Never forget")
quote_array.append("A country built on morals")
quote_array.append("My loyalty is to this flag")
quote_array.append("Hello fellow patriots!")
quote_array.append("Love the country, love the countrymen")
quote_array.append("Americans never give up")
quote_array.append("Representing my beautiful country")
quote_array.append("My country tis of thee")
quote_array.append("We the people")
quote_array.append("America First")

hashtag_array.append("#GodBlessAmerica")
hashtag_array.append("#GodBlessOurTroops")
hashtag_array.append("#RespectTheFlag")
hashtag_array.append("#OldGlory")
hashtag_array.append("#OleGlory")
hashtag_array.append("#MomentOfSilence")
hashtag_array.append("#America")
hashtag_array.append("#USA")
hashtag_array.append("#AmericaFirst")
hashtag_array.append("#Freedom")
hashtag_array.append("#Liberty")
hashtag_array.append("#Motivation")


def getStatus():
    quote = random.choice(quote_array)
    return quote

def getHashtag():
    tag = random.choice(hashtag_array)
    return tag

def getText():
    output = getStatus()+'\n'+getHashtag()
    return output

def getImage():
    image = random.choice(image_list)
    return image



def post():
    print ("posting...")
    with open(getImage(), "rb") as imagefile:
        imagedata = imagefile.read()
    t_upload = Twitter(domain='upload.twitter.com',
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))
    id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
    # send tweet with the list of media ids
    t.statuses.update(status=getText(), media_ids=",".join([id_img1]))
    print ("end of post attempt")


#run
post()
while True:
    time.sleep(3600)
    post()

    

