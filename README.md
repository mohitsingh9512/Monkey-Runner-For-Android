# Monkey-Runner-For-Android
The monkeyrunner tool provides an API for writing programs that control an Android device or emulator from outside of Android code. With monkeyrunner, you can write a Python program that installs an Android application or test package, runs it, sends keystrokes to it, takes screenshots of its user interface, and stores screenshots on the workstation. The monkeyrunner tool is primarily designed to test applications and devices at the functional/framework level and for running unit test suites, but you are free to use it for other purposes.

The monkeyrunner tool is not related to the UI/Application Exerciser Monkey, also known as the monkey tool. The monkey tool runs in an adb shell directly on the device or emulator and generates pseudo-random streams of user and system events. In comparison, the monkeyrunner tool controls devices and emulators from a workstation by sending specific commands and events from an API. 

# Monkey runner script for testing android app 
# Handles monkey runner going off from the app
# Stores all the output to monkey_testing.txt
