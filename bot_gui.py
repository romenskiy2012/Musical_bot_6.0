# BEGIN ПЕТЬ!
from time import strftime, localtime, sleep, time, gmtime#Для (Time)
import bd_module
import asyncio
import time_mark

def convert_to_preferred_format(sec): # конвертировать в предпочитаемый формат
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    if hour == 0:
        return (f"{min}:{sec}")
    else:
        return (f"{hour}:{min}:{sec}")

theme = 2

async def timeline(bot, SQL_Q, message, time_SSS, lll, index, start_position, description): # временная шкала
    description_list = ""
    if description != None or description != "":
        hub_time, hub_name = time_mark.init_read(description)
    if len(hub_name) == len(hub_time):
        a = 0
        for hub_time_l in hub_time:
            description_list = description_list + f"{hub_time_l} - {hub_name[a]}\n"
            a = a + 1
    else:
        print(f"!!!КОНФЛИКТ!!!\n{len(hub_name)} != {len(hub_time)}")
    def description_list_target_ALL(hub_time, hub_name, target_id):
        description_list_target = ""
        if len(hub_name) == len(hub_time):
            a = 0
            for hub_time_l in hub_time:
                ty_res = gmtime(hub_time_l)
                res = strftime("%H:%M:%S",ty_res)
                #print(res)
                if a == target_id:
                    description_list_target = description_list_target + f"➡️ `{res}` - {hub_name[a]} ⬅️\n"
                else:
                    description_list_target = description_list_target + f"🔘 `{res}` - {hub_name[a]}\n"
                a = a + 1
        else:
            print(f"!!!КОНФЛИКТ!!!\n{len(hub_name)} != {len(hub_time)}")
        #print(description_list_target)
        return description_list_target
    def ALA(start_position, hub_time, hub_name):
        M = 0
        for L in hub_time:
            if L >= start_position:
                if len(hub_name) >= M:
                    return hub_name[M - 1], M - 1
            M = M + 1
        return None, None
    slips_l = 10
    L_1 = "```\n╔════════════════════════════════╗\n"
    L_3 = "\n╚════════════════════════════════╝```"
    id_jgkihjkf = int(message.author.guild.id)
    a = 0
    for id_lin in SQL_Q[3]: # Узноём номер сообшений.
        if id_lin == message.channel.id:
            qm2 = int(SQL_Q[5][a])
            channel_id = message.channel.id
        a = a + 1
    print("Жив ?")
    await asyncio.sleep(5)
    start_position = int(start_position) + 5
    print("Жив ?2")
    msg_sa = await bot.get_guild(id_jgkihjkf).get_channel(channel_id).fetch_message(qm2)
    while bd_module.checking_the_timeline(index):
        time_p = time_SSS/100
        time_pS = int(start_position/time_p)
        i = int(int(time_pS)*0.3)
        L_2 = f"║ {'█' * i}{' ' * (30 - i)} ║ "
        time_SSS_Q = convert_to_preferred_format(time_SSS)
        start_position_Q = convert_to_preferred_format(start_position)
        name, target_id = ALA(start_position, hub_time, hub_name)
        if name == None:
            bot.loop.create_task(msg_sa.edit(content=(f"{lll}{L_1+L_2+L_3}{start_position_Q} - {time_SSS_Q} {time_pS}%")))
        else:
            if theme == 0:
                bot.loop.create_task(msg_sa.edit(content=(f"{lll}{L_1+L_2+L_3}{start_position_Q} - {time_SSS_Q} {time_pS}%\n➡️ {name} ⬅️")))
            elif theme == 1:
                bot.loop.create_task(msg_sa.edit(content=(f"{lll}{L_1+L_2+L_3}{start_position_Q} - {time_SSS_Q} {time_pS}%\n{description_list}")))
            elif theme == 2:
                description_list_target = description_list_target_ALL(hub_time, hub_name, target_id)
                bot.loop.create_task(msg_sa.edit(content=(f"{lll}{L_1+L_2+L_3}{start_position_Q} - {time_SSS_Q} {time_pS}%\n{description_list_target}")))
        await asyncio.sleep(slips_l)
        start_position = int(start_position) + slips_l



# END

