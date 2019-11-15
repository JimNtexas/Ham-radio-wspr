import subprocess
import time

success = True
while success:
    result = subprocess.run(['wspr','-x 1','-o','KE5WAN','EM10ck','20','20M'])

    print ("result: " + str(result.returncode))
    success = (result.returncode == 0)
    if success:
        print("sleeping 2 minutes")
        time.sleep(2*60)
        print("------------------------\n")

localtime = time.asctime( time.localtime(time.time()) )
print ("wspr stopped :", localtime)

