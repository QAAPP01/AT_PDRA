import subprocess
import pytest

from ATFramework_aPDR.ATFramework.drivers.driver_factory import DriverFactory
from ATFramework_aPDR.configs import app_config, driver_config
from ATFramework_aPDR.pages.page_factory import PageFactory
from main import package_version, package_build_number


class TestInit():

    def setup_class(cls):
        from .conftest import DRIVER_DESIRED_CAPS
        from .conftest import REPORT_INSTANCE
        print('Init. Test')
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        cls.report = REPORT_INSTANCE

    def test_report_init(self):
        from .conftest import DRIVER_DESIRED_CAPS
        print('Start to init. report')
        self.report.add_ovinfo("title", "aPDR_SFT")
        self.report.add_ovinfo("os", "Android")
        self.report.add_ovinfo("device", DRIVER_DESIRED_CAPS['udid'])
        self.report.add_ovinfo("version", f'{package_version}.{package_build_number}_P')
        self.report.add_ovinfo("duration", 'auto-fill')

    def test_app_init(self):
        desired_caps = app_config.init_cap
        driver = DriverFactory().get_mobile_driver_object("appium u2", driver_config, app_config, 'local', desired_caps)
        page_main = PageFactory().get_page_object("main_page", driver)
        page_main.enter_launcher()
        page_main.enable_file_name()

    # @pytest.mark.skip
    # def test_build_init(self):
    #     from .conftest import DRIVER_DESIRED_CAPS
    #     print('[test_build_init] Start to remove aPDR related project/Movies files')
    #     list_folder = ['storage/emulated/0/Movies/cyberlink/PowerDirector', 'storage/emulated/0/PowerDirector']
    #     for folder in list_folder:
    #         command = f'adb -s {DRIVER_DESIRED_CAPS["udid"]} shell rm -r {folder}'
    #         print(command)
    #         subprocess.call(command)
    #     print('[test_build_init] Done')
