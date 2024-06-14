import inspect
import logging
import logging.handlers
import os
import platform
from functools import wraps

try:
    os.system('color')
except:
    pass

log_path = ""
dname = os.path.dirname
pattern = dname(dname(dname(__file__)))  # [log] -> [ATFramework] -> [Target Folder]

if platform.system() == "Windows":
    import ctypes


    class DbgViewHandler(logging.Handler):
        def emit(self, record):
            ctypes.windll.kernel32.OutputDebugStringW(self.format(record))

for frame in inspect.stack():
    if pattern in frame.filename:
        log_path = dname(frame.filename) + "/log"

os.makedirs(log_path, exist_ok=True)


def set_udid(udid):
    global log_path
    log_path = f"{log_path}/{udid}"


def logger(*msg, function=None, file_name=f'{log_path}/module.log', write_to_file=True, line=True,
           log_level: str = None):
    if not function:
        function = inspect.stack()[1].function
        line = inspect.stack()[1].frame.f_lineno
        name = os.path.basename(inspect.stack()[1].filename)
    else:
        line = inspect.stack()[2].frame.f_lineno
        name = os.path.basename(inspect.stack()[2].filename)

    def get_color(string):
        reset = '\033[0m'
        colors = {
            'debug': '\033[37m',  # level = 10, gray
            'info': '\033[97m',  # level = 20, white
            'warn': '\033[33m',  # level = 30, yellow
            'error': '\033[31;m',  # level = 40, red
            'crit': '\033[30;41;1;1m',  # level = 50, black with red background

            'time': '\033[92m',
            'name': '\033[97;4;1m',
            'function': '\033[96m',
            'line': '\033[93;1m'
        }
        return reset + colors[string]

    def get_log_level():
        info_strings = '[Info]', '[info]'
        warning_strings = '[Warning]', '[warning]', '[Warn]', '[warn]'
        error_strings = '[Error]', '[error]', '[AssertError]', '[AssertionError]', '[UnitTestError]'
        critical_strings = '[Critical]', '[critical]', '[Crit]', '[crit]', '[Exception]', '[exception]'

        if log_level:
            match log_level.lower():
                case 'info':
                    return logging.INFO, get_color('info')
                case 'warn':
                    return logging.WARN, get_color('warn')
                case 'err':
                    return logging.ERROR, get_color('error')
                case 'crit':
                    return logging.CRITICAL, get_color('crit')

        for level_strings, levels, colors in [
                (info_strings, logging.INFO, 'info'),
                (warning_strings, logging.WARN, 'warn'),
                (error_strings, logging.ERROR, 'error'),
                (critical_strings, logging.CRITICAL, 'crit')]:
            try:
                iter(msg)
                if any(x for x in level_strings if x in msg[0]):
                    return levels, get_color(colors)
            except TypeError:
                if any(x for x in level_strings if x in msg):
                    return levels, get_color(colors)

        return logging.NOTSET, get_color('info')

    level, color = get_log_level()

    formatter = logging.Formatter(fmt=f"%(asctime)s <{name}> [{function}](line {line}) - %(message)s",
                                  datefmt="%m/%d/%Y %I:%M:%S %p")

    _logger = logging.getLogger("ATFramework")
    if _logger.handlers:
        for hdlr in _logger.handlers[:]:
            _logger.removeHandler(hdlr)

    _console = logging.StreamHandler()
    _console.setLevel(level)
    _console.setFormatter(logging.Formatter(fmt=f"{get_color('time')}%(asctime)s "
                                                f"{get_color('name')}<{name}> "
                                                f"{get_color('function')}[{function}] "
                                                f"{get_color('line')}(line {line}) "
                                                f"{color} %(message)s",
                                            datefmt="%m/%d/%Y %I:%M:%S %p"))

    ft_rotating = logging.handlers.TimedRotatingFileHandler(file_name, when="D", interval=1, backupCount=0, delay=True)
    ft_rotating.setLevel(level)  # file_time_rotating
    ft_rotating.setFormatter(formatter)

    _logger.setLevel(level)
    _logger.addHandler(_console)
    _logger.addHandler(ft_rotating)

    if platform.system() == "Windows":
        dbw = DbgViewHandler()
        dbw.setLevel(level)
        dbw.setFormatter(formatter)
        _logger.addHandler(dbw)

    myMsg = [str(x) for x in msg]
    _logger.log(level, str(*myMsg))
    ft_rotating.close()


def qa_log(file_name=None, write_to_file=True):
    'decorator'
    if not file_name:
        file_name = os.path.dirname(__file__) + "/log/Product.log"
        os.makedirs(log_path, exist_ok=True)

    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            log_pattern = "Start function " + \
                          ("args: %s" % str(args) if args else "") + \
                          (" kwargs: %s" % str(kwargs) if kwargs else "")
            logger(log_pattern, function=func.__name__, file_name=file_name)
            ret = func(*args, **kwargs)
            logger("End function ", function=func.__name__, file_name=file_name)
            return ret

        return inner

    return outer


if __name__ == "__main__":
    '''decorator sameple'''


    @qa_log()
    def test(index, text="TEXT"):
        print("index={} text={}".format(index, text))


    test(33, text="sample")

    '''normal logger sample'''