import os
from main import package_version, package_build_number



class TestInit:

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

        device_brand = os.popen(f"adb -s {DRIVER_DESIRED_CAPS['udid']} shell getprop ro.product.brand").read().strip()
        device_model = os.popen(f"adb -s {DRIVER_DESIRED_CAPS['udid']} shell getprop ro.product.model").read().strip()

        self.report.add_ovinfo("device", f"{device_brand} {device_model}")
        self.report.add_ovinfo("version", f'{package_version}.{package_build_number}_P')
        self.report.add_ovinfo("duration", 'auto-fill')