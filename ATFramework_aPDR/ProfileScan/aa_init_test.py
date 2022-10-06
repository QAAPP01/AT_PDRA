from configs import driver_config
import subprocess
import pytest

class TestInit():

    def setup_class(cls):
        from .conftest import DRIVER_DESIRED_CAPS
        from .conftest import REPORT_INSTANCE
        print('Init. Test')
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        cls.report = REPORT_INSTANCE

    def test_report_init(self):
        from configs import driver_config
        from .conftest import DRIVER_DESIRED_CAPS
        print('Start to init. report')
        self.report.add_ovinfo("title", "aPDR_ProfileScan")
        self.report.add_ovinfo("os", "Android")
        self.report.add_ovinfo("device", DRIVER_DESIRED_CAPS['udid'])
        #self.report.add_ovinfo("version", driver_config.android_device_general['platformVersion'])
        self.report.add_ovinfo("version", '9')
        self.report.add_ovinfo("duration", 'auto-fill')

    #@pytest.mark.skip
    def test_build_init(self):
        from .conftest import DRIVER_DESIRED_CAPS
        print('[test_build_init] Start to remove aPDR related project/Movies files')
        list_folder = ['storage/emulated/0/Movies/cyberlink/PowerDirector', 'storage/emulated/0/PowerDirector']
        for folder in list_folder:
            command = f'adb -s {DRIVER_DESIRED_CAPS["udid"]} shell rm -r {folder}'
            print(command)
            subprocess.call(command)
        print('[test_build_init] Done')