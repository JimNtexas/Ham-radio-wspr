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
delayBetweenLoops = args.d
numberOfTransmissions = ("-x " + str(args.x))

while success:
    xmitCount = 0
    while xmitCount < args.x and success:
        result = subprocess.run(['wspr', numberOfTransmissions,'-o','KE5WAN','EM10ck','20','20M'])
        success = (result.returncode == 0)    
        xmitCount += 1
        print (str(xmitCount) + ": result: " + str(result.returncode))
        
    
    if success:
        print("sleeping " + str(delayBetweenLoops) + " minutes")
        time.sleep(delayBetweenLoops*60)
        print("------------------------\n")

localtime = time.asctime( time.localtime(time.time()) )
print ("wspr stopped :", localtime)

