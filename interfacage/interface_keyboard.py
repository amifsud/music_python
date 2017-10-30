#!/usr/bin/python
#
# pyxhook -- an extension to emulate some of the PyHook library on linux.
#
#    Copyright (C) 2008 Tim Alexander <dragonfyre13@gmail.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#    Thanks to Alex Badea <vamposdecampos@gmail.com> for writing the Record
#    demo for the xlib libraries. It helped me immensely working with these
#    in this library.
#
#    Thanks to the python-xlib team. This wouldn't have been possible without
#    your code.
#    
#    This requires: 
#    at least python-xlib 1.4
#    xwindows must have the "record" extension present, and active.
#    
#    This file has now been somewhat extensively modified by 
#    Daniel Folkinshteyn <nanotube@users.sf.net>
#    So if there are any bugs, they are probably my fault. :)

import sys
import re
import threading

from Xlib import X, XK, display
from Xlib.ext import record
from Xlib.protocol import rq

#######################################################################
########################START CLASS DEF################################
#######################################################################

class HookManager(threading.Thread):
    """This is the main class. Instantiate it, and you can hand it KeyDown and KeyUp (functions in your own code) which execute to parse the pyxhookkeyevent class that is returned.

    This simply takes these two values for now:
    KeyDown = The function to execute when a key is pressed, if it returns anything. It hands the function an argument that is the pyxhookkeyevent class.
    KeyUp = The function to execute when a key is released, if it returns anything. It hands the function an argument that is the pyxhookkeyevent class.
    """
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.finished = threading.Event()
        
        # Are shift and caps pressed ?
        self.ison = {"shift":False, "caps":False}
        # Compile our regex statements.
        self.isshift = re.compile('^Shift')
        self.iscaps = re.compile('^Caps_Lock')
        self.shiftablechar = re.compile('^[a-z0-9]$|^minus$|^equal$|^bracketleft$|^bracketright$|^semicolon$|^backslash$|^apostrophe$|^comma$|^period$|^slash$|^grave$')
        self.logrelease = re.compile('.*')
        self.isspace = re.compile('^space$')
        
        # Assign default function actions (do nothing).
        self.KeyDown = lambda x: True
        self.KeyUp = lambda x: True
        
        self.contextEventMask = [X.KeyPress,X.MotionNotify]
        
        # Hook to our display.
        self.local_dpy = display.Display()
        self.record_dpy = display.Display()
        
    def run(self):
        # Check if the extension is present
        if not self.record_dpy.has_extension("RECORD"):
            print "RECORD extension not found"
            sys.exit(1)
        r = self.record_dpy.record_get_version(0, 0)
        print "RECORD extension version %d.%d" % (r.major_version, r.minor_version)

        # Create a recording context; we only want key and mouse events
        self.ctx = self.record_dpy.record_create_context(
                0,
                [record.AllClients],
                [{
                        'core_requests': (0, 0),
                        'core_replies': (0, 0),
                        'ext_requests': (0, 0, 0, 0),
                        'ext_replies': (0, 0, 0, 0),
                        'delivered_events': (0, 0),
                        'device_events': tuple(self.contextEventMask), #(X.KeyPress, X.ButtonPress),
                        'errors': (0, 0),
                        'client_started': False,
                        'client_died': False,
                }])

        # Enable the context; this only returns after a call to record_disable_context,
        # while calling the callback function in the meantime
        self.record_dpy.record_enable_context(self.ctx, self.processevents)
        # Finally free the context
        self.record_dpy.record_free_context(self.ctx)

    def cancel(self):
        self.finished.set()
        self.local_dpy.record_disable_context(self.ctx)
        self.local_dpy.flush()
    
    def printevent(self, event):
        print event
    
    def processevents(self, reply):
        if reply.category != record.FromServer:
            return
        if reply.client_swapped:
            print "* received swapped protocol data, cowardly ignored"
            return
        if not len(reply.data) or ord(reply.data[0]) < 2:
            # not an event
            return
        data = reply.data
        while len(data):
            event, data = rq.EventField(None).parse_binary_value(data, self.record_dpy.display, None, None)
            if event.type == X.KeyPress:
                hookevent = self.keypressevent(event)
                self.KeyDown(hookevent)
            elif event.type == X.KeyRelease:
                hookevent = self.keyreleaseevent(event)
                self.KeyUp(hookevent)

    def keypressevent(self, event):
        matchto = self.lookup_keysym(self.local_dpy.keycode_to_keysym(event.detail, 0))
        if self.shiftablechar.match(self.lookup_keysym(self.local_dpy.keycode_to_keysym(event.detail, 0))): ## This is a character that can be typed.
            if self.ison["shift"] == False:
                keysym = self.local_dpy.keycode_to_keysym(event.detail, 0)
                return self.makekeyhookevent(keysym, event)
            else:
                keysym = self.local_dpy.keycode_to_keysym(event.detail, 1)
                return self.makekeyhookevent(keysym, event)
        else: ## Not a typable character.
            keysym = self.local_dpy.keycode_to_keysym(event.detail, 0)
            if self.isshift.match(matchto):
                self.ison["shift"] = self.ison["shift"] + 1
            elif self.iscaps.match(matchto):
                if self.ison["caps"] == False:
                    self.ison["shift"] = self.ison["shift"] + 1
                    self.ison["caps"] = True
                if self.ison["caps"] == True:
                    self.ison["shift"] = self.ison["shift"] - 1
                    self.ison["caps"] = False
            return self.makekeyhookevent(keysym, event)
    
    def keyreleaseevent(self, event):
        if self.shiftablechar.match(self.lookup_keysym(self.local_dpy.keycode_to_keysym(event.detail, 0))):
            if self.ison["shift"] == False:
                keysym = self.local_dpy.keycode_to_keysym(event.detail, 0)
            else:
                keysym = self.local_dpy.keycode_to_keysym(event.detail, 1)
        else:
            keysym = self.local_dpy.keycode_to_keysym(event.detail, 0)
        matchto = self.lookup_keysym(keysym)
        if self.isshift.match(matchto):
            self.ison["shift"] = self.ison["shift"] - 1
        return self.makekeyhookevent(keysym, event)

    # need the following because XK.keysym_to_string() only does printable chars
    # rather than being the correct inverse of XK.string_to_keysym()
    def lookup_keysym(self, keysym):
        for name in dir(XK):
            if name.startswith("XK_") and getattr(XK, name) == keysym:
                return name.lstrip("XK_")
        return "[%d]" % keysym

    def asciivalue(self, keysym):
        asciinum = XK.string_to_keysym(self.lookup_keysym(keysym))
        if asciinum < 256:
            return asciinum
        else:
            return 0
    
    def makekeyhookevent(self, keysym, event):
        if event.type == X.KeyPress:
            MessageName = "key down"
        elif event.type == X.KeyRelease:
            MessageName = "key up"
        return pyxhookkeyevent(self.lookup_keysym(keysym), self.asciivalue(keysym), MessageName)
    
