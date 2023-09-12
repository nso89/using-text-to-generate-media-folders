# using-python-comments-to-generate-a-markdown-file
Using Text to Generate Media Folders.
    
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)
* [Configuration](#configuration)

#### <a name="prerequisites"></a>Prerequisites
* A complete install of `Python 3.x`.

#### <a name="setup"></a>Setup
1. Under your `USERPROFILE`, extract `using-text-to-generate-media-folders-main.zip`.

**Example**:
```
C:\Users\nso89\using-text-to-generate-media-folders-main
```
#### <a name="running-the-script"></a>Running the Script
1. Open `cmd.exe` and change the directory to the `using-text-to-generate-media-folders-main` folder.

**Example**:
```
C:\Users\nso89>cd using-text-to-generate-media-folders-main
```
2. Start the `main.py` script.

**Example**:
```
C:\Users\nso89\using-text-to-generate-media-folders-main>python main.py
```

3. It asks you for the `folder` name:

**Example**:
```
Folder Name: Trip to Banff National Park
```
4. Under `Downloads`, the `main.py` generates `1` folder and `2` subfolders:

**Example**:
```
C:\Users\nso89\Downloads\Trip to Banff National Park
C:\Users\nso89\Downloads\Trip to Banff National Park\Sets
C:\Users\nso89\Downloads\Trip to Banff National Park\Video
```

#### <a name="configuration"></a>Configuration
If you need to change the `SOURCE_PARENT`:

1. Open the `main.py` script in any text editor.
2. Locate the `SOURCE_PARENT` variable.

**Example**:
```
SOURCE_PARENT = Path.home().joinpath("Downloads")
```
3. When you finish changing the variables, save and close the editor.
