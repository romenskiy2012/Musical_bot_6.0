def init_read(A):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    F = []
    F.extend(A)
    class Car:
        number_couple = [] # number_couple
        number_quantity = 0
        number = ""


        def clear(self):
            Car.number_quantity = 0
            Car.number = ""

        @staticmethod
        def checking_number(trash): # Проверка числа!
            for number in numbers:
                if number == trash:

                    Car.number_quantity = Car.number_quantity + 1
                    #print(f"LOL - {Car.number_quantity}")
                    if Car.number_quantity <= 2:
                        #print(trash)
                        Car.number = Car.number + trash
                        #print(Car.number)
                    #else:
                        #Car.clear()
                    return False
            return True


        def transport_numbers(self): # Перенос числа нахуй
            if self.number != "":
                self.number_couple.append(int(self.number))
                self.clear()
                pass

        def save_numbers(self): # Высрать число
            self.transport_numbers()
            self.number_couple.reverse()
            seconds = 0
            multiplier = 1
            print(f"DDD --- {self.number_couple}")
            for piece_number_couple in self.number_couple:
                seconds = seconds + piece_number_couple * multiplier
                multiplier = multiplier * 60
            self.number_couple = []
            self.clear()
            return seconds
        def ls(self): # Проверка готово ли число
            if len(self.number_couple) != 0:
                return True
            return False



    hub_time = []
    hub_name = []
    car_a = Car()
    name_read = False
    collector = ""
    for trash in F:
        if trash == "\n":
            car_a.clear()
            name_read = False
            if collector != "":
                collector = collector.replace(']', '')
                hub_name.append(collector) # Высрать имя
                collector = ""

        elif name_read == True:
            collector = collector + trash

        elif trash == ":":
            car_a.transport_numbers() # Перенос числа нахуй

        else:
            if car_a.checking_number(trash):# Проверка числа!
                if car_a.ls(): # Проверка готово ли число
                    hub_time.append(car_a.save_numbers()) # Высрать число
                    name_read = True
                elif Car.number != "":
                    car_a.clear()
    if collector != "":
        collector = collector.replace(']', '')
        hub_name.append(collector) # Высрать имя
    print("AAAAAA")
    print(hub_time)
    print(hub_name)
    return hub_time, hub_name

"1:29:57 ?"


