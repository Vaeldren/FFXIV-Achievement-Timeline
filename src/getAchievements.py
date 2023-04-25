import asyncio
import aiohttp
import logging
import requests
import pyxivapi
import datetime

async def getAchievements(link):

    r = requests.get('https://xivapi.com/character/22192778?data=AC')
    #gets achievement data

    data = r.json()
    #stores in json format - readable

    achievements = data['Achievements']['List']
    #stores achievement list

    #sort by date
    #look for certain ids that show progression - start, arr, hw, sb, shb, ew
    #310 lominsa, 311 grid, 312 uldah (envoy)
    #788 2.0 fin
    #1001 2.3 fin (crystal braves formed)
    #1129 2.55 fin
    #1139 3.0 fin
    #1594 3.3 fin (nidhogg dead)
    #1630 3.4 fin (all scions back, wod gone)
    #1691 3.55 fin
    #1787 4.0 (just entered kugane)
    #1792 4.0 kugane fin
    #1794 4.0 fin
    #2233 4.55 fin
    #2293 5.0 start (first lightwarden dead)
    #2298 5.0 fin
    #2642 5.3 fin (back to source)
    #2851 5.55 fin
    #2952 6.0 start (tower of zot done)
    #2958 6.0 end
    #3075 6.1 end (newfound adventure)
    #3105 6.2 end (adventure into void)

    ids_to_check = {310:"limsa lominsa start",
                    311:"gridania start",
                    312:"uldah start",
                    788:"ARR 2.0 finished",
                    1001:"ARR 2.3 finished",
                    1129:"ARR 2.55 finished",
                    1139:"HW 3.0 finished",
                    1594:"HW 3.3 finished",
                    1691:"HW 3.55 finished",
                    1794:"SB 4.0 finished",
                    2233:"SB 4.55 fin",
                    2298:"SHB 5.0 fin",
                    2642:"SHB 5.3 fin",
                    2851:"SHB 5.55 fin",
                    2958:"EW 6.0 fin",}    
    #ids to check
    
    results = {string: None for string in ids_to_check.values()}
    #dictionary

    for achievement in achievements:
        id =  achievement['id']
        datestr = achievement['date']
        date = datetime.strptime(datestr, '%d%m%y %H%M%S') #stores date in datetime

        if id in ids_to_check:
            results[id] = date #uses id to locate position and store date

            if all(date is not None for date in results.values()):
                break





if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='%H:%M')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getAchievements())
