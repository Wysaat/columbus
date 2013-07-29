###########################################################################
# this file is of
# user defined methods for dealing with posted data
###########################################################################

def qrcode(data):
    from os import chdir
    from subprocess import call
    chdir("/home/user/qrcode")
    call(["python", "main.py", data[0], data[1]])
    image_path = "/home/user/qrcode/newqrcode.png"
    chdir("/home/user/webpages")
    call(["cp", image_path, "newqrcode.png"])