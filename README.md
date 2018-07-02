# lshuge

Find out what's huge, and you get to define what's huge.

Below is just a demo, this isn't finished yet, and I fear it'll never be.

```shell
$ mkfile 1k s
$ mkfile 5k xs
$ mkfile 1m xxl
$ ls -alh
-rw-------  1 timfeirg  staff   1.0K Jul  3 01:33 s
-rw-------  1 timfeirg  staff    20K Jul  3 01:32 xs
-rw-------  1 timfeirg  staff   1.0M Jul  3 01:32 xxl
$ lshuge.py . --percentage 0.8
xxl    1.0M
$ mkfile 1m xxl2
$ lshuge.py . --percentage 0.3
xxl    1.0M
xxl2   1.0M
```
