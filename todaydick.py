import datetime
import random

from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot import on_regex
from nonebot.permission import SUPERUSER

boki_status = ("勃起", "软掉")
phimosis_status = ("包茎", "半包茎", "非包茎")


def get_random_seed(qid: int):
    now = datetime.datetime.now()
    date_ = "".join(map(str, [now.year, now.month, now.day]))
    return qid * int(date_) % 1000000007


def get_boki_status(seed: int):
    random.seed(seed)
    return random.choice(boki_status)


def get_boki_angle(boki_stat: str, seed: int):
    if boki_stat == "勃起":
        random.seed(seed)
        return random.randint(10, 180)
    return 0


def get_phimosis_status(seed: int):
    random.seed(seed)
    return random.choice(phimosis_status)


def get_hardness(seed: int, boki_stat: str):
    random.seed(seed)
    if boki_stat == "勃起":
        return random.randint(2, 10)
    return random.randint(0, 4)


def get_length_comment(length: int, boki_stat: str):
    if boki_stat == "软掉":
        length *= 1.3

    if length > 20:
        return "哪来的兽人，怎么会这么长"
    elif length > 15:
        return "还是蛮长的"
    elif length > 10:
        return "达到平均水平啦"
    elif length >= 0:
        return "好短!"
    return "牛牛缩进去了？？？"


def get_eggs_weight(seed: int):
    random.seed(seed)
    return random.randint(1, 1000)


def get_length(seed: int, boki_stat: str):
    random.seed(seed)
    if boki_stat == "勃起":
        return random.randint(-5, 25)
    return random.randint(-10, 15)


def get_today_dick_status(user_id: int):
    rand_seed = get_random_seed(user_id)

    boki_stat = get_boki_status(rand_seed)
    angle = get_boki_angle(boki_stat, rand_seed)
    phimosis_stat = get_phimosis_status(rand_seed)
    hardness = get_hardness(rand_seed, boki_stat)
    eggs_weight = get_eggs_weight(rand_seed)
    length = get_length(rand_seed, boki_stat)
    comment = get_length_comment(length, boki_stat)
    if boki_stat == "勃起":
        return f"你今天有一根勃起的,boki角度为{angle}度的{phimosis_stat}的\
莫氏硬度为{hardness},并且蛋蛋{eggs_weight}克的{length}cm的牛子，{comment}"
    return f"你今天有一根软掉的,{phimosis_stat}的莫氏硬度为{hardness},并且\
蛋蛋{eggs_weight}克的{length}cm的牛子，{comment}"


my_dick = on_regex("^今天的牛子$", priority=50)


@my_dick.handle()
async def _(event: MessageEvent):
    await my_dick.finish(get_today_dick_status(event.user_id))
