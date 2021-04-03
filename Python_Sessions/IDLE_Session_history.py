Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = "Lunus Torvalds"
>>> 
>>> 
>>> id(name)
140449864501424
>>> name = "Narayanan"
>>> id(name)
140449862336944
>>> 
>>> 
>>> 
>>> name = 1
>>> id(name)
4513512624
>>> 
>>> name_2 = 1
>>> id(name_2)
4513512624
>>> 
>>> name_2 = 2
>>> 
>>> 
>>> id(name_2)
4513512656
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> name = name_2
>>> id(name), id(name_2)
(4513512656, 4513512656)
>>> 
>>> name = "narayanan"
>>> dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> 
>>> 
>>> import os
>>> dir(os)
['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'DirEntry', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 'F_LOCK', 'F_OK', 'F_TEST', 'F_TLOCK', 'F_ULOCK', 'MutableMapping', 'NGROUPS_MAX', 'O_ACCMODE', 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_EXLOCK', 'O_NDELAY', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O_RDONLY', 'O_RDWR', 'O_SHLOCK', 'O_SYNC', 'O_TRUNC', 'O_WRONLY', 'PRIO_PGRP', 'PRIO_PROCESS', 'PRIO_USER', 'P_ALL', 'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_WAIT', 'PathLike', 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD', 'RTLD_NOW', 'R_OK', 'SCHED_FIFO', 'SCHED_OTHER', 'SCHED_RR', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'ST_NOSUID', 'ST_RDONLY', 'TMP_MAX', 'WCONTINUED', 'WCOREDUMP', 'WEXITED', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv', '_spawnvef', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chflags', 'chmod', 'chown', 'chroot', 'close', 'closerange', 'confstr', 'confstr_names', 'cpu_count', 'ctermid', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'environb', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 'fchmod', 'fchown', 'fdopen', 'fork', 'forkpty', 'fpathconf', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'get_blocking', 'get_exec_path', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 'getgrouplist', 'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid', 'getppid', 'getpriority', 'getsid', 'getuid', 'initgroups', 'isatty', 'kill', 'killpg', 'lchflags', 'lchmod', 'lchown', 'linesep', 'link', 'listdir', 'lockf', 'lseek', 'lstat', 'major', 'makedev', 'makedirs', 'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty', 'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'popen', 'pread', 'putenv', 'pwrite', 'read', 'readlink', 'readv', 'register_at_fork', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sched_get_priority_max', 'sched_get_priority_min', 'sched_yield', 'sendfile', 'sep', 'set_blocking', 'set_inheritable', 'setegid', 'seteuid', 'setgid', 'setgroups', 'setpgid', 'setpgrp', 'setpriority', 'setregid', 'setreuid', 'setsid', 'setuid', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe', 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'st', 'stat', 'stat_result', 'statvfs', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names', 'system', 'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 'truncate', 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitpid', 'walk', 'write', 'writev']
>>> 
>>> 
>>> help(os.mkdir)
Help on built-in function mkdir in module posix:

mkdir(path, mode=511, *, dir_fd=None)
    Create a directory.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    
    The mode argument is ignored on Windows.

>>> os.getlogin()
'root'
>>> os.uname()
posix.uname_result(sysname='Darwin', nodename='Mac-mini-2.local', release='20.3.0', version='Darwin Kernel Version 20.3.0: Thu Jan 21 00:06:51 PST 2021; root:xnu-7195.81.3~1/RELEASE_ARM64_T8101', machine='x86_64')
>>> clear()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    clear()
NameError: name 'clear' is not defined
>>> 
>>> 


>>> 

>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> 
>>> 
>>> 
>>> list1 = range(10)
>>> list1
range(0, 10)
>>> 
>>> 
>>> list1 = list(range(10))
>>> list1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list1 = list(range(100))
>>> list1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
>>> 

>>> 
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __reduce__(...)
 |      Helper for pickle.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

