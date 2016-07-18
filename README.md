Project by HITVARDHAN SINGH SOLANKI

A stopwatch Game.

Mini-project description - "Stopwatch: The Game"

Our mini-project for this week will focus on combining text drawing in the canvas with timers to build a simple digital stopwatch that keeps track of the time in tenths of a second. The stopwatch should contain "Start", "Stop" and "Reset" buttons. To help guide you through this project, we suggest that you download the provided program template for this mini-project and build your stopwatch program as follows:

Mini-project development process

Construct a timer with an associated interval of 0.1 seconds whose event handler increments a global integer. (Remember that create_timer takes the interval specified in milliseconds.) This integer will keep track of the time in tenths of seconds. Test your timer by printing this global integer to the console. Use the CodeSkulptor reset button in the blue menu bar to terminate your program and stop the timer and its print statements. Important: Do not use floating point numbers to keep track of tenths of a second! While it's certainly possible to get it working, the imprecision of floating point can make your life miserable. Use an integer instead, i.e., 12 represents 1.2 seconds.
Write the event handler function for the canvas that draws the current time (simply as an integer, you should not worry about formatting it yet) in the middle of the canvas. Remember that you will need to convert the current time into a string using str before drawing it.
Add "Start" and "Stop" buttons whose event handlers start and stop the timer. Next, add a "Reset" button that stops the timer and reset the current time to zero. The stopwatch should be stopped when the frame opens.
Next, write a helper function format(t) that returns a string of the form A:BC.D where A, C and D are digits in the range 0-9 and B is in the range 0-5. Test this function independent of your project using this testing template http://www.codeskulptor.org/#examples-format_template.py. (Just cut and paste your definition of format into the template.) Note that the string returned by your helper function format should always correctly include leading zeros. For example: format(0) = 0:00.0 , format(11) = 0:01.1 , format(321) = 0:32.1 , and format(613) = 1:01.3 .
Insert a call to the format function into your draw handler to complete the stopwatch. (Note that the stopwatch need only work correctly up to 10 minutes, beyond that its behavior is your choice.)
Finally, to turn your stopwatch into a test of reflexes, add to two numerical counters that keep track of the number of times that you have stopped the watch and how many times you manage to stop the watch on a whole second (1.0, 2.0, 3.0, etc.). These counters should be drawn in the upper right-hand part of the stopwatch canvas in the form "x/y" where x is the number of successful stops and y is number of total stops. My best effort at this simple game is around a 25% success rate.
Add code to ensure that hitting the "Stop" button when the timer is already stopped does not change your score. We suggest that you add a global Boolean variable that is True when the stopwatch is running and False when the stopwatch is stopped. You can then use this value to determine whether to update the score when the "Stop" button is pressed.
Modify "Reset" so as to set these counters back to zero when clicked.
Steps 1-3 and 5-7 above are relatively straightforward. However, step 4 requires some adept use of integer division and modular arithmetic. So, we again emphasize that you build and debug the helper function format(t) separately following the tips in the Code Clinic Tips page. Following this process will save you time. For an example of a full implementation, we suggest that you watch the video lecture on this mini-project.

Grading Rubric - 13 pts total (scaled to 100 pts)

1 pt - The program successfully opens a frame with the stopwatch stopped.
1 pt - The program has a working "Start" button that starts the timer.
1 pt - The program has a working "Stop" button that stops the timer.
1 pt - The program has a working "Reset" button that stops the timer (if running) and resets the timer to 0.
4 pts - The time is formatted according to the description in step 4 above. Award partial credit corresponding to 1 pt per correct digit. For example, a version that just draw tenths of seconds as a whole number should receive 1 pt. A version that draws the time with a correctly placed decimal point (but no leading zeros) only should receive 2 pts. A version that draws minutes, seconds and tenths of seconds but fails to always allocate two digits to seconds should receive 3 pts.
2 pts - The program correctly draws the number of successful stops at a whole second versus the total number of stops. Give one point for each number displayed. If the score is correctly reported as a percentage instead, give only one point.
2 pts - The "Stop" button correctly updates these success/attempts numbers. Give only one point if hitting the "Stop" button changes these numbers when the timer is already stopped.
1 pt - The "Reset" button clears the success/attempts numbers.




Code Clinic Tips

This page include helpful tips based on our experience in helping students in the "Code Clinic" (interactivepython@online.rice.edu). Be sure and take a look at these tips if you get stuck.

Tip #1

Make sure that format()returns (not prints) the formatted time as a string. Also, be sure to call format with the global timer counter in your draw handler to output the formatted time on the canvas. Remember: return a string in the definition of format, call format correctly in the draw handler.

