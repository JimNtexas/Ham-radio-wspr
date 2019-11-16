import subprocess
import time
import argparse

success = True
parser = argparse.ArgumentParser(description='Script to control WsprPI')
parser.add_argument("--x", default=3, help="Number of transmissions per loop")
parser.add_argument("--d", default=2, help="Delay in minutes between calls to wspr")
parser.print_help()
args = parser.parse_args()

print("\nnumber of transmissions per loop: " + str(args.x))
print("delay between loops: " + str(args.d) + " minutes\n")
delayBetweenLoops = args.x
numberOfTransmissions = ("-x " + str(args.d))

while success:
    runCnt = 1 
    result = subprocess.run(['wspr',numberOfTransmissions,'-o','KE5WAN','EM10ck','20','20M'])

    print ("result: " + str(result.returncode))
    success = (result.returncode == 0)
    if success:
        print("sleeping " + str(delayBetweenLoops) + " minutes")
        time.sleep(delayBetweenLoops*60)
        print("------------------------\n")

localtime = time.asctime( time.localtime(time.time()) )
print ("wspr stopped :", localtime)

