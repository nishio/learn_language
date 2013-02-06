#!/usr/bin/env python
import subprocess
import sys
import os
if len(sys.argv) > 1:
    scriptname = sys.argv[1]
    subprocess.call(["/Applications/Squeak-4.3-All-in-One.app/Contents/MacOS/Squeak VM Opt",
                     "/Applications/Squeak-4.3-All-in-One.app/Contents/Resources/WithOSProcess.image",
                     os.path.abspath(scriptname)])
else:
    # run without script
    subprocess.call(["/Applications/Squeak-4.3-All-in-One.app/Contents/MacOS/Squeak VM Opt",
                     "/Applications/Squeak-4.3-All-in-One.app/Contents/Resources/WithOSProcess.image"])

