import subprocess
import time

success = True
while success:
    result = subprocess.run(['wspr','-x 1','-o','KE5WAN','EM10ck','20','20M'])

    print ("result: " + str(result.returncode))
    success = (result.returncode == 0)
    if success:
        print("sleeping 4 minutes")
        time.sleep(4*60)

print ("wspr stopped")

