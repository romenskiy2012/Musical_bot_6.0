A = """

ღ Thank you for watching my video ღ

❖ Subscribe and turn on the bell for more ❖

▶️ Mix Information
Best Nightcore Songs Mix 2022 ♫ Gaming Music Mix ♫ House, DnB, Trap, Bass, Dubstep NCS, Monstercat

♫ Tracklist
00:00 Nightcore - Triplo Max x Vanessa Campagna - My Soul Is Your Soul
https://fanlink.to/fTec

02:07 Nightcore - Sabai & Madalen Duke - Love For You
https://monster.cat/loveforyou

05:08 Nightcore - Acejax feat. Danilyon - By My Side
http://ncs.io/ByMySideID

07:47 Nightcore - Coopex & NEZZY - You And Me
http://ncs.io/CNYouAndMe

10:27 Nightcore - Fairlane, ROZES, & JT Roach - Out Loud
http://monster.cat/outloud

13:48 Nightcore - EMDI x RØGUENETHVN - Let Your Heartbreak (feat. Leo the Kind)
http://ncs.io/LetYourHeartbreakID

16:01 Nightcore - it's different - Shadows (feat. Miss Mary)
http://ncs.io/shadows

19:20 Nightcore - JackEL & Merdix Antwinette - Pain (VIP)
https://fanlink.to/cWht

21:34 Nightcore - Rob Gasser & Laura Brehm - Vertigo
http://ncs.lnk.to/vertigo

24:39 Nightcore - Alex Holmes & Dark Point - You Are
http://ncs.io/YouAre

27:24 Nightcore - EMDI & Britt Lari - Magnetic
https://fanlink.to/mgntc

29:40 Nightcore - Laszlo - Feels Like Love
https://monster.cat/10year

32:24 Nightcore - Ellis & Nu Aspect - U
https://monster.cat/10year

36:04 Nightcore - Alex Cortes x The Wavez (feat Dianna) - Crystal Lights (RYSE Remix)
https://fanlink.to/Tuz

39:48 Nightcore - Bishu & Casey Cook - Solid Ground
https://monster.cat/solid-ground

42:00 Nightcore - HuBee - I Wanna Know
https://fanlink.to/gwKZ

44:56 Nightcore - Diamond Eyes - Everything
http://ncs.io/EverythingID

48:54 Nightcore - Alan x Walkers - Unity (Neone Remix)
https://youtu.be/B1tpYjYkcvk

51:22 Nightcore - 3mon - Paradise (ft. Kiara)
https://fanlink.to/prds

53:55 Nightcore - Alex Skrindo, Severin & Like Lions - Heart
https://ncs.io/Heart

56:21 Nightcore - Anixto - Memories (ft. Davis Mallory)
https://fanlink.to/gH9s

59:18 Nightcore - Marin Hoxha - Nostalgic (feat. Hannah Pisani)
https://jupitamusic.com/nostalgic/

01:01:56 Nightcore - NORTIN - Hypnotized
https://fanlink.to/eAA8

01:04:39 Nightcore - Miles Away & AXYS - 18 (feat. RYYZN)
https://fanlink.to/MA-18

01:07:36 Nightcore - Paul Garzon - Vellichor
https://fanlink.to/vllchr

01:10:03 Nightcore - Richard Caddock, WRLD, Nitro Fun, Slippy & Subtact - Break The Silence
http://monster.cat/iTunes-5Year

01:14:04 Nightcore - Vicetone - Fences (feat. Matt Wertz)
https://monstercat.ffm.to/fences

01:17:13 Nightcore - Outwild x She Is Jules - Golden
http://ncs.io/Golden

01:20:57 Nightcore - Jim Yosef & Shiah Maisel - Best of Me
https://fanlink.to/gqJZ

01:23:29 Nightcore - Rival x Cadmium - Seasons (feat. Harley Bird)
http://ncs.io/SeasonsID

01:27:10 Nightcore - Heyder & Navaro & Taylor Mosley - What Is Love
https://fanlink.to/fas8

01:29:57 Nightcore - Heuse & METAHESH - I'll Be Here (Feat. Noctilucent)
https://ncs.io/IllBeHere

▶️ Thumbnail Character: https://bit.ly/3KJYePi

▶️ NoCopyrightSounds / NCS
https://youtube.com/NoCopyrightSounds
https://soundcloud.com/nocopyrightsounds
https://instagram.com/nocopyrightsounds
https://facebook.com/NoCopyrightSounds
https://twitter.com/NCSounds

▶️ Monstercat
https://monster.cat/2biZbkd
https://apple.co/2xiKWTO
https://facebook.com/monstercat
https://twitter.com/monstercat
https://instagram.com/monstercat

▶️ Magic Music / Magic Records
https://youtube.com/channel/UCp6_KuNh...
https://instagram.com/magicmusicsquad/

▶️ Jupita
https://open.spotify.com/user/vv71z58...
https://soundcloud.com/jupitamusic
https://www.instagram.com/jupitamusic/

# Tags:#nightcore #nightcoremix #nightcoresongs #gamingmusic #gamingmix #gamingmusic2022

✉ Copyright / License / Issues: Contact me via email [ariamusicnightcore@gmail.com]
"""
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
F = []
F.extend(A)
"""
G = False
L = 0
i_1 = 0
Lo = 0
M = ""
"01:29:57 ?"
index_l = []
index_A = []
def NAN(A):
    for number in numbers:
        if number == A:
            return True
    return False

for V in F:
    if i_1 == True and V == "\n":
        i_1 = False
        #index_A.append(M)
    else:
        M = M + V
    if V == ":" and G == True and Lo == 2:
        Lo = 0
    elif NAN(V):
        print(f"{L} - {V}")
        #i_1 = L
        index_l.append(V)
        #if Lo == 2:

        Lo = Lo + 1
    elif G == True:
        G = False
        if len(index_l) >= 3:
            i_1 = True
            P = ""
            for Nj in index_l:
                P = P + Nj
            index_A.append(P)
            index_l = []
    elif len(index_l) != 0:
        print(index_l)
        index_l = []


    L = L + 1

for L in index_A:
    print(L)
"""
"""
A = 0
Namber = ""
Nambers = []
index_l = []
G = False
def NAN(A):
    for number in numbers:
        if number == A:
            return True
    return False
for V in F:
    if G == False:
        if NAN(V):
            Namber = Namber + V
        elif V == ":":
            Nambers.append(Namber)
            Namber = ""
        elif len(Nambers) >= 1 and Namber != "":
            Nambers.append(Namber)
            Namber = ""
            if
            if len(Nambers) == 3:
                s
            Nambers = []
            index_l.append()
A = A + A
"""

