#!/usr/bin/python
# coding: utf8

import subprocess
import sys
import getpass

key_name = "my_key_1"
try:
  key_id = int(subprocess.Popen("keyctl request user {} @s".format(key_name),
    shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read())
  print subprocess.Popen("keyctl print {}".format(str(key_id)),
    shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().rstrip()
except ValueError:
  sys.stderr.write("Password for '{}' : ".format(key_name))
  password = getpass.getpass("").rstrip()
  subprocess.Popen("keyctl add user {} '{}' @s".format(key_name, password),
    shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  print password
