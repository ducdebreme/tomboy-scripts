#!/usr/bin/env python
#
#   Create a note of which lists all notes of a given NOTEBOOK
#   so one can easily export all the notes to an HTML file
#

import dbus, time

notebook = "2012-09 JS Days in Berlin"

# Get the D-Bus session bus
bus = dbus.SessionBus()

# Access the Tomboy D-Bus object
obj = bus.get_object("org.gnome.Tomboy","/org/gnome/Tomboy/RemoteControl")

# Access the Tomboy remote control interface
tomboy = dbus.Interface(obj, "org.gnome.Tomboy.RemoteControl")

notes_links = ""

#for note in tomboy.ListAllNotes():
#system:notebook:2012-09 js days in berlin
for note in tomboy.GetAllNotesWithTag("system:notebook:" + notebook):
  notes_links += tomboy.GetNoteTitle(note) + " \n"
  #print tomboy.GetTagsForNote(note)
  #print tomboy.GetNoteTitle(note) + " \n" 

note_title = "Notebook - " + notebook
uri = tomboy.FindNote(note_title)

if uri == "":
  uri = tomboy.CreateNamedNote(note_title)
  
print uri + "\n"
print tomboy.NoteExists(uri)

tomboy.SetNoteContents(uri, note_title + "\n\n" + notes_links)
tomboy.DisplayNote(uri)
