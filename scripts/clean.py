#!/usr/bin/python
# coding: utf8

import subprocess

try:
  subprocess.Popen("keyctl purge user", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
except ValueError:
  print("")
