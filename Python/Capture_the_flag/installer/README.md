# CAPTURE THE FLAG

## An application for you to organize your files automatically.

### You only need to add a three letters tag before the file's name while you're downloading it.
### For this application to work properly (at least on MacOS) you will need to associate it with the _Automator_ app.


## INSTALLING:

1. Download and unzip the CTF file.
2. Execute the CTF_install file. you can do it by double-clicking it or by Terminal:

```bash
./ctf_install
```

<p> When you install it Two tab will pop open. The first one is to set your Desktop path. The Second one is for you to set your firsts TAGs and tagged folders. </p>
<p>A TAG is a set of three uppercase letters. i.e. ART , for an arts' folder. </p>
<p>When you use it on the files, you must type two strokes (--) right after the TAG. i.e. "ART--AnMazingArt.jpg"</p>

---

## AUTOMATING:

<p>For you to automate it, you will need to use the <em>Automator</em> app. You can find in the Lauchpad or by searcing it in the Spotlight <code>command + spacebar</code>.</p>
<p>When it's open you must follow this is steps:</p>

1. Select the option called _Folder Action_.
2. Right in the upper section of the window. Choose your _Download_ folder.
3. Search in the library (of commands) for _Execute Shell Script_. Click and drag it to the main interface.
4. On it, select the ``/bin/bash`` shell and type the following sequence:

```bash
cd #your/desktop/path
./.AUTOCTF
```
4. Save and close it.

### Now you have an automated file filter.

---

## BONUS:

<p>Another suggestion we give, it to make a alias for the <em>automatic files</em> folder found in the HOME of the User.<code>cd $HOME</code>.</p>