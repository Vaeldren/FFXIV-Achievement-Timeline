from flask import Flask, jsonify
import asyncio
import requests
import datetime

app = Flask(__name__)

@app.route('/')
def get_achievements():
    r = requests.get('https://xivapi.com/character/22192778?data=AC')
    #get data - not hardcode for final
    data = r.json()
    #convert to json format
    achievements = data['Achievements']['List']
    #stores achievement list

    ids_to_check = {
     310: {"title": "The Lominsan Envoy", "description": "Embarked on a journey from the maritime city-state of Limsa Lominsa.", "patch": "A Realm Reborn patch 2.0", "type": "msq"},
    311: {"title": "The Gridanian Envoy", "description": "Embarked on a journey from the forest nation of Gridania.", "patch": "A Realm Reborn patch 2.0", "type": "msq"},
    312: {"title": "The Ul'dah Envoy", "description": "Embarked on a journey from the desert city-state of Ul'dah.", "patch": "A Realm Reborn patch 2.0", "type": "msq"},
    788: {"title": "The Ultimate Weapon", "description": "Defeated the Ultima Weapon and brought down the head of the XIVth Imperial Legion, Gaius van Baelsar.", "patch": "A Realm Reborn patch 2.0", "type": "msq"},
    1129: {"title": "Before the Fall", "description": "Sought asylum in Ishgard after the Scions were betrayed by the Crystal Braves and torn apart by political schemes, leading to their separation.", "patch": "A Realm Reborn patch 2.5", "type": "msq"},
    1139: {"title": "Heavensward", "description": "Ventured into the land of Ishgard and fought against the heretics, dragons, and the Archbishop himself, ultimately learning the true history of the Dragonsong War.", "patch": "Heavensward patch 3.0", "type": "msq"},
    1691: {"title": "The Far Edge of Fate", "description": "Attempted to halt Ilberd's summoning of the primal Shinryu but ultimately failed, spurring the Alliance to take action towards the liberation of Ala Mhigo.", "patch": "Heavensward patch 3.5", "type": "msq"},
    1794: {"title": "Stormblood", "description": "Liberated the nations of Ala Mhigo and Doma from Garlean occupation, defeating the possessed Shinryu and its controller Zenos yae Galvus, leader of the XIIth Imperial Legion.", "patch": "Stormblood patch 4.0", "type": "msq"},
    2233: {"title": "A Requiem for Heroes", "description": "Charged by a cryptic robed figure with the task of investigating the Crystal Tower to find the key to saving the comatose Scions.", "patch": "Stormblood patch 4.5","type": "msq"},
    2298: {"title": "Shadowbringers", "description": "Traversed the realm of the First and restored balance to a world ravaged by the Flood of Light by defeating Emet-Selch, learning much of the Ascian's true motives.", "patch": "Shadowbringers patch 5.0", "type": "msq"},
    2851: {"title": "Death Unto Dawn", "description": "Confronted the threat of the Telophoroi's lunar primals and worked to thwart Fandaniel's machinations with the help of the Alliance.", "patch": "Shadowbringers patch 5.5", "type": "msq"},
    2958: {"title": "Endwalker", "description": "Embarked on a journey beyond the stars to save the universe from the impending doom of the Final Days and faced off against Meteion, the incarnation of despair.", "patch": "Endwalker patch 6.0", "type": "msq"},
    
    1231: {"title": "Sins of the Savage Father I", "description": "Complete Alexander: Gordias (Savage).", "patch": "Heavensward patch 3.0", "type": "raid"},
    1399: {"title": "Touching the Void", "description": "Complete the Void Ark.", "patch": "Heavensward patch 3.1", "type": "raid"},
    1479: {"title": "Sins of the Savage Son I", "description": "Complete Alexander: Midas (Savage).", "patch": "Heavensward patch 3.2", "type": "raid"},
    1574: {"title": "Ex Mhachina", "description": "Complete the Weeping City of Mhach.", "patch": "Heavensward patch 3.3", "type": "raid"},
    1642: {"title": "Sins of the Savage Creator I", "description": "Complete Alexander: The Creator (Savage).", "patch": "Heavensward patch 3.4", "type": "raid"},
    1689: {"title": "What's Dun Is Done", "description": "Complete Dun Scaith.", "patch": "Heavensward patch 3.5", "type": "raid"},
    1898: {"title": "I Am the Savage Delta, I Am the Savage Omega I", "description": "Complete Omega: Deltascape (Savage).", "patch": "Stormblood patch 4.0", "type": "raid"},
    1992: {"title": "Zodiac Thriller", "description": "Complete the Royal City of Rabanastre.", "patch": "Stormblood patch 4.1", "type": "raid"},
    1993: {"title": "Resistance Is Futile", "description": "Defeat Bahamut Prime in the Unending Coil of Bahamut (Ultimate).", "patch": "Stormblood patch 4.1", "type": "raid"},
    2027: {"title": "I Am the Savage Sigma, I Am the Savage Omega I", "description": "Complete Omega: Sigmascape (Savage).", "patch": "Stormblood patch 4.2", "type": "raid"},
    2106: {"title": "Didn't Stop, Made It Pop", "description": "Complete the Ridorana Lighthouse.", "patch": "Stormblood patch 4.3", "type": "raid"},
    2107: {"title": "Ultimatum", "description": "Defeat the Ultima Weapon in the Weapon's Refrain (Ultimate).", "patch": "Stormblood patch 4.3", "type": "raid"},
    2121: {"title": "I Am the Savage Alpha, I Am the Savage Omega I", "description": "Complete Omega: Alphascape (Savage).", "patch": "Stormblood patch 4.4", "type": "raid"},
    2164: {"title": "Orbonne to Pick", "description": "Complete the Orbonne Monastery.", "patch": "Stormblood patch 4.5", "type": "raid"},
    2412: {"title": "Savage Paradise Found I", "description": "Complete Eden's Gate (Savage).", "patch": "Shadowbringers patch 5.0", "type": "raid"},
    2443: {"title": "The First Law", "description": "Complete the Copied Factory.", "patch": "Shadowbringers patch 5.1", "type": "raid"},
    2444: {"title": "When I Ruled the World", "description": "Defeat Perfect Alexander in the Epic of Alexander (Ultimate).", "patch": "Shadowbringers patch 5.1", "type": "raid"},
    2594: {"title": "Savage Trouble in Paradise I", "description": "Complete Eden's Verse (Savage).", "patch": "Shadowbringers patch 5.2", "type": "raid"},
    2622: {"title": "Uncanny Valley", "description": "Complete the Puppets' Bunker.", "patch": "Shadowbringers patch 5.3", "type": "raid"},
    2722: {"title": "Savage Paradise Within Thee I", "description": "Complete Eden's Promise (Savage).", "patch": "Shadowbringers patch 5.4", "type": "raid"},
    2847: {"title": "Deus et Machina", "description": "Complete the Tower at Paradigm's Breach.", "patch": "Shadowbringers patch 5.5", "type": "raid"},
    3038: {"title": "Could Be Savage I", "description": "Complete Pandæmonium: Asphodelos (Savage).", "patch": "Endwalker patch 6.0", "type": "raid"},
    3073: {"title": "Divine Intervention", "description": "Complete Aglaia.", "patch": "Endwalker patch 6.1", "type": "raid"},
    3074: {"title": "As Suits a Hero", "description": "Complete Dragonsong's Reprise (Ultimate).", "patch": "Endwalker patch 6.1", "type": "raid"},
    3111: {"title": "Savage Gaze of the Abyss I", "description": "Complete Pandæmonium: Abyssos (Savage).", "patch": "Endwalker patch 6.2", "type": "raid"},
    3161: {"title": "Divine Revelry", "description": "Complete Euphrosyne.", "patch": "Endwalker patch 6.3", "type": "raid"},
    3162: {"title": "Heart to Heartless", "description": "See Omega's experiment to its ultimate conclusion in the Omega Protocol (Ultimate).", "patch": "Endwalker patch 6.3", "type": "raid"}
    }
    #ids to check, also add images
    
    results = {string: None for string in ids_to_check.values()}

    for achievement in achievements:
        id =  achievement['id']
        datestr = achievement['date']
        date = datetime.datetime.strptime(datestr, '%d%m%y %H%M%S')

        if id in ids_to_check:
            data = ids_to_check[id]
            results[id] = {
                'date': date,
                'description': data['description'],
                'patch': data['patch'],
                'type': data['type']
            }

            if all(date is not None for date in results.values()):
                break

    return jsonify(results)

if __name__ == '__main__':
    app.run()
