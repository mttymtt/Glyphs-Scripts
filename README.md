# ABOUT

These are Python scripts for use with the [Glyphs font editor](http://glyphsapp.com/).

# INSTALLATION

1. Put the scripts folder (or an alias) into the *Scripts* folder which appears when you choose *Script > Open Scripts Folder* (Cmd-Shift-Y): `~/Library/Application Support/Glyphs/Scripts/`
2. Then, hold down the Option (Alt) key, and choose *Script > Reload Scripts* (Cmd-Opt-Shift-Y). Now the scripts are visible in the *Script* menu
3. For some of the scripts, you will also need to install Tal Leming's *Vanilla*: Go to *Glyphs > Preferences > Addons > Modules* and click the *Install Modules* button. That’s it.

### git

I recommend to use git for getting the scripts, and syncing them on a regular basis. Use this git command for cloning the repository into your Scripts folder:

```bash
git clone https://github.com/mttymtt/Glyphs-Scripts ~/Library/Application\ Support/Glyphs/Scripts/mttymtt/
```

And this one for updating it:

```bash
cd ~/Library/Application\ Support/Glyphs/Scripts/mttymtt/
git checkout
```

If the terminal scares you, feel free to use one of the many readily available git clients.

# TROUBLESHOOTING

Please report problems and request features [as a GitHub issue](/issues). Make sure you have the latest version of the scripts and your app is up to date. And please, always **indicate both your Glyphs and macOS version.** Thank you.


# License

Copyright 2019 Matthew Smith (@mttymtt). This repository may contain code samples by Rainer Erich Scheichelbauer (@mekkablue), Georg Seifert (@schriftgestalt), and Tal Leming (@typesupply). Others may be credited in the docstring of individual scripts.

*The copy used in the About, Installation, git, and Troubleshooting sections are all pulled from Rainer Erich Scheichelbauer's [Glyphs-Scripts](https://github.com/mekkablue/Glyphs-Scripts) repository.*

Licensed under the Apache License, Version 2.0 (the "License");
you may not use the software provided here except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
