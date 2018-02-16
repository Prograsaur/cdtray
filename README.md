# cdtray
Tiny CD-ROM tray manipulation library (based on ctypes)

    open_cd(drive=None)     - Open CD-ROM tray. <drive> -- Drive letter if you have more than one
    close_cd(drive=None)    - Close CD-ROM tray. <drive> -- Drive letter if you have more than one
    cd_has_disk(drive=None) - Returns True if CD-ROM drive has a disk inserted
    wait_for_disk(drive=None, timeout = 1) - Waits for user to insert the disk

Usage example:

    from cdtray import *
    
    open_cd('D')
    print('Please insert the disk into drive D')
    wait_for_disk('D')
    print('Thank you')
