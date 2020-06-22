import os
import re

class GetDeviceMsgs:

    # 获取连接设备的设备ID
    def getDeviceIds(self):
        # 获取连接的设备信息 ['List of devices attached\n', '20080411\tdevice\n', 'GWY0216C15005982\tdevice\n', '\n']
        Ids = list(os.popen("adb devices").readlines())
        # 存储设备ID
        deviceIds = []
        # 使用正则获取连接设备的设备ID 20080411  GWY0216C15005982
        for i in range(1, len(Ids)-1):
            id = re.findall(r"^\w*\b", Ids[i])[0]
            deviceIds.append(id)
        return deviceIds
        print(deviceIds)

    # 获取设备信息，即设备ID，设备版本号，设备的appActivity
    def getDeviceMsgs(self, deviceIds):
        # 存储所有设备的设备信息，即设备ID，设备版本号，设备的appActivity
        deviceMsgs = []
        # 获取连接设备的版本号、appActivity
        for i in range(0, len(deviceIds)):
            id = deviceIds[i]
            # 获取连接设备的安卓系统版本
            versionMsg = list(os.popen('adb -s {} shell getprop ro.build.version.release'.format(id)).readlines())
            version = str(versionMsg).split("'")[1].split("\\")[0]
            print("adb命令获取的设备版本号为：", versionMsg)
            print("处理后获取的设备版本号为：" + version)

           # 获取连接设备测试APP的appActivity 这里是根据应用包名来获取的  APP的包名可以问开发
            activityMsg = list(os.popen('adb -s {} shell dumpsys package 替换为自己测试的APP的应用包名 | findstr 替换成自己的过滤词'.format(id)).readlines())
            activity = str(activityMsg[0]).split("/")[1].split(" ")[0]
            print("adb命令获取的appActivity为：", activityMsg)
            print("处理后获取的appActivity为：" + activity)
            deviceMsgs.append({'deviceId': id, 'deviceVersion': version, 'appActivity': activity})
        return deviceMsgs
