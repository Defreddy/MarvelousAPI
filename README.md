# MarvelousAPI
An advanced take on the Marvel API challenge.

![image](https://user-images.githubusercontent.com/57659570/136712809-1f7d6d53-5698-4aa8-8d7d-969a311c0bf5.png)

Clean code:
Code is as structured as possible. I tried to use as many definitons as possible.
The most sloppy code piece is the "While True" loop which is just a huge block of code...
Comments and indentation are included in 99% of the python file.

Web Service Connectivity:
Custom web service connectivity without the use of 3rd party software. There is a 3rd party wrapper tool available for the Marval API for easier access; which was NOT allowed for this project.

https://pypi.org/project/marvel/

Authentication:
You can authenticate using your own PRIVATE and PUBLIC API keys in 1, 2 ,3.

Input & Output:
The input is asked every once in a while. The user only utilises the "enter character" input field.
Output is supplied in a variety of ways: multiple tables with a lot of information.
A suggestions table is included in the validation checker in case you guess "wrong".
Unfortunately on second faulty guess the program shuts down due to suggestions being "uncallable".
This is the only bug in the program - otherwise it works 99% of the time.

Extra:
all extra's are included.
Error handling: disabled warning (in the beginning) + checks most common error codes: 200; 401, 403 (client-side) and 500+ (server-side).
Input validation: is included in the "While True" loop. Checks the input, provides suggestions and ask for a new input. As said before; on second faulty guess program shuts down. On first good try it completes, on second good try it completes too (thanks to suggestions).
Extra functionalities: this is the suggestions tab that is included after entering a wrong character (or only a part of a character). The entire program is based on called a correct character; thus this added feature gives the user an extra option in providing a correct character, thus the program being more usable by more users. The program also provides more insights to links (wiki,...) and characters available in comics, series, stories and events.

Don't forget the Marvel copyright at the end of the program. ;) 

Cheers, enjoy the show!
