import pprint

from public_method import *


def click_unlocked():
    images_info = get_image_paths_2("D:\\WorkingCode\\Clashmini2.air\\picture\\collocation\\locked\\hero\\")
    find_list = []
    not_find_list = []
    pprint.pp(images_info)
    for image_info in images_info:
        if exists(Template(image_info["image_path"], resolution=(1080, 2400), threshold=0.9)):
            touch(Template(image_info["image_path"], resolution=(1080, 2400), threshold=0.9))
            """
                other things
            """
            if image_info["name"] == "COUNTESS":
                click_skill_locked(image_info)
            click_hero_unlocked()
            if exists(
                    Template("./picture/collocation/button/button_quit.png", resolution=(1080, 2400), threshold=0.9)):
                touch(
                    Template("./picture/collocation/button/button_quit.png", resolution=(1080, 2400), threshold=0.9))
            find_list.append(image_info["name"])
        else:
            not_find_list.append(image_info["name"])
    pprint.pp(find_list)
    pprint.pp(not_find_list)


# 未解锁时点击技能
def click_skill_locked(image_info: dict):
    for skill_locked in image_info['skills_locked']:
        if exists(Template(skill_locked, resolution=(1080, 2400), threshold=0.9)):
            touch(Template(skill_locked, resolution=(1080, 2400), threshold=0.9))
            for skill_unlocked in image_info['skills_unlocked']:
                if exists(Template(skill_unlocked, resolution=(1080, 2400), threshold=0.9)):
                    touch(Template(skill_unlocked, resolution=(1080, 2400), threshold=0.9))
            touch(Template("picture/collocation/button/button_skill_close.png",
                           resolution=(1080, 2400), threshold=0.9))
        else:
            break


# 解锁英雄
def click_hero_unlocked():
    if exists(Template("picture/collocation/button/button_unlocked.png", resolution=(1080, 2400), threshold=0.8)):
        touch(Template("picture/collocation/button/button_unlocked.png", resolution=(1080, 2400), threshold=0.8))
        if exists(
                Template("picture/collocation/button/button_unlocked_gem.png", resolution=(1080, 2400), threshold=0.8)):
            touch(
                Template("picture/collocation/button/button_unlocked_gem.png", resolution=(1080, 2400), threshold=0.8))