We have also prepared a simple testing template for format() that you can use to make sure that your implementation of format() works correctly. Just cut and paste your implementation of format() into the template and run.

http://www.codeskulptor.org/#examples-format_template.py

----------------------------------------------------------------------------------------

We have built an experimental automated unit testing application for testing your format function. Simply click on the link below, enter a CodeSkulptor URL for your format code, and then submit to Owltest. Please be patient since the app takes a few seconds to load and run.

http://codeskulptor.appspot.com/owltest/?urlTests=iipp_f13.stopwatch_tests.py&urlPylintConfig=skip

Tip #2

Excellent student post (by Amir Elnemr) from previous session on computing digits in format

Here is the format function required logic and operations for anyone who is struggling with it. I tried my best to explain everything so I apologize if some parts seem redundant or too simple for you.

The problem: Given a number of tenths of seconds format a string output in the format A:BC.D where: A = the amount of minutes in that number B = the amount of tens of seconds C = the amount of seconds in excess of tens of seconds D = the amount of the remaining tenths of seconds

If a number doesn't have a value a value of 0 should be printed out as a place holder. Explanation: 9 seconds should be printed out as 09 seconds where 0 is represented by B and 9 is represented by C and if the amount of time is less than 1 min a 0 should be displayed in the minutes place represented by A

The solution: A simple formula using integer division and/or modulo operations can be used for each number (A to D) to determine its value. Recall that integer division drops any remainders in the quotient and modulo gives back the remainder of the division. in python the integer division operator is // and the modulo operator is % Examples: 5 // 2 = 2 (while 5 / 2 = 2.5 integer division drops the extra .5) 5 % 2 = 1 (because 5 / 2 = 2 with a remainder of 1)

Using this knowledge here is how you can get the value of each number (A to D): A (the amount of minutes) the given number is in tenth of seconds so

We need to divide it by 10 to be in seconds and
Divide that by 60 to be in minutes. (1 and 2 combined- divide by 600) So we can get A by dividing the tenths of seconds by 600 and dropping the remainder (using integer division)
B (the amount of tens of seconds)

We need to get the amount of whole seconds first and drop the remainder tenths of seconds with an easy integer division by 10
The number we have now can be split into two parts; The amount of minutes and the amount of seconds that are less than one minute. We can divide that number of seconds by 60 to give us the number of minutes but what we're really concerned with is the second part; the remainder of that division so we can use a modulo operation (the amount of seconds % 60) to get that remainder
Now that we have the amount of seconds how can we get the tens of seconds in that number? let's say the number is 34 we can simple divide it by 10 to get 3 and drop the remainder 4 with an integer division by 10
C (the amount of seconds in excess of tens of seconds) The same as B except in step 3 using the same 34 seconds example we don't need the 3 this time; instead we need the 4 We can simply accomplish this by using a modulo operation instead of the integer division by 10 to get the remainder (the number of seconds that are less than 10 seconds)

D (the amount of the remaining tenths of seconds) This is the simplest of all. The given amount of tenths of seconds can be split into two parts; the number of whole seconds and the number of tenths of seconds that are less than one second. using the same logic in B and C you can easily come up with the formula.

Useful tip: Integer division will yield 0 where normal division will yield a decimal point number less than 1

After all the values are determined what's left is to return them from the function as a string with the format of A:BC.D . so all you need is to return the concatenation of the string equivalent of those values and the pretty colon and point.

Tip #3

Important

As you build more and more complicated code, you should focus on building your code incrementally. By that, I mean: write a little bit of code, test/debug it, write some more code, test/debug it, etc. Writing 20-30 lines of code and THEN trying to debug it with lots of potential errors is a very bad idea. If you keep your program always in a close-to-working state, debugging it is MUCH easier. Again, I suggest following the mini-process development process.

Tip #4

Subtle bug that may arise if your code is poorly structured

We've had several people ask about a subtle bug where their code runs correctly the vast majority of the time, but occasionally awards a "success" on a time ending in "1". I 've seen this error in the Code Clinic. It's a subtle one that points out the trickiness of event-driven programming. Here is what I saw and how to fix it:

The draw handler calls format which, in addition to returning a string also assigns it to a global variable. In the error case, the string ends in "0".
The timer handler ticks and increments the counter to end in 1.
The stop button handler is called and stops the timer. However, instead of correctly checking the counter, it incorrectly checks the last character of the formatted string which is "0". Thus, the handler records an incorrect success.
The draw handler then calls format with the counter ending in 1 and produces a formatted time ending in "1".
So, to fix this error, make your test for a success be something of the form : (counter % 10) == 0.
