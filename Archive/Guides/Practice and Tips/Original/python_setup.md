# Setting Up Python and Installing Packages (Windows, MacOS)

This guide should get you started with getting a usable Python environment installed on your computer for Data Science classes. 
It will walk you through setting up a virtual environment, activating it, and installing packages.

## Step 1: Install Python 3

All of these commands will be run from a terminal (be that iTerm, Terminal, cmd, or Powershell; see the note about PowerShell limitations below).

### MacOS

You need a more modern version of Python3 than comes preinstalled; check your version by running

```bash
$> python3 --version
```

If you see a message saying python3 is not installed or a version number that is smaller than `3.8`, you should update your python by installing a stable version from https://python.org.

### Windows
If you run Windows 10, there are two possibilities for installing Python 3
#### Recommended: Microsoft Store
You may be able to install Python 3 directly from the Microsoft Store; this seems to be the easiest way to accomplish this. 
This only is available on newer builds of Windows 10.

#### Download and install manually (only option for previous versions of Windows or if the Microsoft Store gives you an error)
Download the installer from [here](https://python.org).
When you run the installer, it is very important that you check the box at the bottom of the setup window that says "Add Python 3.x to PATH" (the x depends on which version you downloaded)

***Note*** If you install python manually, you should run `python` instead of `python3` in the following steps.

## Step 2: Verify that you have Python 3

Open a *new* terminal window (CMD/Powershell, Terminal, xterm, etc), and run the following command: `python3 --version`
Depending on what version of python installed, you should see something that looks like:

```bash
C:\Users\nathane>python3 --version
Python 3.8.6
```
or
```bash
C:\Users\nathane>python3 --version
Python 3.9.0
```

The second number doesn't matter; what's important is that you have Python 3.x.y installed; if you see Python 2, you may need to install Python 3 again and make sure your path is set correctly.  You should have at least Python 3.8 (JupyterLab requires >= Python 3.5, other packages may have newer dependencies)

## Step 3: Create our Data Science Virtual Environment

A Virtual Environment is a way to isolate installed packages and libraries in a way that does not conflict with system installations of utilities.
To use a virtual environment we must first create it.  If you want to put your virtual environment in a specific location, open a terminal in that directory; I will just put mine in my home directory (`C:\Users\nathane`).
The virtual environment (which I will call a venv) will be created in a directory where we're currently at; I am going to name mine `ds-venv` (you can change the name if you want).

To create the virtual environment, run
```bash
python3 -m venv ds-venv
```

This creates a copy of the python environment in the directory ds-venv; check out the contents with `dir` or `ls` depending on your OS

```bash
C:\Users\nathane>dir ds-venv
Directory of C:\Users\nathane\ds-venv

10/14/2020  09:17 AM    <DIR>          .
10/14/2020  09:17 AM    <DIR>          ..
10/14/2020  09:17 AM    <DIR>          Include
10/14/2020  09:17 AM    <DIR>          Lib
10/14/2020  09:17 AM               119 pyvenv.cfg
10/14/2020  09:17 AM    <DIR>          Scripts
               1 File(s)            119 bytes
               5 Dir(s)  114,095,161,344 bytes free
```

At this point, our virtual environment is set up.  Whenever we want to use python, we need to activate the environment

## Step 4: Activate the environment

### MacOS/Linux
`source ds-venv/bin/activate`

### Windows

Make sure you use `cmd` or [allow scripts to be run from PowerShell](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.1)

`ds-venv\Scripts\Activate`

You should now see that your terminal has changed:

```bash
C:\Users\nathane>ds-venv\Scripts\Activate

(ds-venv) C:\Users\nathane>
```

## Step 5: Installing packages
At this point, we can install packages.
The normal way to install a package is to run the command:

```bash
pip install <packagename>
```

You can specify multiple packages to install by separating the list with spaces.

### Installing Numpy (Windows only)

A lot of packages we will use require the `numpy` package; unfortunately on Windows the newest version exposes a bug in the Windows math co-routines.
Before installing anything else, we can specify the version of numpy to get installed so we have a safe working version:

```bash
pip install numpy==1.19.3
```

If at any time you need a specific version of a package, you can specify it with the `==version` addition to the package name.

### Installing JupyterLab and Matplotlib

Run

```bash
pip install jupyterlab matplotlib
```
You should see a lot of downloads; it's grabbing all of the prerequisites from various sources and installing them.

When it's done, test that it installed by running `jupyter lab`:

```text
(ds-venv) C:\Users\nathane>jupyter lab
```

You should get a new browser window to pop up with your running instance of JupyterLab!  Success!

If your instructor provides you a text file with requirements (I'll call it `requirements.txt`), you can automatically install all of the packages by running `pip install -r path/to/requirements.txt` (replace it with the path to `requirements.txt`)

# Using your Environment

## Installing other packages

Once you have activated your environment, you can install new packages in the same way you installed jupyterlab: `pip install <package name>`.
Your instructor will provide a list of packages you may need for the class.

If you open a shell and install packages while you are running JupyterLab, you will need to restart your kernel (using the menu or the refresh button in the Notebook interface) to pick up the new packages.

## JupyterLab

One option (if you want to avoid using a terminal) is to open the directory where you created your virtual environment, and run `jupyter-lab` from either the `bin` or `Scripts` directory, depending on whether you're on MacOS or Windows, respectively.  Windows may open a web browser that says it cannot find the file; copy and paste the URLs (usually `httplocalhost:8888/?token=<sometoken>`) and paste it in your browser.
You should be able to create shortcuts to this `jupyter-lab` to make it easier to find.  Consult your OS and the internet on how to do this correctly.

Otherwise:

1. Open a terminal
1. Activate your virtual environment
1. run `jupyter lab`

## IDE Support (PyCharm, etc)

Configure your interpreter in your IDE to point to `ds-venv\Scripts\python.exe` or `ds-venv/bin/python` (depending on Windows or *NIX)
