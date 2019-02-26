# hashCracker by Austin Tyler
Dictionary attack on SHA1 hashes

# How to run this program
1. Make sure you have [Python 2.7](https://www.python.org/download/releases/2.7/) installed
1. Run hashCraacker.py in the command line with the hash you wish to crack as the first argument and the directory of password_list.txt as the second

# An example
> C:\Users\atyler\PycharmProjects\hashCracker\venv\Scripts\python.exe C:/Users/atyler/PycharmProjects/hashCracker/hashCracker.py 801cdea58224c921c21fd2b183ff28ffa910ce31 C:/Users/atyler/PycharmProjects/hashCracker/password_list.txt

> The password is vjhtrhsvdctcegth

> Guesses: 999968

> Time elapsed: 2.40499997139

# Homework Answers
1. b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 = letmein, 16 guesses
1. 801cdea58224c921c21fd2b183ff28ffa910ce31 = vjhtrhsvdctcegth, 999,968 guesses
1. ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 = harib salted with slayer, 1,546,154 guesses
