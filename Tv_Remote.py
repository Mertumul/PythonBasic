import random
import time


class TV_Remote():

    def __init__(self,tv_status="OFF",tv_volume=0,channel_list=["Fox"],channel="Fox"):

        self.tv_status=tv_status
        self.tv_volume=tv_volume
        self.channel_list=channel_list
        self.channel=channel

    def turn_on_tv(self):
        if(self.tv_status=="ONN"):
            print("TV is already onn")
        else:
            print("TV turns onn")
            self.tv_status="ONN"

    def turn_of_tv(self):
        if(self.tv_status=="OFF"):
            print("TV is already off")
        else:
            print("TV turns off")
            self.tv_status="OFF"

    def set_the_sound(self):
        while(True):
            answer=input("press the '<' to decrease the voleme\npress the '>' to increase the volume\npress the 'q' to exit")

            if answer=='<':
                dec=int(input("enter the volume you want to reduce"))
                if dec>self.tv_volume:
                    print("the sound cannot go below zero")
                else:
                    self.tv_volume -=dec

            elif answer=='>':
                inc=int(input("enter the volume you want to increase"))
                if (self.tv_volume+inc) >100:
                    print("the sound cannot go above 100")
                else:
                    self.tv_volume +=inc
            elif answer =='q':
                break
            else:
                print("please press the correct keys!! ")

    def add_channel(self,channel_name):
        print("Channel is being added....")
        time.sleep(1)
        self.channel_list.append(channel_name)
        print("Channel Added..")

    def randon_channel(self):

        rand=random.randint(0,len(self.channel_list))
        self.channel=self.channel_list[rand]
        print("Current Channel=",self.channel)

    def __len__(self):
        return len(self.channel_list)
    
    def __str__(self):
        return "TV Status = {}\nTV_Volume = {}\nChannel List = {}\nCurrent Channel = {}".format(self.tv_status,self.tv_volume,self.channel_list,self.channel)


tv_remote1=TV_Remote()
print("""

TV APPLICATION

1.Turn on the TV

2.Turn off the TV

3.Set the Sound

4.Add Channel

5.Learn the number of channels

6.Pass the Randon Channel

7.TV Information

Please press the 'q' to exit

""")

while(True):
    ans=input("Which action would you like to apply?")

    if ans =='q':
        break
    elif ans =='1':
        tv_remote1.turn_on_tv()
    elif ans =='2':
        tv_remote1.turn_of_tv()
    elif ans =='3':
        tv_remote1.set_the_sound()
    elif ans =='4':
        addchannel=input("Write the channel names separated by commas!!!")
        channel_list=addchannel.split(",")
        for add in channel_list:
            tv_remote1.add_channel(add)
    elif ans =='5':
        print("Number of Channels =",len(tv_remote1))
    elif ans =='6':
        tv_remote1.randon_channel()
    elif ans =='7':
        print(tv_remote1)

    else:
        print("please press the correct keys!! ")
    