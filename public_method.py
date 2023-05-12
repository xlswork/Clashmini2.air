import datetime

from airtest.core.api import *
import os


# 获取图片路径
def get_path(target_dir):
    # 遍历目标目录下的所有文件和文件夹
    for item in os.listdir(target_dir):
        # 拼接完整路径
        item_path = os.path.join(target_dir, item)

        # 判断是否是文件夹
        if os.path.isdir(item_path):
            print('Folder:', item_path)
        else:
            print('File:', item_path)


# 获取指定目录下的图片文件
def get_image_paths(folder_path):
    image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
    image_paths = []

    for file in os.listdir(folder_path):
        filename, extension = os.path.splitext(file)
        if extension.lower() in image_extensions:
            image_paths.append(os.path.join(folder_path, file))

    return image_paths


# 在指定目录下创建以当前时间为名的文件夹
def create_timestamp_folder(parent_folder):
    # 获取当前时间并格式化为字符串
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # 在指定目录下创建以当前时间命名的文件夹
    new_folder_path = os.path.join(parent_folder, timestamp)
    os.makedirs(new_folder_path)

    return new_folder_path


"""
跳转界面
"""


# 前往商店
def jump_shop():
    wait(Template("./picture/navigation_bar/battle_up.png", resolution=(1080, 2400)))
    if exists(Template("./picture/navigation_bar/shop_down_free.png", resolution=(1080, 2400))):
        touch(Template("./picture/navigation_bar/shop_down_free.png", resolution=(1080, 2400)))
    elif exists(
            Template("./picture/navigation_bar/shop_down.png", resolution=(1080, 2400))):
        touch(Template("./picture/navigation_bar/shop_down.png", resolution=(1080, 2400)))
    else:
        print("商店跳转失败")
        return None
    if check_shop():
        print("商店跳转成功")
    else:
        print("商店跳转失败")
        return None


# 确认是否在商店
def check_shop():
    if exists(
            Template("./picture/navigation_bar/shop_up_free.png", record_pos=(-0.006, 1.009), resolution=(1080, 2400))):
        return True
    elif exists(
            Template("./picture/navigation_bar/shop_down.png", record_pos=(-0.006, 1.009), resolution=(1080, 2400))):
        return True
    else:
        return False


# 前往收集界面
def jump_collocation():
    wait(Template("./picture/navigation_bar/battle_up.png", resolution=(1080, 2400)))
    if exists(Template("./picture/navigation_bar/collocation_down.png", resolution=(1080, 2400))):
        touch(Template("./picture/navigation_bar/collocation_down.png", resolution=(1080, 2400)))
    elif exists(Template("./picture/navigation_bar/collocation_down_redbot.png", resolution=(1080, 2400))):
        touch(Template("./picture/navigation_bar/collocation_down_redbot.png", resolution=(1080, 2400)))
    else:
        print("收集界面跳转失败")
        return None
    if check_collocation():
        print("收集界面跳转成功")
    else:
        print("收集界面跳转失败")


# 确认是否在商店
def check_collocation():
    if exists(
            Template("./picture/navigation_bar/collocation_up.png", resolution=(1080, 2400))):
        return True
    elif exists(
            Template("./picture/navigation_bar/collocation_down_redbot.png", resolution=(1080, 2400))):
        return True
    else:
        return False