>>> 
>>> list(range(5,5,100))
[]
>>> 
>>> 
>>> range(5,101,5)
range(5, 101, 5)
>>> 
>>> list(range(5,101,5))
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
>>> 
>>> 
>>> list(range(101))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> 
>>> 
>>> 
>>> list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> 
>>> list(range(11))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> test_list = list(range(11))
>>> test_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> 
>>> test_list[5]
5
>>> 
>>> 
>>> test_list = list(range(10,21))
>>> 
>>> test_list[5]
15
>>> test_list
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> 
>>> test_list[5,19]
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    test_list[5,19]
TypeError: list indices must be integers or slices, not tuple
>>> 
>>> test_list[5:4]
[]
>>> test_list[5:9]
[15, 16, 17, 18]
>>> 
>>> 
>>> test_list[-1]
20
>>> test_list[-2]
19
>>> len(test_list)
11
>>> test_list.size()
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    test_list.size()
AttributeError: 'list' object has no attribute 'size'
>>> 
>>> dir(test_list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> 
>>> 
>>> pop(test_list)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    pop(test_list)
NameError: name 'pop' is not defined
>>> test_list.pop()
20
>>> test_list
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
>>> test_list[4] = 100
>>> 
>>> test_list
[10, 11, 12, 13, 100, 15, 16, 17, 18, 19]
>>> 
>>> 
>>> name = "narayanan"
>>> 
>>> 
>>> del test_list[5:]
>>> test_list
[10, 11, 12, 13, 100]
>>> 
>>> 
>>> del name[4:]
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    del name[4:]
TypeError: 'str' object does not support item deletion
>>> 
>>> 
>>> del name
>>> name = "separate_str"
>>> 
>>> name
'separate_str'
>>> name = name.replace('_str','')
>>> 
>>> name
'separate'
>>> 
>>> 
>>> name = "separate_str"
>>> id(name)
140449055928752
>>> name = name.replace('_str','')
>>> id(name)
140449055929968
>>> 
>>> 
>>> id(test_list)
140449055908104
>>> tes_list.append(101)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    tes_list.append(101)
NameError: name 'tes_list' is not defined
>>> 
>>> 
>>> test_list.append(101)
>>> 
>>> 
>>> id(test_list)
140449055908104
>>> 
>>> 
>>> 
>>> 
>>> tes_list
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    tes_list
NameError: name 'tes_list' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 


>>> 

>>> 
>>> test_list
[10, 11, 12, 13, 100, 101]
>>> 
>>> test_list_1 = test_list
>>> 
>>> id(test_list_1, test_list)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    id(test_list_1, test_list)
TypeError: id() takes exactly one argument (2 given)
>>> 
>>> 
>>> 
>>> id(test_list_1), id(test_list)
(140449055908104, 140449055908104)
>>> 
>>> 
>>> test_list_1.append(102)
>>> 
>>> test_list_1
[10, 11, 12, 13, 100, 101, 102]
>>> test_list
[10, 11, 12, 13, 100, 101, 102]
>>> 
>>> 
>>> third_list = test_list_1
>>> 
>>> third_list.append(110)
>>> 
>>> 
>>> third_list, test_list_1, test_list
([10, 11, 12, 13, 100, 101, 102, 110], [10, 11, 12, 13, 100, 101, 102, 110], [10, 11, 12, 13, 100, 101, 102, 110])
>>> 
>>> 
>>> a = 1
>>> b = a
>>> b = 2
>>> a, b
(1, 2)
>>> 
>>> 
>>> 
>>> a = 1
>>> b = a
>>> id(a), id(b)
(4513512624, 4513512624)
>>> b = 10
>>> id(a), id(b)
(4513512624, 4513512912)
>>> 
>>> 
>>> name_1 = "narayanan"
>>> name_2 = "narayanan"
>>> 
>>> id(name_1), id(name_2)
(140449055929904, 140449055929904)
>>> 
>>> 
>>> name_1 = "narayanan"
>>> name_2 = name_1
>>> name_2 = "testing_string_immutability"
>>> id(name_1), id(name_2)
(140449055929904, 140449056033648)
>>> 
>>> 
>>> list_1 = [1, 2, 3]
>>> list_2 = list_1
>>> id(list_1), id(list_2)
(140449055930248, 140449055930248)
>>> list_2 = [3, 5]
>>> 
>>> id(list_1), id(list_2)
(140449055930248, 140449055908168)
>>> 
>>> 
>>> 
>>> list_1 = [1, 2, 3]
>>> list_2 = list_1
>>> id(list_1), id(list_2)
(140449055908296, 140449055908296)
>>> 
>>> 
>>> list_2.append(4)
>>> 
>>> list_1
[1, 2, 3, 4]
>>> list_2
[1, 2, 3, 4]
>>> id(list_1), id(list_2)
(140449055908296, 140449055908296)
>>> 
>>> list_1[0] = 100
>>> 
>>> list_1, list_2
([100, 2, 3, 4], [100, 2, 3, 4])
>>> 
>>> 
>>> list_2
[100, 2, 3, 4]
>>> 
>>> list_1 = []
>>> list_2
[100, 2, 3, 4]
>>> [100, 2, 3, 4]
[100, 2, 3, 4]
>>> 
>>> 
>>> 


>>> 


>>> 
>>> 

>>> import copy
>>> dir(copy)
['Error', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_copy_dispatch', '_copy_immutable', '_deepcopy_atomic', '_deepcopy_dict', '_deepcopy_dispatch', '_deepcopy_list', '_deepcopy_method', '_deepcopy_tuple', '_keep_alive', '_reconstruct', 'copy', 'deepcopy', 'dispatch_table', 'error']
>>> 
>>> 
>>> 
>>> list_1 = [1, 2, 3]
>>> list_2 = copy.deepcopy(list_1)
>>> list_2.append(4)
>>> 
>>> list_1, list_2
([1, 2, 3], [1, 2, 3, 4])
>>> 
