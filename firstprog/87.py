# Shutil module
import shutil
import pywin
import os
a=shutil.__all__
print(a)
# shutil.copy()
# shutil.copytree()
# shutil.move()
# shutil.rmtree()
# shutil.copy("C:\Users\dsumi\Downloads\Cybersecurity Principles.pdf""Cybersecurity.py")
if pywin.is_platform_unicode:
    shutil.copytree("C:\Users\dsumi\PycharmProjects","Projects")
    print("None")