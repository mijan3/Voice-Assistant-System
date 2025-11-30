# Voice-Assistant-System


A Voice Assistant System Name as (Peya). Peya is a Python based that can interact with the user through speech
recognition, perform tasks like opening applications,searching on Google or Wikipedia, Playing music randomly, telling jokes,and having samal talk.

This Project uses speach recognition and text to speech (TTS) to provide a hands-free assistant experience similar to Iron Man's JARVIS.

## Features
Greet the user according to the time of day(Morning,Afternoon,Evening)

Recognize voice commands using Google Speech Recognition

Speak responses using pyttsx

Time & Date announcements

Wikipedia serch with spoken summary

Open websites like Google,Facebook,Youtube

Play random music for a specified folder

Open system Applications: Calculater,Notepad,CMD

Open Calendar(Google Calendar via Browser)

Tell jokes and respond to basic small talk

GEMINI AI integration for dynamic responses

Take Screenshots on command

Exit gracefully with a voice command



## Requiremtns 
Python 3.11 or higher


# How to run?

1.Create a virtual enviroment:

```bash
conda create -n peya python=3.11 -y
```
2.Activate virtual environment:

```bash
conda activate peya 
```
3. Install required packages:
```bash
pip install -r requirments.txt
```
4. Run the peya:
```bash
python peya.py
```
## For exe file conversion
```bash
pip install pyinstaller
```
```bash
pyinstaller --onefile peya.py
```
## Author
**Mijanur Rahman**
- GitHub: [Mijanur-Rahman](https://github.com/mijan3)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