A = """
Best Nightcore Songs Mix 2022 ♫ Gaming Music Mix ♫ House, DnB, Trap, Bass, Dubstep NCS, Monstercat
Like = Motivation
If you enjoyed this mix, please be sure to comment "kurumi ara ara"

Tracklist:

00:00 Nightcore - ABRO & A'Lone - Takeaway
https://garde.lnk.to/takeaway

02:21 Nightcore - JKRS & AIZZO - Hung Up
http://garde.lnk.to/hung-up

04:28 Nightcore - Ascence - Umbrella
https://fhc.fanlink.to/umbrella

06:58 Nightcore - JKRS & AIZZO - Smells Like Teen Spirit
https://garde.lnk.to/slts

09:07 Nightcore - Mannymore & Blaze U - Closer
https://fhc.fanlink.to/mb-closer

11:10 Nightcore - anaïs x Dillistone - Yellow Hearts (Lyrics) [7clouds Release]
https://7clouds.fanlink.to/YellowHearts

13:48 Nightcore - Kat Meoz - Run Tonight
https://cloudkid.lnk.to/runtonight

16:08 Nightcore - Kat Meoz - Somebody Else
https://cloudkid.lnk.to/somebodyelse

19:15 Nightcore - Jim Yosef & Anna Yvette - Linked [NCS Release]
http://ncs.io/2017LinkedID

22:36 Nightcore - JJD, BOXOY - Still Looking Out For You (Lyrics) ft. Eline Esmee [7clouds Release]
https://7clouds.fanlink.to/StillLooki...

25:29 Nightcore - Kat Meoz - Reason (Lyrics) [7clouds Release]
https://7clouds.fanlink.to/Reason

28:18 Nightcore - Mickey Valen - Ur Perfect I Hate It (Airmow Remix)
https://cloudkid.lnk.to/urperfect-rem...

30:57 Nightcore - Moorty - All Or Nothing (Lyrics) feat. Lola Rhodes [7clouds Release]
https://spoti.fi/2SJsUcZ

33:48 Nightcore - OVSKY - Time [NCS Release]
https://ncs.io/OTime

35:52 Nightcore - Titanz, KEYMAK & Blith - Dizzy (ft. Anna-Sophia Henry)
https://fhc.fanlink.to/Dizzy

38:13 Nightcore - Allergic & LOOP - All Good Things (Come To An End)
https://garde.lnk.to/agt

40:18 Nightcore - KENO & MERSII - All I Need
https://fhcd.fanlink.to/allineed

42:45 Nightcore - Kilian K, MEYSTA & Nito-Onna - Sweet Dreams
https://fhc.fanlink.to/sweet-dreams

44:40 Nightcore - Lost Sky - Vision pt. II (feat. She Is Jules) [NCS10 Release]
https://ncs.io/Vision2

47:47 Nightcore - Mert Can - Poker Face
https://garde.lnk.to/pokerface

49:42 Nightcore - NO.NEED & Matt Zho - Counting Stars
http://garde.lnk.to/countingstars

52:12 Nightcore - STAR SEED - Cayenne (feat. Zoe Moon) [NCS Release]
https://ncs.io/Cayenne

56:10 Nightcore - Syn Cole - Melodia [NCS Release]
https://ncs.io/Melodia

58:38 Nightcore - Mo Falk & OVSKY - Home [NCS Release]
https://ncs.io/MOHome

01:01:23 Nightcore - Amir Sohrab - Save My Heart (ft. MONA)
https://fhcs.fanlink.to/savemyheart

01:04:28 Nightcore - Amir Sohrab - Whisper
https://fhcs.fanlink.to/whisper

01:07:19 Nightcore - Sam Ourt & FERGO - Love Me [NCS Release]
https://ncs.io/SFLoveMe

01:09:17 Nightcore - Spirit Link, Fakti, køhvt - Again & Again (Lyrics) [7clouds Release]
https://7clouds.fanlink.to/AgainAndAgain

01:11:44 Nightcore - Rachel Lorin - Kerosene (Lyrics) [7clouds Release]
https://7clouds.fanlink.to/Kerosene

nightcore , nightcore mix , nightcore mix 2022 , nightcore 2022 , mix , nightcore 1 hour , nightcore playlist , kurumi nightcore , nightcore songs

Thumbnail Character: https://bit.ly/31VgwLK

📧 Submit your Track: kurumitrack@gmail.com
📧 Copyright issues: kurumicri@gmail.com

NoCopyrightSounds / NCS
https://youtube.com/NoCopyrightSounds
https://soundcloud.com/nocopyrightsounds
https://instagram.com/nocopyrightsounds
https://facebook.com/NoCopyrightSounds
https://twitter.com/NCSounds

7clouds
https://open.spotify.com/user/7clouds...
https://facebook.com/7cloudsmusic
https://twitter.com/7cloudsmusic
https://instagram.com/7clouds

CloudKid
https://soundcloud.com/cloudkid
https://instagram.com/cloudkid
https://twitter.com/cloudkidmusic
https://facebook.com/cldkid

Future House Cloud
https://youtube.com/c/FutureCloud
https://facebook.com/futurehousecloud
https://soundcloud.com/future-house-c...
https://instagram.com/futurehousecloud
https://futurehousecloud.com

Garde
https://soundcloud.com/garderecords
https://garde.fanlink.to/spotify
https://youtube.com/channel/UCSlYjL17...

Kurumi
https://open.spotify.com/playlist/0WP...
https://twitter.com/KurumiMixes
https://facebook.com/KurumiMixes
https://instagram.com/KurumiMixes

#nightcore
#nightcoremusic
#nightcoremix
#nightcoresongs
#nightcore1hour
"""

"""
hub_time, hub_name = init_read(A)
for Al in hub_time:
    print(Al)
print("---------------------")
for Al in hub_name:
    print(Al)
"""
