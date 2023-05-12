import pprint

from public_method import *
import os


# 点击coins
def click_coin():
    target_dir = "picture/shop/coins"
    for path in os.listdir(target_dir):
        coin_path = os.path.join(target_dir, path)
        touch(Template(coin_path, record_pos=(-0.006, 1.009), resolution=(1080, 2400)))


def click_mini_pass():
    if exists(Template("picture/shop/mini_pass/mini_pass.png", record_pos=(-0.006, 1.009), resolution=(1080, 2400))):
        touch(Template("picture/shop/mini_pass/mini_pass.png", record_pos=(-0.006, 1.009), resolution=(1080, 2400)))
        touch(Template("picture/shop/mini_pass/mini_pass_open_info.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        touch(Template("picture/shop/mini_pass/mini_pass_open_info_content.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        # chest
        touch(Template("picture/shop/chests/avatar/chest_avatar_Muscateer.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        touch(Template("picture/shop/chests/chest_open.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        touch(Template("picture/shop/chests/unit/chest_skill_Musketeer_Muscateer.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        touch(Template("picture/shop/chests/chest_open.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        touch(Template("picture/shop/chests/emote/chest_emote_YouAreMine.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        touch(Template("picture/shop/chests/chest_open.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))

        # coin
        for i in range(7):
            x = 180
            touch(Template((x, 1300), record_pos=(-0.006, 1.009), resolution=(1080, 2400)))
            sleep(1)
            x += 120
    else:
        pass


# 点击1_time_only_deal
def find_1_time():
    swipe((400, 2000), (400, 500), duration=1)
    if exists(Template("picture/shop/1_time/1_time.png", record_pos=(-0.006, 1.009), resolution=(1080, 2400))) \
            or exists(
        Template("picture/shop/1_time/1_time_2.png", record_pos=(-0.006, 1.009), resolution=(1080, 2400))):
        # 2.99
        touch(Template("picture/shop/1_time/2.99.png", record_pos=(-0.006, 1.009), resolution=(1080, 2400)))
        sleep(1)
        touch(Template("picture/shop/1_time/2.99_open_3_EpicHeroShards.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        sleep(1)
        touch(Template("picture/shop/1_time/2.99_open_3_EpicHeroShards_open_close.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        sleep(1)
        touch(Template("picture/shop/1_time/2.99_open_5_RareHeroShards.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        sleep(1)
        touch(Template("picture/shop/1_time/2.99_open_5_RareHeroShards_open_close.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        sleep(1)
        touch(Template("picture/shop/1_time/2.99_open_10_CommonHeroShards.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        sleep(1)
        touch(
            Template("picture/shop/1_time/2.99_open_10_CommonHeroShards_open_close.png", record_pos=(-0.006, 1.009),
                     resolution=(1080, 2400)))
        sleep(1)
        touch(Template("picture/shop/1_time/close.png", record_pos=(-0.006, 1.009), resolution=(1080, 2400)))
        sleep(1)
        # 9.99
        touch(Template("picture/shop/1_time/9.99.png", record_pos=(-0.006, 1.009), resolution=(1080, 2400)))
        sleep(1)
        touch(Template("picture/shop/1_time/2.99_open_3_EpicHeroShards.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        sleep(1)
        touch(Template("picture/shop/1_time/2.99_open_3_EpicHeroShards_open_close.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        sleep(1)
        touch(Template("picture/shop/1_time/2.99_open_5_RareHeroShards.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        sleep(1)
        touch(Template("picture/shop/1_time/2.99_open_5_RareHeroShards_open_close.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        sleep(1)
        touch(Template("picture/shop/1_time/2.99_open_10_CommonHeroShards.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        sleep(1)
        touch(
            Template("picture/shop/1_time/2.99_open_10_CommonHeroShards_open_close.png", record_pos=(-0.006, 1.009),
                     resolution=(1080, 2400)))
        sleep(1)

        # 19.99
        touch(Template("picture/shop/1_time/19.99.png", record_pos=(-0.006, 1.009), resolution=(1080, 2400)))
        sleep(1)
        touch(Template("picture/shop/1_time/19.99_open_close.png", record_pos=(-0.006, 1.009),
                       resolution=(1080, 2400)))
        sleep(1)

        # 关闭1-time
        touch(Template("picture/shop/1_time/close.png", record_pos=(-0.006, 1.009), resolution=(1080, 2400)))
        sleep(1)

    else:
        pass


def iterating_chest_list():
    img_paths = get_image_paths("picture/shop/chests/")
    find_list = []
    not_find_list = []
    for img_path in img_paths:
        if exists(Template(img_path, resolution=(1080, 2400), threshold=0.9)):
            touch(Template(img_path, resolution=(1080, 2400), threshold=0.9))
            if exists(
                    Template("./picture/shop/chest_button/button_3_close.png", resolution=(1080, 2400), threshold=0.9)):
                touch(
                    Template("./picture/shop/chest_button/button_3_close.png", resolution=(1080, 2400), threshold=0.9))
            find_list.append(img_path)
        else:
            print(img_path)
            not_find_list.append(img_path)
    pprint.pp(find_list)
    pprint.pp(not_find_list)
