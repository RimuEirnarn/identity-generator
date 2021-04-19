"""A utility module"""
from os.path import exists as _exists
from os import mkdir as _mkdir
from os import system as _system
from re import sub as _sub
from secrets import SystemRandom as _SystemRandom
from random import Random as _Random
from random import randint as _randbase
from sys import stdin as _stdin
from sys import stdout as _stdout
from time import sleep as _sleep


def sleep(time):
    try:
        _sleep(time)
    except (EOFError, KeyboardInterrupt):
        exit(1)

def system_clear():
    _system("clear || cls")


def safe_input(prompt=None):
    try:
        x = input(prompt)
    except (EOFError, KeyboardInterrupt) as exc:
        print(f"\n{exc.__class__.__name__}")
        raise SystemExit(9) from None
    try:
        return int(x)
    except:
        return None

def create_dir(path):
    if _exists(path):
        return None
    _mkdir(path)


def create_dirs(path):
    """Walked Create Directory
    
    example:
        ./hello/world"""
    paths = path.split("/")
    n = "/"+path[0]
    index = 0
    while True:
        create_dir(n)
        index += 1
        try:
            n += "/"+path[index]
        except IndexError:
            break
    return True


def _mkdirs(root, iteratable):
    """Generate files.
    
    iteratable can only be a string/list/tuple/dict
    
    string -> Create a directory
    list -> nothing.
    tuple -> create files.
    dict -> see util.create_roots."""
    for n in iteratable:
        if isinstance(n, str):
            create_dir(root+n)
        elif isinstance(n, list):
            pass
        elif isinstance(n, tuple):
            touchs(root, n)
        elif isinstance(n, dict):
            create_dir(root+n)
            create_roots(root+n+"/", n)
        else:
            raise Exception("Error.")
        


def touch(file):
    if not _exists(file):
        _system(f"touch {repr(file)}")


def touchs(root, iteratable):
    """Generate files.
    
    iteratable can only be a string/list/tuple/dict
    
    string -> Create a file
    list -> create directories.
    tuple -> nothing.
    dict -> see util.create_roots."""
    for n in iteratable:
        if isinstance(n, str):
            touch(root+n)
        elif isinstance(n, list):
            _mkdirs(root, n)
        elif isinstance(n, tuple):
            pass
        elif isinstance(n, dict):
            pass
        else:
            raise Exception("Error.")


def create_roots(start: str, root: dict):
    """Create oriented program path.
    
    start -> root path of the program.
    eg: /home/Nobody/myprogram
    
    root -> A dictionary of the program.
    the key will be used as Directory names. and leftover will be a file. if the leftover value was not a dictionary.
        It will raise an error, whether the leftover was not dictionary or string or list.
        
    root:
        dictionary -> Name of the directory and the contents
        list -> name of the directories to be created
        string -> name of the file to be created
        tuple -> name of the files to be created
        None -> create nothing."""
    if not isinstance(root, dict):
        raise TypeError("root was not a dict object.")
    root_dir = start
    if len(root) == 0:
        create_dir(root_dir)
    for n in root:
        create_dir(root_dir+n)
        if isinstance(root[n], dict):
            create_roots(root_dir+n+"/", root[n])
        elif isinstance(root[n], str):
            touch(root_dir+'/'+n)
        elif isinstance(root[n], list):
            _mkdirs(root_dir+n+"/", root[n])
        elif isinstance(root[n], tuple):
            touchs(root_dir+n+"/", root[n])
        elif root[n] is None:
            pass
        else:
            raise Exception(f"{repr(n)} was not a string/dictionary")
    
    return None


