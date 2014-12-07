## Workflows Help Workflow ##

### NOTE ###
This is a really old workflow, the current "old" version can be downloaded from [Packal](http://www.packal.org) -- you can also find it in this repo. However, it does __not__ work with Yosemite.

There is a quick fix hosted in this repo: [download](https://github.com/shawnrice/alfred2-workflow-help/raw/master/whw.alfredworkflow). It does have a different Bundle ID than the old one, so when I finally find the time to give the new one all the functionality that it needs, then it won't automatically update through the Packal Updater. Still, it's a fix until I find the time to get back to this project.

------

Currently, there is just one command: __help__.

The workflow crawls through your installed workflows and pulls out the information about keywords and hotkeys among others and compiles a temporary help file that it shows view a quicklook debug utility.
 
Github Repository here: https://github.com/s...2-workflow-help
Download here: https://github.com/s....alfredworkflow
 
Has Alleyoop support.
 
The file can take a few seconds to generate, and it is generated every time. This will change in a later version.
 
##### Quirks and files included: #####
* This workflow displays the file generated through a debug mode of Quicklook (so that the focus doesn't need to switch to finder), so there will always be a "[debug]" message on the window.
* I've included a Quicklook Markdown generator in the workflow to make sure that the file always displays correctly.
* There are some images that are included that are not _currently_ used (these are in the "images" folder). They will be used to show the hotkeys later.
* ALP is included. Right now, only part of the library is used, so I might strip it down to make the workflow smaller.
* _So, the size of the workflow is larger because of these things in there._

##### Dependencies and Testing: #####
Built on Mountain Lion (10.8.3)
_Should be compatible for all systems as the only dependencies are included in the workflow._

##### Roadmap: #####
* Clean up the help.py code.
* Cache the generated file and update it only when the workflow folder changes.
* Make the display of the file nicer.
* Add in more images to the file.
* Display individual workflow helps (show the data for that workflow as well as the readme.md file).
* Have a better precedent to show either text or subtext for the command help.
* Try to figure out a way to describe arguments taken for different commands / hotkeys.
* Make it understand file actions better.
* Clean up the file/folder structure.
* Some other ideas are written into the source code
* Maybe some more... any ideas?
 
##### Screenshot: #####

<img src="https://github.com/shawnrice/alfred2-workflow-help/raw/master/screenshot.png">

