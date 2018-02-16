#!/usr/bin/env python
#-----------------------------------------------------------------------------
# Author: Prograsaur (c) 2018
#-----------------------------------------------------------------------------

'''
Utilities for the CD-ROM drive tray manipulation
'''

#region Imports
import sys
import ctypes
from time import sleep
from ctypes.wintypes import UINT, DWORD
#endregion Imports

#region Utils
_winmm = ctypes.windll.WINMM

def mciExecute(cmd):
    result_buf = ctypes.create_unicode_buffer(256)
    res = _winmm.mciSendStringW(cmd, result_buf, ctypes.sizeof(result_buf), None)
    return res, result_buf.value
#endregion Utils

#region Library
#-----------------------------------------------------------------------------
def set_cd_drive(drive=None):
    if not drive: return 'cdaudio'
    mciExecute('open {0}: type cdaudio alias cd_{0}'.format(drive))
    return 'cd_' + drive

def cd_drive(do_open, drive=None):
    '''
    Open or close CD-ROM tray.
    do_open -- Pass True - to open the tray and False to close it
    drive   -- Drive letter if you have more then one drive
    '''
    drive = set_cd_drive(drive)
    cmd = 'set {0} door {1} wait'.format(drive, 'open' if do_open else 'closed')
    mciExecute(cmd)

def open_cd(drive=None):
    '''
    Open CD-ROM tray
    drive -- Drive letter if you have more than one
    '''
    cd_drive(True, drive)

def close_cd(drive=None):
    '''
    Close CD-ROM tray
    drive -- Drive letter if you have more than one
    '''
    cd_drive(False, drive)

def cd_has_disk(drive=None):
    '''
    Returns True if CD-ROM drive has a disk inserted
    drive -- Drive letter if you have more than one
    '''
    drive = set_cd_drive(drive)
    return mciExecute('status {0} media present wait'.format(drive))[1] == 'true'

def wait_for_disk(drive=None, timeout = 1):
    '''
    Waits for user to insert the disk
    drive -- Drive letter if you have more than one
    '''
    while not cd_has_disk(drive): sleep(timeout)
#endregion Library

#region Tests
def _test():
    print('This is a python library - not a standalone application')
    print('Starting self test...')
    open_cd()
    print('CD tray should be open now')
    sleep(3)
    close_cd()
    print('CD tray should be closed now')
    return -1
#endregion Tests

#--- Main --------------------------------------------------------------------
if __name__ == '__main__':
    sys.exit(_test())