def randint(x, y, onion=3):
    """a Random Integer Generator.
    
    This Function. creates an random integer and use it as seed. the process will still continue, until "onion" (another name of Layer) reached 0 or lesser."""
    base = _randbase(x, y)
    base_ = None
    default_onion = onion
    while onion > 0:
        n = _randbase(0, 10)
        if not base_:
            if n <= 5:
                base_ = _Random(base).randint(x, y)
            if n > 5 and n <= 10:
                base_ = _SystemRandom(base).randint(x, y)
        else:
            if n <= 5:
                base_ = _Random(base_).randint(x, y)
            if n > 5 and n <= 10:
                base_ = _SystemRandom(base_).randint(x, y)
        onion -= 1
    if default_onion <= 0:
        base_ = randint(x, y, 3)  # Default
    return base_

def fill(instance, index, content):
    """Filler to list/array.

    :type instance: list
    :type index: int
    :type content: Any
    :param instance: 'list' instance
    :param index: Index to be filled
    :param content: Content of a Index
    :return: None"""
    if isinstance(instance, list):
        instance_len = len(instance)
        if instance_len == index or instance_len > index:
            instance[index] = content
        if instance_len == index-1:
            instance.append(content)
        if instance_len < index:
            _n = index - instance_len
            for _n_ in range(_n+1):
                instance.append(None)
            instance[index] = content
        return None
    if isinstance(instance, dict):
        instance[index] = content
        return None
    else:
        raise TypeError("Instance need to be list")


def expect(instance, value, only_key=False):
    if isinstance(instance, list):
        if value in instance:
            return True
    if isinstance(instance, dict):
        _b = {}
        # Key is a repr and an Assignment. (instance['KEY'] = 'CONTENT'), but it will return
        # returns[KEY] = True
        # depending on keyword 'only_key'
        if only_key is False:
            for _a in instance:
                if value == instance[_a]:
                    _b[f"instance[{_a}]){value})"] = True
        else:
            for _a in instance:
                if value == _a:
                    _b[_a] = True
        return _b


def guess_os():
    """Guessing Operating That User used"""
    MSDOS = "C:\\"
    UNIX = "/usr/bin/python3"
    ANDROID = "/system/xbin"
    # Well i used some random path do define what OS They are
    # Support: Linux, MacOS. Android, Windows
    # There quite little chance that /data/media/0 is also on Other Linux
    # Beside Android
    # And these are random things and a common sense for OS-es
    if _exists(MSDOS):
        return "Windows (MSDOS)"
    if _exists(UNIX):
        if _exists("/etc/os-release"):
            return open("/etc/os-release").readlines()[1].split("=")[1][1:-2]
        return "Linux/MacOS (UNIX)"
        #TRY HARDER!
    if _exists(UNIX) and _exists(ANDROID):
        EXISTANCES = []
        ANDROID_PATH = ["/system/bin/sdcard", "/storage/self", "/data/user/0", "/data/misc/wifi", "/init"]
        for _ANDROID in ANDROID_PATH:
            if _exists(_ANDROID):
                EXISTANCES.append(True)
            else:
                EXISTANCES.append(False)
        del _ANDROID
        _b = 0
        for _a in EXISTANCES:
            _b += _a  # Since Boolean (True) is 1. so whatever
        if _exists("/etc/os-release"):
            return open("/etc/os-release").readlines()[1].split("=")[1][1:-2]
        if _b == len(ANDROID_PATH):
            return "Android (Linux)"
        return "Android/Linux/MacOS (UNIX)"

    if _exists(ANDROID):
        return "Android (Linux)"


def toint(anything):
    ints = list("1234567890")
    x = []
    anything = str(anything)
    for n in anything:
        if n in ints:
            x.append(n)
    
    return int("".join(a for a in x))

def tofloat(anything):
    xfloat = list("1234567890.")
    x = []
    anything = str(anything)
    periodexist = False
    for n in anything:
        if n in xfloat:
            if n == "." and periodexist is True:
                pass
            elif n == "." and periodexist is False:
                x.append(n)
                periodexist = True
            else:
                x.append(n)
    
    return float("".join(a for a in x))

def noint(anything):
    return _sub("[1234567890]", "", anything)
