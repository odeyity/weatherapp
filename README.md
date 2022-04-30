# Weather Application built with PyOWM

Credits:
PyOWM - https://github.com/csparpa/pyowm
OWM - https://openweathermap.org/

This program is probably one of the easiest things to make, as it is simple and everything you need is handed straight to you
but I decided to make it EVEN more simple so you just have to add your OWM Weather token and you're done. Feel free to make a
much better version, if I see it, I will probably delete this repo.

How to create an API Token with OWM: 
go to https://openweathermap.org/ and sign up. Navigate to https://home.openweathermap.org/api_keys and copy the key.
Replace API TOKEN with the key

1 account should suffice (60 api calls/min), but if you are making a large scale version, I would suggest creating other accounts with API keys and making the python program find one which has not reached its api call limit.
