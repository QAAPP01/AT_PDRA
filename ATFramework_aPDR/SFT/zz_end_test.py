
class TestEnd():

    def setup_class(cls):
        from .conftest import DRIVER_DESIRED_CAPS
        
        print('End Test')
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        cls.

    def test_end(self, driver):
        print('Start to export report')
        #calculate test duration
        #self.report.add_ovinfo("duration", "xxx")
        self.report.export()
        driver.driver.quit()