"01:29:57 ?"
#list.reverse()
class Car:
    Loft = []
    Namber = 0
    Namber_i = ""


    def clear(self):
        Car.Namber = 0
        Car.Namber_i = ""

    @staticmethod
    def NAN(A): # Проверка числа!
        for number in numbers:
            if number == A:

                Car.Namber = Car.Namber + 1
                #print(f"LOL - {Car.Namber}")
                if Car.Namber <= 2:
                    #print(A)
                    Car.Namber_i = Car.Namber_i + A
                    #print(Car.Namber_i)
                #else:
                    #Car.clear()
                return False
        return True


    def LOL(self): # Перенос числа нахуй
        if self.Namber_i != "":
            self.Loft.append(int(self.Namber_i))
            self.clear()
            pass

    def LOL_2(self): # Высрать число
        self.LOL()
        self.Loft.reverse()
        P = 0
        L = 1
        print(f"DDD --- {self.Loft}")
        for A in self.Loft:
            P = P + A * L
            L = L * 60
        self.Loft = []
        self.clear()
        return P
    def ls(self): # Проверка готово ли число
        if len(self.Loft) != 0:
            return True
        return False

LOL_a = []
car_a = Car()
L = False
collector = ""
for trash in F:
    if trash == "\n":
        car_a.clear()
        L = False
        if collector != "":
            LOL_a.append(collector) # Высрать число
            collector = ""

    elif L == True:
        collector = collector + trash

    elif trash == ":":
        car_a.LOL() # Перенос числа нахуй

    else:
        if car_a.NAN(trash):# Проверка числа!
            if car_a.ls(): # Проверка готово ли число
                LOL_a.append(car_a.LOL_2()) # Высрать число
                L = True
print(LOL_a)








