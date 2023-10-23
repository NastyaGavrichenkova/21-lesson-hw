import pydantic_settings
from typing import Literal


class AppConfig(pydantic_settings.BaseSettings):
    bstack_userName: str
    bstack_accessKey: str
    remote_url: str

    android_app_url: str
    android_platformVersion: Literal['9.0', '10.0', '11.0'] = '9.0'
    android_deviceName: Literal[
        'Google Pixel 3XL',
        'Samsung Galaxy S20',
        'Oppo A96'
    ] = 'Google Pixel 3XL'

    ios_app_url: str
    ios_platformVersion: Literal['15', '16'] = '15'
    ios_deviceName: [
        'iPhone 13',
        'iPhone 14 Pro Max'
    ] = 'iPhone 13'

    @property
    def bstack_creds(self):
        return {
            'userName': self.bstack_userName,
            'accessKey': self.bstack_accessKey,
        }

    @property
    def android_device_and_platform_version(self):
        return {
            "platformVersion": self.android_platformVersion,
            "deviceName": self.android_deviceName,
        }


    @property
    def ios_device_and_platform_version(self):
        return {
            "platformVersion": self.ios_platformVersion,
            "deviceName": self.ios_deviceName,
        }
