
class TestEnd():

    def setup_class(cls):
        from .conftest import DRIVER_DESIRED_CAPS
        from .conftest import REPORT_INSTANCE
        print('End Test')
        print('REPORT_INSTANCE=', REPORT_INSTANCE)
        cls.report = REPORT_INSTANCE

    def test_end(self):
        print('Start to export report')
        #calculate test duration
        #self.report.add_ovinfo("duration", "xxx")
        self.report.export()
