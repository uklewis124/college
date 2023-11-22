import time
def install_xxx():
    print("Progress: {}%".format(var), end="\r", flush=True)


time.sleep(2)
var = 0
while True:
    var += 1
install_xxx()