# ptcat
Linux cat command using python

Coursework Description

The objective of this coursework is to demonstrate that you have developed your programming
(scripting) skills to prove that you can use the skill to develop a useful tool.
Develop a tool to carry out same functions in a basic Linux command. The objective is to properly
understand the command, how it is working, what it does, and rewrite the command using your
preferred language. As an example, you can write a script to add a user into the system by studying
‘adduser’ command.

The report should contain:
• A specification of what it supposes to do
• Your code with adequately comments to properly understand it.
• An evaluation of how well it solved the specified need
• Screenshots or file printouts showing sample output or results.



This error comes when running with wrong input fie; Print message with "File Not Found" should be printed insted.

files in directory
┌──(sky㉿kali)-[~/Desktop]
└─$ ls -la                                                                                 1 ⨯
total 40
drwxr-xr-x  3 sky sky  4096 Jan  8 20:19  .
drwxr-xr-x 15 sky sky  4096 Jan  8 19:35  ..
-rw-r--r--  1 sky sky    32 Jan  8 18:48  hello.world
-rw-r--r--  1 sky sky 14294 Jan  8 11:26  iit
drwxr-xr-x  2 sky sky  4096 Jan  8 20:19 'old cats'
-rw-r--r--  1 sky sky  3300 Jan  8 19:40  ptcat
-rw-r--r--  1 sky sky    75 Jan  8 12:02  test
                                                  


error screen
┌──(sky㉿kali)-[~/Desktop]
└─$ python3.9 ptcat -h tes 
Traceback (most recent call last):
  File "/home/sky/Desktop/ptcat", line 64, in <module>
    file1 = open(fileName, 'r') #read line by line 'r' means readable
FileNotFoundError: [Errno 2] No such file or directory: 'tes'
                                                                 
