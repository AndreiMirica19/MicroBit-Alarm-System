# MicroBit-Alarm-System
The alarm system has the following compotament:

it can be configured by commands introduced from the serial interface (the terminal);
it can be armed by pressing a sequence of buttons;
it can be disarmed by pressing a sequence of buttons;
it can be configured for automatic disarming, after a certain time interval;
it will store a sound if the system will be moved for 2 seconds;
it will store logs regarding arming and disarming;

The system will be configured using the terminal. To initiate the connection to the terminal, simply press any key (hint: uart), after which the system will display a prompt in the form "alarm cmd>" that allows you to enter system configuration commands. When the system receives commands in the terminal, it will not be in working order (it will do nothing but execute commands).

The connection to the terminal is closed using the exit command.

The system can save 3 different user profiles. The following information will be saved for each user:

name - username;
pin - a 4-digit code used to arm / disarm the alarm.
The following commands will be used to configure user profiles:

profile add name pin - add a new profile; if the profile has been added successfully, the message Profile added will be displayed; if a profile with the same name already exists, the pin will change; if an attempt is made to add a 4th profile, the message: Could not save profile will be displayed. Limit exceeded .; if the pin does not have 4 digits, the message Could not save profile will be displayed. Invalid pin.

profile delete name - deletes the profile identified by name; if the deletion was successful the text will be displayed:


Profile deleted; if the deletion could not be performed because the profile does not exist, the message: Could not delete profile will be displayed. Profile name does not exist.


Ariming time

The system allows the configuration of the arming time. It is measured in minutes and represents the length of time a system remains armed. For example, if the arming time is set to 30, 30 minutes after arming, the alarm will automatically disarm.

If not changed, the default arming time is 1.

The arm time val command is used to set the arming time.


To arm the alarm system, press buttons A and B at the same time, at which point the LED array will enter the pin input mode.

If the pin is inserted correctly, the arming will be signaled by displaying a smiling face, and if the pin is not correct, a sad face will be displayed.

After signaling the armature, until disarming, the system will have the entire array of LEDs on

Pin input

When the system enters pin input mode, it will start by displaying the value 0 using the LED array and will allow the values to be incremented using the A and B buttons. Pressing the A key can increase the values and pressing the B key can increase the values. decrease values. If the increment reaches the maximum value (9), it will continue with 0,1,2, etc. The behavior is similar if the decrement reaches 0.

To select a value, tap the Micro: bit logo.


Disarmament

When in armed mode, the system can be disarmed by pressing buttons A and B at the same time, after which the system will enter pin input mode. If the pin is inserted correctly, disarming will be signaled by displaying a smiling face for 3 seconds. If the pin is not correct, a sad face will be displayed for 3 seconds and the alarm will continue to be armed.


Automatic disarmament

If the arming time has elapsed, the system will automatically disarm. It will display a smiling face for 3 seconds to signal this, after which the LED array will go out completely.

Alarm activation

If the system is armed, the alarm will be activated by shaking the device for 2 seconds. If this happens, the LED array will flash and make a sound. It will not stop until the system is manually disarmed.

Information storage

The alarm will contain a file with one entry for each of the following events:

arming
manual disarmament
automatic disarmament
alarm activation
When one of these events occurs, a <time> <event> line will be added, where time is the hour and minute the event occurred and event is one of the texts described below.
  
Information messages

To store events on your device, the following messages will be stored:

User armed the system. - for arming the system, where the user is the user who armed the system;
User disarmed the system. - for manual disarming of the system, where the user is the user who disarmed the system;
Automatic disarmed system. - for automatic disarming of the system;
Alarm activated. - to start the alarm.
  
  
Alarm information display

To read and delete information from the alarm system, use the following commands in the system terminal:

log print - displays all information;
log delete - deletes all information and displays the message Logs deleted.
  
