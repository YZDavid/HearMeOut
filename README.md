# HearMeOut (5648)
NUS 22/23 Orbital Project

**Level of Achievement**: Project Apollo 11  
**Project Scope**: HearMeOut aims to summarise text and convert it into audio with the use of Artificial Intelligence 

With the help of Artificial Intelligence Tools, large chunks of texts can be easily converted into smaller bite sized instead. In addition, it also enables users to have the option of hearing the summarized text instead. This is done with the help of libraries such as **`Hugging Face's Transformers`**, **`NLTK (Natural Language Toolkit)`** and  **`gTTS (Google Text-to-Speech)`**

## Installation
### 0. Ensure `Python` is already installed on your system.

* `Python` installation for [Windows/Mac/Linux](https://www.python.org/downloads/)

### 1. Download a copy of this repo

Navigate into the folder you want the repository to be in. Download a copy of this reposity by running the command in the terminal window of that folder:
```
git clone https://github.com/YZDavid/HearMeOut.git
```

### 2. Create a virtual environment within the repo

Get inside the workspace of the folder:
```
cd HearMeOut
```
Setup a virtual environment with the following command 
For **Windows**:
```
python -m venv venv
```
For **Mac**:
```
python3 -m venv venv
```
Note that as of writing this README, The app is running on `Python 3.11.3`. If there is any issues with Python versions and the dependencies listed in `requirements.txt`,
you may consider looking into creating virtual environments with specified Python versions. You can look into the Python library [virtualenv](https://virtualenv.pypa.io/en/latest/)
if you need specific Python versions.

### 3. Activate the virtual environment

Activate the virtual environment by running the following command
For **Windows**:
```
venv/Scripts/activate
```
For **Mac**:
```
source venv/bin/activate
```
Refer to the [venv docs](https://docs.python.org/3/library/venv.html) for more details

### 4. Install dependencies

Run the following command to install all dependencies needed for this app to run
```
pip install -r requirements.txt
```

### 5. Launch application

Finally, launch the application by running the python program server.py
```
python server.py
```

## Usage
### 1. Accessing the website

Ensure that the server is running after you have launched the program with `python server.py`.\
It will be hosted on `127.0.0.1:5000` (localhost port 5000) and you will be able to access it on the browser if it is running.

### 2. Summarising text

Click on "Get Started" and you will be taken to the `Text Summariser` page. You may click on the settings icon to change the output settings.  
* Audio: Chooses whether audio file is generated
* Auto: Let the summariser automatically generate the output
* Percentage of Original: Set a target % to how long you want your summary to be compared to the original file
Simply enter a chunk of text you want summarised inside the input text box.  
Once done, click on summarise to generate a summary of the input text. **Do note that it will take awhile**

### 3. Summarising URLs

You can access this via the navbar on top, click on `Summarisers > URL Summariser` to access the page. Similarly, you may click on the settings option to change the output settings.
* Audio: Chooses whether audio file is generated
Simply enter a valid URL link to a news article or any parseable webpage, and it will attempt to summarise the page for you. The ability of this function really depends on the website.  
Once done, click on summarise to generate a summary of the input text.

### 4. Latest Summary

This page will show you your most recent summary, if any. It will also be the page you are taken to once you summarise your text/content from URL.

### 5. History
You can see all your past summaries in this page. You can download the audio files at will, and delete the whole summary if you choose to do so.

