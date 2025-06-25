# STUDYPUD

#### Video Demo: (https://youtu.be/so0VeJTStH8)

#### Description:

For my final project, I made a Python Pomodoro app. The app idea is mostly inpired by the **"Forest"** app, but a simplified version of it.
I had to learn tkinter to know how to deal with a GUI, because a text based user interface is not really all this lovely.
Learning tkinter was tricky, there was no real course I could find from start to end that explained this process.
However, I managed to search the web for specefic problems that I faced while working, and voilà.
For simplifying UI design, I made this program always minimized. A maximize app will break position and visual harmony of all my program, which is something I tried to avoid.
The app uses the pomodoro technique, which allows users to study for a burst of time, then take a shorter break time, usually around 5 minutes.
Making the clock logic was really new, I made it using extensive if statements and boolians, but it simply broke the live timer I made. So I had to replace them.
I prefered the program to be more flexable, rather than following the classical pomodoro, a user might prefer to study for longer sessions, other user might require longer break time, and a last type that prefers longer study sessions and longer rest sessions.
I made it simple to change UI background as well, that serves an end goal of making the program more flexible and valuable, while retaining its original simplicity.
The user can change the length of his study-break session as long as he wills, if he doesn't provide any value, it will be assumed to the classical 25 minutes study session and 5 minutes break.
After the set time passes, they user will hear a sound notifying him, he can either choose to start the next session break session directly or take a longer break.
The user will also be able to manipulate the default settings as he will, there will be 2 input boxes for that.
In the center of the page, a timer will be shown, the timer has life update with the user input. I made in a clear styling based on minutes and seconds using modolo.
Below the live time section, there will be a small plant that will change how it looks, purely inspired by **Forest** App.
If the user daily total of study minutes basses a certain limit, there will be a reward for him, more than moral sense of achievement.
Although the app can theoritaclly store every day total study minutes, there is no certain tap in which this will be engaging to add, I tried to make a graph, but figured it would take another 50+ hours in it.
For now I will store the total time a user will spend, over time, I will add this functionality.
Everyday, the app will create a total daily study minutes, which will show the user how hard did he work, and how big did the plant become.
There is 3 main buttons below the plants, one to start the timer AND to resume it, the next to pause it, the last to reset it.
At the bottom of the page, there will be an option to change the theme of the total page, the program will also remember the color whenever the user reopens the program.
Given the flexabilty given by tkinter for choosing color, it is plausable to assume that the user will prefer to be able to save his once prefered background color.
the user could have given the option to change EVERYTHING, from the color of the background, to the type of the fonts, even the name of the program! This was not all that useful, because overtime, it will require deep setting.txt file, the file should also be using JSON, which I can't deal with outside web context.
The natural color for the program is a close to a off-white shade, and the sound it will make upon time-completion is the standard windows sound from the winsound library, this is something that is planned to be changed soon, given the user the utility to control the sound to what ever he pleases.
I made this program because I wanted to use it myself, there are plenty of great pomodoro apps on mobile, less great on PC, I though to myself that it would be a perfect oppurtunity to apply my programming language to a goal the will benefit me at last.
This is the most compound program I have built for now, prehaps later on I will add more functionality for it, because doing it was more than fun, it was a challange.
