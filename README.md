<p align="center">
  <img src="https://github.com/TelegramTools/TLSecret/raw/master/images/Intro.png">
 </p>
<p align="center">
  <img src="https://github.com/TelegramTools/TLSecret/raw/master/images/SecretModeLabel.png">
 </p>

# TLSecret

TLSecret allows you to grant access to your Telegram account in other Telegram Tools apps, which may require logging in two users (TLMerger, TLRevert and TLImporter for instance).
This is known as "Secret Mode" in all of my apps. 
They can be indetified by the "Compatible with Secret Mode" label.

# How to use?

When using TLSecret, we will be using two different apps at the same time. Some explanations:

- The **listener** app: The Telegram Tools' app where you want to be logged in (TLImporter, TLMerger, TLRevert...)
- TLSecret, which will help to grant access to a Telegram account in any of the **listener** apps.

The instructions below considers that you will be the person using TLSecret, while your partner will be using any of the **listener** apps.
The **listener** app can be running in a remote computer, no physical presence is required to authenticate you succesfully!

## Preparation

Before you can do anything with TLSecret, your partner must prepare the **listener** app:

- All **listeners** app will prompt the user, at any point, whether using the "Secret Mode" or not. Your partner should agree to use it
- Your partner's chat list will be displayed in the window. He must choose you from the list.
- The app will display **Waiting for a response...**.

Once the app is **Waiting for a response...**, you will be able to use TLSecret to grant your partner's access into your Telegram account.

## Granting access

If your partner's **listener** app is already *Waiting for a response...*, open TLSecret and perform these simple steps:

- Log in in Telegram as you would normally do: Input your phone number, verification code and password.
- (The app will be encrypting your details, which may take a few seconds, but don't freak out if you see that it stays blank for a while!)
- Your chat list will be printed inside the window. Choose your partner from the list.
- Wait until the authentication is done succesfully in your partner's computer.

You are done!
At this point, you will have full control over your authorization in Telegram. Just by pressing ENTER, you will be able to revoke the authorization and discard that session.
If you have closed the app after authenticating, you will be able to revoke the session by opening it again and pressing ENTER.

## What if something else goes wrong?

As stated in the app's disclaimer, there is no perfect encryption and the 100% security doesn't exist. In fact, there are many security flaws in the app: The password for decrypting the file could be easily obtained from the binaries, after decrypting the session file, it could be read before it's processed by the **listener** app, the Telegram's AuthKey is stored in the RAM's of your partner's computer, which can also be read if he has the proper knowledge. Although I consider that TLSecret is really safe to use and has proper security, you need to know that nothing is perfect and I don't suggest you to use this app with completely unknown people, but at least, with some people you trust a little.
Remember that you also will be able to revoke any session if everything fails, using other Telegram apps: Go to *Settings - Privacy and Security - Active Sessions* and revoke any session you don't know.

# Downloads

You can always find the latest version of the app in the [Releases tab](https://github.com/TelegramTools/TLSecret/releases).

Binaries for Windows are included and bundled as an .exe executable. If you want to use this python script in Mac or Linux, you will be able to, using the compiled binaries under the *bin* folder. Whenever you are running the compiled binary, make sure that you have Python3 installed in your system and also pip. Run this command: `pip install -r requirements.txt` before running the app.

# Use from sources

Make sure that you replace the `apiID`, `apiHash` and `password` variables in your own script. Read instructions [here](https://core.telegram.org/api/obtaining_api_id) for getting the `apiID` and `apihash` variables of Telegram.

Remember that you need to use the same `password` variable in the **listener** app and in TLSecret, otherwise encryption will fail.

# Credits

Huge thanks to [Telethon](https://github.com/LonamiWebs/Telethon), and his great creator, [Lonami](https://github.com/Lonami), who always was up to answering questions and helping in development. I'm so grateful for his patience :).
Also, huge thanks to [pyAESCrypt](https://github.com/marcobellaccini/pyAesCrypt), which simplified a lot the process of encrypting/decrypting the session files.
Thanks to the [PyInstaller](https://www.pyinstaller.org/) team for their great tool, which I used to build the Windows binaries.

Also, huge acknowledgements to Telegram for making such a great messenger!

**Give always credits to all the original authors and owners when using some parts of their hard work in your own projects**
