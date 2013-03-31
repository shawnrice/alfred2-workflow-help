#!/usr/bin/python

#Volatile:~/Library/Caches/com.runningwithcrayons.Alfred-2/Workflow Data/[bundle id]

#Non-Volatile:~/Library/Application Support/Alfred 2/Workflow Data/[bundle id]

# To any pythoners out there who may read this script: this is probably atrocious code
# but it's my first python script. Forgive me. Maybe join the github development 

import alp
import re
import os
import getpass

user = getpass.getuser()
dir = "/Users/" + user + "/Library/Application Support/Alfred 2/Workflow Data/com.help.shawn.rice"
edir = "/Users/" + user + "/Library/Application\ Support/Alfred\ 2/Workflow\ Data/com.help.shawn.rice"

if not os.path.isdir(dir):
	os.makedirs(dir)

output_file = "alfred-help.md"

location = dir + "/" + output_file

file = open(location, "w")



hotmod = {		131072 : "shift",

				262144 : "control",

				393216 : "shift+control",

				524288 : "option",

				655360 : "shift+option",

				786432 : "control+option",

				917504 : "shift+control+option",

				1048576 : "command",

				1179648 : "shift+command",

				1310720 : "control+command",

				1441792 : "shift+control+command",

				1572864 : "option+command",

				1703936 : "shift+option+command",

				1835008 : "control+option+command",

				1966080 : "shift+control+option+command"

}



hotarg = {		0 : "No Argument",

				1 : "Selection in OS X",

				2 : "OS X Clipboard Contents",

				3 : "Text"

}



hotaction = { 	0 : "Pass through to Workflow",

				1 : "Show Alfred"

}







listdir = os.getcwd() + "/../"

# list of directories in the 

# print "Folders found in ", listdir

dirs = os.walk(listdir).next()[1]



# walk through the directory list array

i = 1 #currently setup just to read the first valid info.plist file



workflows = {}



for item in dirs:

	if item != "alfred-help":



			plist = listdir + "/" + item + "/info.plist"

 

 			folder = item

			 

			info = alp.readPlist(plist)

#.replace(" ","\ ")

			buffer = "<img src=\"file://localhost/" + listdir + item + "/icon.png\" height=\"50px\">      <font size=\"5em\"><b>" + info['name'] + "</b></font>\n<hr>"
			buffer += "\n\n_(" + info['bundleid'] + ") by " + info['createdby'] + "_\n"

			if "disabled" in info:

				if info['disabled']:

					buffer +=  " (<font color=\"red\">disabled</font>)\n"

#				else:

#					buffer +=  "\n\t\tCurrently enabled."

#			else:

#				buffer +=  "\n\t\tCurrently enabled."

			if info['description']:

				buffer +=  "######<font color=\"gray\">" + info['description'] + "</font>\n"

			else:

				buffer +=  "\n"

				

			i += 1



			commands = "\t"

			hotkeys = "\t"

			for item in info['objects']:

				if item['type'] == "alfred.workflow.input.keyword":

					if commands == "\t":

						commands = "\r\n* " + item['config']['keyword']

					else:

						commands += "\r\n* " + item['config']['keyword']

					if "text" in item['config']:

						commands += " (" + item['config']['text'] + ")"

					elif "subtext" in item['config']:

						commands += " (" + item['config']['subtext'] + ")"

				if item['type'] == "alfred.workflow.trigger.hotkey":

					if hotkeys != "\t":

						hotkeys += "\n\n"

					if "hotmod" in item['config'] and item['config']['hotmod']:

						hotkeys += "\r\n* " + hotmod[item['config']['hotmod']] + " " + item['config']['hotstring']

					else:

						hotkeys += "\r\n* " + "<font color=\"red\">Not yet defined</font>"

					if item['config']['argument']:

						hotkeys += " (Takes " + hotarg[item['config']['argument']] + " as an argument)"						

				if item['type'] == "alfred.workflow.input.scriptfilter":

					if commands == "\t":

						commands = "\r\n* " + item['config']['keyword']

					else:

						commands += "\r\n" + "* " + item['config']['keyword']

					if "subtext" in item['config']:

						commands += " (" + item['config']['subtext'] + ")"

					elif "text" in item['config']:

						commands += " (" + item['config']['text'] + ")"

					elif "title" in item['config']:

						commands += " (" + item['config']['title'] + ")"

			buffer += "\n\n"

			if commands != "\t":						

				buffer += "__Commands__\n" + commands

			if hotkeys != "\t":

				buffer += "\n\n__Hotkeys__\n" + hotkeys

			

			workflows[info['name']] = buffer


buffer = ""

for key in sorted(workflows.keys(), key=lambda x: x.lower()):

#	buffer += "## " + key + "\n"

	buffer += workflows[key] + "\n\n<br><br>"

buffer = buffer.encode('utf-8')

file.write(buffer)

file.close()

command = "qlmanage -p " + edir + "/" + output_file + " -c .md -g libraries/QLMarkdown.qlgenerator >/dev/null 2>&1 &"
os.system(command)


##

#			Add in readme files for next version

##			

#			if 'readme' in info:

#				readme = info['readme']

#			else:

#				print "No readme file included."

				

#			re.sub("^([\#]{1,})([a-zA-Z0-9 :.-]{1,})([\#]{1,})",

#					"<b>\2</b>",

#					readme)





