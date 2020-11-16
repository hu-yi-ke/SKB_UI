import yaml
from Config.dir_setting import Config
from appium import webdriver


def init(point =4723,**kwargs):
    with open(Config.yaml_path + "/appium_desired.yaml",encoding="utf-8") as fs:
        desired_caps = yaml.load(fs,Loader=yaml.FullLoader)
        print(desired_caps)
    for key,values in kwargs.items():
        desired_caps[key] = values
    print(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(point),desired_caps)
    return driver

if __name__ == '__main__':
    a = init()
    print(a)