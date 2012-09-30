#!/usr/bin/env python
#
#   This script creates a tomboy note containing link to each other note
#   so one can easily export all the notes to an HTML file
#
#	author:Pedro
#
#   Check out lamehacks.net for more lame scripts and stuff

import dbus, time

note_title = "Note Index"

# Get the D-Bus session bus
bus = dbus.SessionBus()

# Access the Tomboy D-Bus object
obj = bus.get_object("org.gnome.Tomboy","/org/gnome/Tomboy/RemoteControl")

# Access the Tomboy remote control interface
tomboy = dbus.Interface(obj, "org.gnome.Tomboy.RemoteControl")

notes_links = ""

for note in tomboy.ListAllNotes():
  notes_links += tomboy.GetNoteTitle(note) + " \n"

uri = tomboy.FindNote(note_title)
if uri == "":
  uri = tomboy.CreateNamedNote(note_title)

tomboy.SetNoteContents(uri, note_title + "\n\n" + notes_links)
tomboy.DisplayNote(uri)
