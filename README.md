<p align="center">
  <img src="https://github.com/TelegramTools/TLSecret/raw/master/images/Intro.png">
 </p>

# TLSecret
An small script for simplifying the authentication of other Telegram's users in all Telegram Tools apps

Some Telegram Tools apps requires you to sign in two users in Telegram. With TLSecret, you can authenticate and pass your Telegram's keys using the "Secret Mode" on all Telegram Tools apps, without the need of giving your phone number, code and password to your partner's using one of the other Telegram Tools apps.
This way, you have full control of your account whenever you want or need to use apps like TLImporter with another person.

# How to use it?

**This instructions assumes that the person who is reading this is the one who wants to grant access into a Telegram account to a person using any of the Telegram Tools apps.**

When using the "Secret Mode", there are two apps involved: 
· The **listener** app (TLRevert, TLMerger, TLImporter and any other Telegram Tools' app that can use the "Secret Mode" to login users). This will be the app where you want to be logged in remotely. It can be running in your partner's computer
· TLSecret, which will be running in your own computer.

As you are the one who wants to grant access to your account, you will be using TLSecret app.

## Preparation

The person using the **listener** app must have entered into the "Secret Mode" (every Telegram Tools app which supports "Secret Mode" will prompt the user at some point whether using "Secret Mode" or not).
After entering into the "Secret Mode", the chat list of your partner will be displayed. He must choose you (the person using TLSecret). After that, a message saying "Waiting for a response..." will be displayed in his chat.

## Using TLSecret

Once the **listener** app is in "Waiting for a response..." mode, you can use TLSecret.

Input your phone number, verification code and password, just like you would do in other Telegram app. Your chat list will be displayed after the authentication is done succesfully. Choose your partner there (the person using the **listener** app).

After that, TLSecret will work behind-the-scenes, and will authorize yourself in your partner's computer. You are done!

## Final tips

After the authentication is done succesfully in the **listener** app, you will be always in control of your session. By pressing ENTER, you will revoke the access to your account and log out your friend of Telegram.
If you have closed the app after the authorization is done, don't worry!. Next time you run it, you will be able to revoke the session by pressing ENTER as well.

# Credits

Secret mode couldn't be possible without [Telethon](https://github.com/LonamiWebs/Telethon), and his great creator, [Lonami](https://github.com/Lonami), who always was up to answering questions and helping in development. I'm so grateful for his patience :).
Also, huge thanks to [pyAesCrypt](https://github.com/marcobellaccini/pyAesCrypt)
Huge thanks to all the team behind [PyInstaller](https://www.pyinstaller.org/), which I used to build the Windows binaries.

**Give always credits to all the original authors and owners when using some parts of their hard work in your own projects**

