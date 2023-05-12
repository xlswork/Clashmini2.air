import pprint

from public_method import *


def click_unlocked():
    img_paths = get_image_paths("picture/collocation/locked/hero")
    find_list = []
    not_find_list = []
    for img_path in img_paths:
        if exists(Template(img_path, resolution=(1080, 2400), threshold=0.9)):
            touch(Template(img_path, resolution=(1080, 2400), threshold=0.9))
            """
                other things
            """
            if exists(
                    Template("./picture/collocation/button/collocation_button_close.png", resolution=(1080, 2400),
                             threshold=0.9)):
                touch(
                    Template("./picture/collocation/button/collocation_button_close.png", resolution=(1080, 2400),
                             threshold=0.9))
            find_list.append(img_path)
        else:
            print(img_path)
            not_find_list.append(img_path)
    pprint.pp(find_list)
    pprint.pp(not_find_list)


# 未解锁时点击技能
def click_skill_locked():
    pass


# 解锁英雄
def click_hero_unlocked():
    pass
