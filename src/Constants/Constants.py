from pydantic_settings import BaseSettings, SettingsConfigDict


class Constants(BaseSettings):

    gameVersion:str = "4.2.3.3.0"
    apiPoints_VERSION:str = "https://static.drips.pw/rotmg/production/current/version.txt"
    apiPoints_EQUIP:str = "https://static.drips.pw/rotmg/production/current/xml/Equip.xml"
    apiPoints_VERIFY:str = "https://www.realmofthemadgod.com/account/verify"
    apiPoints_VERIFYTOKEN:str = "https://www.realmofthemadgod.com/account/verifyAccessTokenClient"
    apiPoints_CHAR:str = "https://www.realmofthemadgod.com/char/list"
    apiPoints_SERVERS:str = "https://www.realmofthemadgod.com/account/servers"

    MINSPEED:float = 0.004
    MAXSPEED:float = 0.0096

    MINFREQ:float = 0.0015
    MAXFREQ:float = 0.008


    apiPoints_launcherHeaders:dict = {
        "User-Agent": "UnityPlayer/2021.3.16f1 (UnityWebRequest/1.0, libcurl/7.84.0-DEV)",
        "X-Unity-Version": "2021.3.16f1"
    }

    apiPoints_exaltHeaders:dict = {
        "User-Agent": "UnityPlayer/2021.3.16f1 (UnityWebRequest/1.0, libcurl/7.84.0-DEV)",
        "X-Unity-Version": "2021.3.16f1"
    }
    CharacterClasses:dict = {
        "ROGUE": 768,
        "ARCHER": 775,
        "WIZARD": 782,
        "PRIEST": 784,
        "WARRIOR": 797,
        "KNIGHT": 798,
        "PALADIN": 799,
        "ASSASSIN": 800,
        "NECROMANCER": 801,
        "HUNTRESS": 802,
        "MYSTIC": 803,
        "TRICKSTER": 804,
        "SORCERER": 805,
        "NINJA": 806,
        "SAMURAI": 785,
        "BARD": 796,
        "SUMMONER": 817,
        "KENSEI": 818
    }
    gameIds:dict = {
        "tutorial": -1,
        "nexus": -2,
        "randomRealm": -3,
        "vault": -5,
        "mapTest": -6,
        "vaultExplanation": -8,
        "nexusExplanation": -9,
        "questRoom": -11,
        "cheatersQuarantine": -13
    }
    idToType:dict = {
        0: "FAILURE",
        1: "TELEPORT",
        3: "CLAIMDAILYLOGINREWARD",
        4: "DELETEPET",
        5: "REQUESTTRADE",
        6: "QUESTFETCHRESPONSE",
        7: "JOINGUILD",
        8: "PING",
        9: "PLAYERTEXT",
        10: "NEWTICK",
        11: "SHOWEFFECT",
        12: "SERVERPLAYERSHOOT",
        13: "USEITEM",
        14: "TRADEACCEPTED",
        15: "GUILDREMOVE",
        16: "PETUPGRADEREQUEST",
        17: "ENTERARENA",
        18: "GOTO",
        19: "INVDROP",
        20: "OTHERHIT",
        21: "NAMERESULT",
        22: "BUYRESULT",
        23: "HATCHPET",
        24: "ACTIVEPETUPDATEREQUEST",
        25: "ENEMYHIT",
        26: "GUILDRESULT",
        27: "EDITACCOUNTLIST",
        28: "TRADECHANGED",
        30: "PLAYERSHOOT",
        31: "PONG",
        33: "CHANGEPETSKIN",
        34: "TRADEDONE",
        35: "ENEMYSHOOT",
        36: "ACCEPTTRADE",
        37: "CHANGEGUILDRANK",
        38: "PLAYSOUND",
        39: "VERIFYEMAIL",
        40: "SQUAREHIT",
        41: "NEWABILITY",
        42: "UPDATE",
        44: "TEXT",
        45: "RECONNECT",
        46: "DEATH",
        47: "USEPORTAL",
        48: "GOTOQUESTROOM",
        49: "ALLYSHOOT",
        50: "IMMINENTARENAWAVE",
        51: "RESKIN",
        52: "RESETDAILYQUESTS",
        53: "PETCHANGEFORMMSG",
        55: "INVSWAP",
        56: "CHANGETRADE",
        57: "CREATE",
        58: "QUESTREDEEM",
        59: "CREATEGUILD",
        60: "SETCONDITION",
        61: "LOAD",
        62: "MOVE",
        63: "KEYINFORESPONSE",
        64: "AOE",
        65: "GOTOACK",
        66: "GLOBALNOTIFICATION",
        67: "NOTIFICATION",
        68: "ARENADEATH",
        69: "CLIENTSTAT",
        74: "HELLO",
        75: "DAMAGE",
        76: "ACTIVEPETUPDATE",
        77: "INVITEDTOGUILD",
        78: "PETYARDUPDATE",
        79: "PASSWORDPROMPT",
        80: "ACCEPTARENADEATH",
        81: "UPDATEACK",
        82: "QUESTOBJID",
        83: "PIC",
        84: "REALMHEROESRESPONSE",
        85: "BUY",
        86: "TRADESTART",
        87: "EVOLVEPET",
        88: "TRADEREQUESTED",
        89: "AOEACK",
        90: "PLAYERHIT",
        91: "CANCELTRADE",
        92: "MAPINFO",
        93: "CLAIMDAILYLOGINRESPONSE",
        94: "KEYINFOREQUEST",
        95: "INVRESULT",
        96: "QUESTREDEEMRESPONSE",
        97: "CHOOSENAME",
        98: "QUESTFETCHASK",
        99: "ACCOUNTLIST",
        100: "SHOOTACK",
        101: "CREATESUCCESS",
        102: "CHECKCREDITS",
        103: "GROUNDDAMAGE",
        104: "GUILDINVITE",
        105: "ESCAPE",
        106: "FILE",
        107: "RESKINUNLOCK",
        108: "NEWCHARACTERINFORMATION",
        109: "UNLOCKINFORMATION",
        112: "QUEUEINFORMATION",
        114: "EXALTATIONUPDATE",
        117: "VAULTINFO",
        118: "FORGEREQUEST",
        119: "FORGERESPONSE",
        120: "BLUEPRINTINFO",
        121: "ENEMYSHOOTACK",
        122: "SHOWALLYSHOOT",
        139: "UNKNOWN139",
        149: "CLAIMBATTLEPASS",
        150: "CLAIMBATTLEPASSRESPONSE",
        159: "SENDEMOTE",
        165: "UNKNOWN165",
        169: "REALMSCORE",
        182: "CRUCIBLEREQUEST",
        183: "CRUCIBLERESPONSE",
        206: "CHATHELLOMSG",
        207: "CHATTOKENMSG",
        208: "CHATLOGOUTMSG"}
    typeToId:dict = {
    "FAILURE": 0,
    "TELEPORT": 1,
    "CLAIMDAILYLOGINREWARD": 3,
    "DELETEPET": 4,
    "REQUESTTRADE": 5,
    "QUESTFETCHRESPONSE": 6,
    "JOINGUILD": 7,
    "PING": 8,
    "PLAYERTEXT": 9,
    "NEWTICK": 10,
    "SHOWEFFECT": 11,
    "SERVERPLAYERSHOOT": 12,
    "USEITEM": 13,
    "TRADEACCEPTED": 14,
    "GUILDREMOVE": 15,
    "PETUPGRADEREQUEST": 16,
    "ENTERARENA": 17,
    "GOTO": 18,
    "INVDROP": 19,
    "OTHERHIT": 20,
    "NAMERESULT": 21,
    "BUYRESULT": 22,
    "HATCHPET": 23,
    "ACTIVEPETUPDATEREQUEST": 24,
    "ENEMYHIT": 25,
    "GUILDRESULT": 26,
    "EDITACCOUNTLIST": 27,
    "TRADECHANGED": 28,
    "PLAYERSHOOT": 30,
    "PONG": 31,
    "CHANGEPETSKIN": 33,
    "TRADEDONE": 34,
    "ENEMYSHOOT": 35,
    "ACCEPTTRADE": 36,
    "CHANGEGUILDRANK": 37,
    "PLAYSOUND": 38,
    "VERIFYEMAIL": 39,
    "SQUAREHIT": 40,
    "NEWABILITY": 41,
    "UPDATE": 42,
    "TEXT": 44,
    "RECONNECT": 45,
    "DEATH": 46,
    "USEPORTAL": 47,
    "GOTOQUESTROOM": 48,
    "ALLYSHOOT": 49,
    "IMMINENTARENAWAVE": 50,
    "RESKIN": 51,
    "RESETDAILYQUESTS": 52,
    "PETCHANGEFORMMSG": 53,
    "INVSWAP": 55,
    "CHANGETRADE": 56,
    "CREATE": 57,
    "QUESTREDEEM": 58,
    "CREATEGUILD": 59,
    "SETCONDITION": 60,
    "LOAD": 61,
    "MOVE": 62,
    "KEYINFORESPONSE": 63,
    "AOE": 64,
    "GOTOACK": 65,
    "GLOBALNOTIFICATION": 66,
    "NOTIFICATION": 67,
    "ARENADEATH": 68,
    "CLIENTSTAT": 69,
    "HELLO": 74,
    "DAMAGE": 75,
    "ACTIVEPETUPDATE": 76,
    "INVITEDTOGUILD": 77,
    "PETYARDUPDATE": 78,
    "PASSWORDPROMPT": 79,
    "ACCEPTARENADEATH": 80,
    "UPDATEACK": 81,
    "QUESTOBJID": 82,
    "PIC": 83,
    "REALMHEROESRESPONSE": 84,
    "BUY": 85,
    "TRADESTART": 86,
    "EVOLVEPET": 87,
    "TRADEREQUESTED": 88,
    "AOEACK": 89,
    "PLAYERHIT": 90,
    "CANCELTRADE": 91,
    "MAPINFO": 92,
    "CLAIMDAILYLOGINRESPONSE": 93,
    "KEYINFOREQUEST": 94,
    "INVRESULT": 95,
    "QUESTREDEEMRESPONSE": 96,
    "CHOOSENAME": 97,
    "QUESTFETCHASK": 98,
    "ACCOUNTLIST": 99,
    "SHOOTACK": 100,
    "CREATESUCCESS": 101,
    "CHECKCREDITS": 102,
    "GROUNDDAMAGE": 103,
    "GUILDINVITE": 104,
    "ESCAPE": 105,
    "FILE": 106,
    "RESKINUNLOCK": 107,
    "NEWCHARACTERINFORMATION": 108,
    "UNLOCKINFORMATION": 109,
    "QUEUEINFORMATION": 112,
    "EXALTATIONUPDATE": 114,
    "VAULTINFO": 117,
    "FORGEREQUEST": 118,
    "FORGERESPONSE": 119,
    "BLUEPRINTINFO": 120,
    "ENEMYSHOOTACK": 121,
    "SHOWALLYSHOOT": 122,
    "UNKNOWN139": 139,
    "CLAIMBATTLEPASS": 149,
    "CLAIMBATTLEPASSRESPONSE": 150,
    "SENDEMOTE": 159,
    "UNKNOWN165": 165,
    "REALMSCORE": 169,
    "CRUCIBLEREQUEST": 182,
    "CRUCIBLERESPONSE": 183,
    "CHATHELLOMSG": 206,
    "CHATTOKENMSG": 207,
    "CHATLOGOUTMSG": 208
    }

    nameToIp:dict = {
        'EUEast': '18.184.218.174',
        'EUSouthWest': '35.180.67.120',
        'USEast2': '54.209.152.223',
        'EUNorth': '18.159.133.120',
        'USEast': '54.234.226.24',
        'USWest4': '54.235.235.140',
        'EUWest2': '52.16.86.215',
        'Asia': '3.0.147.127',
        'USSouth3': '52.207.206.31',
        'EUWest': '15.237.60.223',
        'USWest': '54.86.47.176',
        'USMidWest2': '3.140.254.133',
        'USMidWest': '18.221.120.59',
        'USSouth': '3.82.126.16',
        'USWest3': '18.144.30.153',
        'USSouthWest': '54.153.13.68',
        'USNorthWest': '34.238.176.119',
        'Australia': '13.236.87.250'
    }
    ipToName:dict = {
    '18.184.218.174': 'EUEast',
    '35.180.67.120': 'EUSouthWest',
    '54.209.152.223': 'USEast2',
    '18.159.133.120': 'EUNorth',
    '54.234.226.24': 'USEast',
    '54.235.235.140': 'USWest4',
    '52.16.86.215': 'EUWest2',
    '3.0.147.127': 'Asia',
    '52.207.206.31': 'USSouth3',
    '15.237.60.223': 'EUWest',
    '54.86.47.176': 'USWest',
    '3.140.254.133': 'USMidWest2',
    '18.221.120.59': 'USMidWest',
    '3.82.126.16': 'USSouth',
    '18.144.30.153': 'USWest3',
    '54.153.13.68': 'USSouthWest',
    '34.238.176.119': 'USNorthWest',
    '13.236.87.250': 'Australia'
    }

    intToStatTypes:dict = {
        0: 'MAXHPSTAT',
        1: 'HPSTAT',
        2: 'SIZESTAT',
        3: 'MAXMPSTAT',
        4: 'MPSTAT',
        5: 'NEXTLEVELEXPSTAT',
        6: 'EXPSTAT',
        7: 'LEVELSTAT',
        8: 'INVENTORY0STAT',
        9: 'INVENTORY1STAT',
        10: 'INVENTORY2STAT',
        11: 'INVENTORY3STAT',
        12: 'INVENTORY4STAT',
        13: 'INVENTORY5STAT',
        14: 'INVENTORY6STAT',
        15: 'INVENTORY7STAT',
        16: 'INVENTORY8STAT',
        17: 'INVENTORY9STAT',
        18: 'INVENTORY10STAT',
        19: 'INVENTORY11STAT',
        20: 'ATTACKSTAT',
        21: 'DEFENSESTAT',
        22: 'SPEEDSTAT',
        25: 'TEXTURESTAT',
        26: 'VITALITYSTAT',
        27: 'WISDOMSTAT',
        28: 'DEXTERITYSTAT',
        29: 'CONDITIONSTAT',
        30: 'NUMSTARSSTAT',
        31: 'NAMESTAT',
        32: 'TEX1STAT',
        33: 'TEX2STAT',
        34: 'MERCHANDISETYPESTAT',
        35: 'CREDITSSTAT',
        36: 'MERCHANDISEPRICESTAT',
        37: 'ACTIVESTAT',
        38: 'ACCOUNTIDSTAT',
        39: 'FAMESTAT',
        40: 'MERCHANDISECURRENCYSTAT',
        41: 'CONNECTSTAT',
        42: 'MERCHANDISECOUNTSTAT',
        43: 'MERCHANDISEMINSLEFTSTAT',
        44: 'MERCHANDISEDISCOUNTSTAT',
        45: 'MERCHANDISERANKREQSTAT',
        46: 'MAXHPBOOSTSTAT',
        47: 'MAXMPBOOSTSTAT',
        48: 'ATTACKBOOSTSTAT',
        49: 'DEFENSEBOOSTSTAT',
        50: 'SPEEDBOOSTSTAT',
        51: 'VITALITYBOOSTSTAT',
        52: 'WISDOMBOOSTSTAT',
        53: 'DEXTERITYBOOSTSTAT',
        54: 'OWNERACCOUNTIDSTAT',
        55: 'RANKREQUIREDSTAT',
        56: 'NAMECHOSENSTAT',
        57: 'CURRFAMESTAT',
        58: 'NEXTCLASSQUESTFAMESTAT',
        59: 'LEGENDARYRANKSTAT',
        60: 'SINKLEVELSTAT',
        61: 'ALTTEXTURESTAT',
        62: 'GUILDNAMESTAT',
        63: 'GUILDRANKSTAT',
        64: 'BREATHSTAT',
        65: 'XPBOOSTEDSTAT',
        66: 'XPTIMERSTAT',
        67: 'LDTIMERSTAT',
        68: 'LTTIMERSTAT',
        69: 'HEALTHPOTIONSTACKSTAT',
        70: 'MAGICPOTIONSTACKSTAT',
        71: 'DUSTAMOUNT',
        72: 'DUSTLIMIT',
        79: 'HASBACKPACKSTAT',
        80: 'ENCHANTMENTS',
        81: 'PETINSTANCEIDSTAT',
        82: 'PETNAMESTAT',
        83: 'PETTYPESTAT',
        84: 'PETRARITYSTAT',
        85: 'PETMAXABILITYPOWERSTAT',
        86: 'PETFAMILYSTAT',
        87: 'PETFIRSTABILITYPOINTSTAT',
        88: 'PETSECONDABILITYPOINTSTAT',
        89: 'PETTHIRDABILITYPOINTSTAT',
        90: 'PETFIRSTABILITYPOWERSTAT',
        91: 'PETSECONDABILITYPOWERSTAT',
        92: 'PETTHIRDABILITYPOWERSTAT',
        93: 'PETFIRSTABILITYTYPESTAT',
        94: 'PETSECONDABILITYTYPESTAT',
        95: 'PETTHIRDABILITYTYPESTAT',
        96: 'NEWCONSTAT',
        97: 'FORTUNETOKENSTAT',
        98: 'SUPPORTERPOINTSSTAT',
        99: 'SUPPORTERSTAT',
        100: 'CHALLENGERSTARBGSTAT',
        102: 'PROJECTILESPEEDMULT',
        103: 'PROJECTILELIFEMULT',
        104: 'OPENEDATTIMESTAMP',
        105: 'EXALTEDATK',
        106: 'EXALTEDDEFENSE',
        107: 'EXALTEDSPD',
        108: 'EXALTEDVIT',
        109: 'EXALTEDWIS',
        110: 'EXALTEDDEX',
        111: 'EXALTEDHP',
        112: 'EXALTEDMP',
        113: 'EXALTATIONBONUSDMG',
        114: 'EXALTATIONICREDUCTION',
        115: 'GRAVEACCOUNTID',
        116: 'POTIONONETYPE',
        117: 'POTIONTWOTYPE',
        118: 'POTIONTHREETYPE',
        119: 'POTIONBELT',
        120: 'FORGEFIRE',
        121: 'UNKNOWN121',
        123: 'UNKNOWN123',
        127: 'UNKNOWN127',
        128: 'UNKNOWN128',
        131: 'BACKPACK0STAT',
        132: 'BACKPACK1STAT',
        133: 'BACKPACK2STAT',
        134: 'BACKPACK3STAT',
        135: 'BACKPACK4STAT',
        136: 'BACKPACK5STAT',
        137: 'BACKPACK6STAT',
        138: 'BACKPACK7STAT',
        147: 'UNKNOWN147'}
    statTypesToInt:dict = {
    "MAXHPSTAT": 0,
    "HPSTAT": 1,
    "SIZESTAT": 2,
    "MAXMPSTAT": 3,
    "MPSTAT": 4,
    "NEXTLEVELEXPSTAT": 5,
    "EXPSTAT": 6,
    "LEVELSTAT": 7,
    "INVENTORY0STAT": 8,
    "INVENTORY1STAT": 9,
    "INVENTORY2STAT": 10,
    "INVENTORY3STAT": 11,
    "INVENTORY4STAT": 12,
    "INVENTORY5STAT": 13,
    "INVENTORY6STAT": 14,
    "INVENTORY7STAT": 15,
    "INVENTORY8STAT": 16,
    "INVENTORY9STAT": 17,
    "INVENTORY10STAT": 18,
    "INVENTORY11STAT": 19,
    "ATTACKSTAT": 20,
    "DEFENSESTAT": 21,
    "SPEEDSTAT": 22,
    "TEXTURESTAT": 25,
    "VITALITYSTAT": 26,
    "WISDOMSTAT": 27,
    "DEXTERITYSTAT": 28,
    "CONDITIONSTAT": 29,
    "NUMSTARSSTAT": 30,
    "NAMESTAT": 31,
    "TEX1STAT": 32,
    "TEX2STAT": 33,
    "MERCHANDISETYPESTAT": 34,
    "CREDITSSTAT": 35,
    "MERCHANDISEPRICESTAT": 36,
    "ACTIVESTAT": 37,
    "ACCOUNTIDSTAT": 38,
    "FAMESTAT": 39,
    "MERCHANDISECURRENCYSTAT": 40,
    "CONNECTSTAT": 41,
    "MERCHANDISECOUNTSTAT": 42,
    "MERCHANDISEMINSLEFTSTAT": 43,
    "MERCHANDISEDISCOUNTSTAT": 44,
    "MERCHANDISERANKREQSTAT": 45,
    "MAXHPBOOSTSTAT": 46,
    "MAXMPBOOSTSTAT": 47,
    "ATTACKBOOSTSTAT": 48,
    "DEFENSEBOOSTSTAT": 49,
    "SPEEDBOOSTSTAT": 50,
    "VITALITYBOOSTSTAT": 51,
    "WISDOMBOOSTSTAT": 52,
    "DEXTERITYBOOSTSTAT": 53,
    "OWNERACCOUNTIDSTAT": 54,
    "RANKREQUIREDSTAT": 55,
    "NAMECHOSENSTAT": 56,
    "CURRFAMESTAT": 57,
    "NEXTCLASSQUESTFAMESTAT": 58,
    "LEGENDARYRANKSTAT": 59,
    "SINKLEVELSTAT": 60,
    "ALTTEXTURESTAT": 61,
    "GUILDNAMESTAT": 62,
    "GUILDRANKSTAT": 63,
    "BREATHSTAT": 64,
    "XPBOOSTEDSTAT": 65,
    "XPTIMERSTAT": 66,
    "LDTIMERSTAT": 67,
    "LTTIMERSTAT": 68,
    "HEALTHPOTIONSTACKSTAT": 69,
    "MAGICPOTIONSTACKSTAT": 70,
    "DUSTAMOUNT": 71,
    "DUSTLIMIT": 72,
    "HASBACKPACKSTAT": 79,
    "ENCHANTMENTS": 80,
    "PETINSTANCEIDSTAT": 81,
    "PETNAMESTAT": 82,
    "PETTYPESTAT": 83,
    "PETRARITYSTAT": 84,
    "PETMAXABILITYPOWERSTAT": 85,
    "PETFAMILYSTAT": 86,
    "PETFIRSTABILITYPOINTSTAT": 87,
    "PETSECONDABILITYPOINTSTAT": 88,
    "PETTHIRDABILITYPOINTSTAT": 89,
    "PETFIRSTABILITYPOWERSTAT": 90,
    "PETSECONDABILITYPOWERSTAT": 91,
    "PETTHIRDABILITYPOWERSTAT": 92,
    "PETFIRSTABILITYTYPESTAT": 93,
    "PETSECONDABILITYTYPESTAT": 94,
    "PETTHIRDABILITYTYPESTAT": 95,
    "NEWCONSTAT": 96,
    "FORTUNETOKENSTAT": 97,
    "SUPPORTERPOINTSSTAT": 98,
    "SUPPORTERSTAT": 99,
    "CHALLENGERSTARBGSTAT": 100,
    "PROJECTILESPEEDMULT": 102,
    "PROJECTILELIFEMULT": 103,
    "OPENEDATTIMESTAMP": 104,
    "EXALTEDATK": 105,
    "EXALTEDDEFENSE": 106,
    "EXALTEDSPD": 107,
    "EXALTEDVIT": 108,
    "EXALTEDWIS": 109,
    "EXALTEDDEX": 110,
    "EXALTEDHP": 111,
    "EXALTEDMP": 112,
    "EXALTATIONBONUSDMG": 113,
    "EXALTATIONICREDUCTION": 114,
    "GRAVEACCOUNTID": 115,
    "POTIONONETYPE": 116,
    "POTIONTWOTYPE": 117,
    "POTIONTHREETYPE": 118,
    "POTIONBELT": 119,
    "FORGEFIRE": 120,
    "UNKNOWN121": 121,
    "UNKNOWN123": 123,
    "UNKNOWN127": 127,
    "UNKNOWN128": 128,
    "BACKPACK0STAT": 131,
    "BACKPACK1STAT": 132,
    "BACKPACK2STAT": 133,
    "BACKPACK3STAT": 134,
    "BACKPACK4STAT": 135,
    "BACKPACK5STAT": 136,
    "BACKPACK6STAT": 137,
    "BACKPACK7STAT": 138,
    "UNKNOWN147": 147
    }
    ConditionEffects:dict = {
    "NOTHING": 0,
    "DEAD": 1,
    "QUIET": 2,
    "WEAK": 3,
    "SLOWED": 4,
    "SICK": 5,
    "DAZED": 6,
    "STUNNED": 7,
    "BLIND": 8,
    "HALLUCINATING": 9,
    "DRUNK": 10,
    "CONFUSED": 11,
    "STUNIMMUNE": 12,
    "INVISIBLE": 13,
    "PARALYZED": 14,
    "SPEEDY": 15,
    "BLEEDING": 16,
    "ARMORBROKENIMMUNE": 17,
    "HEALING": 18,
    "DAMAGING": 19,
    "BERSERK": 20,
    "PAUSED": 21,
    "STASIS": 22,
    "STASISIMMUNE": 23,
    "INVINCIBLE": 24,
    "INVULNERABLE": 25,
    "ARMORED": 26,
    "ARMORBROKEN": 27,
    "HEXED": 28,
    "NINJASPEEDY": 29,
    "UNSTABLE": 30,
    "DARKNESS": 31,
    "SLOWEDIMMUNE": 32,
    "DAZEDIMMUNE": 33,
    "PARALYZEDIMMUNE": 34,
    "PETRIFIED": 35,
    "PETRIFIEDIMMUNE": 36,
    "PETEFFECTICON": 37,
    "CURSE": 38,
    "CURSEIMMUNE": 39,
    "HPBOOST": 40,
    "MPBOOST": 41,
    "ATTBOOST": 42,
    "DEFBOOST": 43,
    "SPDBOOST": 44,
    "VITBOOST": 45,
    "WISBOOST": 46,
    "DEXBOOST": 47,
    "SILENCED": 48,
    "EXPOSED": 49,
    "ENERGIZED": 50,
    "HPDEBUFF": 51,
    "MPDEBUFF": 52,
    "ATTDEBUFF": 53,
    "DEFDEBUFF": 54,
    "SPDDEBUFF": 55,
    "VITDEBUFF": 56,
    "WISDEBUFF": 57,
    "DEXDEBUFF": 58,
    "INSPIRED": 59,
    "GROUNDDAMAGE": 99
    }  

