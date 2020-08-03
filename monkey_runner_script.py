# To use monkey runner use monkeyrunner tool and supply your monkey runner script path 
# Driver code from shell/terminal : /opt/android-sdk/tools/bin/./monkeyrunner /opt/jenkins/workspace/qa_testing/scripts/monkey_runner_script.py

# Please change path according to OS
# Start of python script for monkey runner
# App name =  example.apk
# Package name = com.exmaple.m

# monkey_testing.txt contains final report
# monkeyreport.txt is an intermediate report of every execution 

device = MonkeyRunner.waitForConnection()

# delay for emulator start up
time.sleep(10)

subprocess.call("/opt/android-sdk/platform-tools/./adb uninstall com.example.m",shell=True)

apk_path = device.shell('pm path com.example.m')
if apk_path.startswith('package:'):
        print "example already installed."
else:
        print "example not installed, installing Apk..."
        subprocess.call("/opt/android-sdk/platform-tools/./adb install /opt/jenkins/workspace/qa_testing/artifacts/example.apk",shell=True)
        time.sleep(20)
        print "Installed APK"
        subprocess.call("/opt/android-sdk/platform-tools/./adb shell am start -n com.example.m/com.example.m.SplashScreenActivity",shell=True)
        #Login Based Tasks
        print "Login Done"

#try:
#       os.remove("/opt/jenkins/workspace/qa_testing/artifacts/monkeyreport.txt")
#       os.remove("/opt/jenkins/workspace/qa_testing/artifacts/monkey_testing.txt")
#except OSError, e:  ## if failed, report it back to the user ##
#       print ("Error:")

f= open("/opt/jenkins/workspace/qa_testing/artifacts/monkey_testing.txt","w+")
f.write("Mokey Testing")
f.close()

def func():
        print "launching example app ..."
        device.startActivity(component='com.example.m/com.example.m.MainActivity')

        time.sleep(5)

        #pinning the app since monkey goes outside app or turns off the wifi
        #for 720 x 1280
        device.shell("input keyevent KEYCODE_APP_SWITCH")
        device.shell("input tap 600 950")
        device.shell("input tap 532 1072")

        time.sleep(5)

        print "launching events to app ..."
        # Sends 100 events to app 
        subprocess.call("/opt/android-sdk/platform-tools/./adb shell monkey --kill-process-after-error --throttle 300 --pct-syskeys 0 --pct-appswitch 0 -s 3527834 -p com.example.m -v 100 > /opt/jenkins/workspace/qa_testing/artifacts/monkeyraw.txt",shell=True)
        r= open("/opt/jenkins/workspace/qa_testing/artifacts/monkeyraw.txt","r")
        contents = ""
        if r.mode == "r":
                contents = r.read()
        f= open("/opt/jenkins/workspace/qa_testing/artifacts/monkey_testing.txt","a+")
        f.write(contents)
        f.close()

        #Unpin app
        device.shell("am task lock stop")
        return;

for x in range(5):
	func()
print "end of script"