class pyxhookkeyevent:
    """This is the class that is returned with each key event.f
    It simply creates the variables below in the class.
    
    Key = The key pressed, shifted to the correct caps value.
    Ascii = An ascii representation of the key. It returns 0 if the ascii value is not between 31 and 256.
    MessageName = "key down", "key up".
    """
    
    def __init__(self, Key, Ascii, MessageName):
        self.Key = Key
        self.Ascii = Ascii
        self.MessageName = MessageName
    
    def __str__(self):
        return "\nKey Pressed: " + str(self.Key) + "\nAscii Value: " + str(self.Ascii) + "\nMessageName: " + str(self.MessageName) + "\n"

class InterfaceKeyboard(HookManager):
    def __init__(self):
        HookManager.__init__(self)
        self.stack=()
        
        self.KeyDown = self.keyDownCallback
        self.KeyUp = self.keyUpCallback 
        
        self.start()
        
    def keyDownCallback(self, event):
        self.stack = self.stack + (event,)
        self.printevent(event)
        
    def keyUpCallback(self, event):
        self.stack = self.stack + (event,) 
        self.printevent(event)

    def cleanStack(self):
        self.stack = () 

#######################################################################
#########################END CLASS DEF#################################
#######################################################################
    
if __name__ == '__main__':
    interface = InterfaceKeyboard()
