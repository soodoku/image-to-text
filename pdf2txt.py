#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import signal
import logging
import re
import os
import sys
import optparse
import csv
import fnmatch
import subprocess

# ===========================================================================================================
# Default configuration
JPG_OUTPUT_DIR        = 'jpg'                   # Default Text files output directory
JPG_RESOLUTION_DPI    = 400                     # Default Text files output directory
TEXT_OUTPUT_DIR       = 'text'                  # Default Text files output directory

RESUME_OCR            = False

# :\Program Files\gs\gs9.07\
if os.name == 'nt':
    GS_PROG           = r"path_to_gswin32c.exe"
    TESSERACT_PROG    = r"path_to_tesseract.exe"
else:
    GS_PROG           = '/usr/bin/gs'
    TESSERACT_PROG    = '/usr/bin/tesseract'

# ===========================================================================================================

logger = logging. getLogger ('pdf2txt')
logger. addHandler (logging. StreamHandler ())
logger. setLevel (logging. DEBUG)
        
usage = "Usage: %prog [options] <pdf directory>"
def parse_command_line(argv):
    """Command line options parser
    """
            
    parser = optparse.OptionParser(add_help_option=True, usage=usage)
    
    parser.add_option("-d", "--dpi", action="store", 
                      type="int", dest="dpi", default=JPG_RESOLUTION_DPI,
                      help="JPEG Resolution in DPI (default: {0:d})".format((JPG_RESOLUTION_DPI)))
    parser.add_option("-j", "--jpgdir", action="store", 
                      type="string", dest="jpgdir", default=JPG_OUTPUT_DIR,
                      help="JPEG output directory (default: {0!s})".format((JPG_OUTPUT_DIR)))
    parser.add_option("-t", "--textdir", action="store", 
                      type="string", dest="txtdir", default=TEXT_OUTPUT_DIR,
                      help="Text output directory (default: {0!s})".format((TEXT_OUTPUT_DIR)))
    parser.add_option("-r", "--resume", action="store_true", 
                      dest="resume", default=RESUME_OCR,
                      help="Resume OCR to Text (default: {0!s})".format((RESUME_OCR)))
    return parser.parse_args(argv)
    
def getSize(filename):
    """Returns file size
    """
    try:
        return os.path.getsize(filename)
    except:
        return 0
        
def jpg_to_text(options, filename, rootdir):
    """OCR JPEG files and save as TEXT files
    """
    try:
        relpath = os.path.relpath(filename)
    except:
        relpath = os.path.splitdrive(filename)[1]
    relpath = re.sub('^' + re.escape(options.jpgdir), '', relpath, flags=re.I)
    relpath = re.sub(r'^[\.|\\|\/]*', '', relpath)
    extdir = rootdir + '/' + os.path.dirname(relpath)
    fname = extdir + '/' + os.path.basename(relpath)
    fname = os.path.splitext(fname)[0]
    print("OCR JPG to TEXT: {0!s}".format((filename)))
    try:
        if not os.path.exists(extdir):
            os.makedirs(extdir)
        if getSize(fname + ".txt") == 0 or not options.resume:
            p = subprocess.Popen([TESSERACT_PROG, filename, fname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            return out, err
        else:
            return "Resume, file exist skipped", ""
    except:
        pass
    return "", "ERROR"

def pdf_to_jpg(filename, rootdir, dpi):
    """Convert PDF files to JPEG files
    """
    try:
        relpath = os.path.relpath(filename)
    except:
        relpath = os.path.splitdrive(filename)[1]
    relpath = re.sub(r'^[\.|\\|\/]*', '', relpath)
    extdir = rootdir + '/' + os.path.dirname(relpath)
    fname = extdir + '/' + os.path.basename(relpath)
    fname = os.path.splitext(fname)[0] + '-%d.jpg'
    print("Convert PDF to JPG: {0!s}".format((filename)))
    try:
        if not os.path.exists(extdir):
            os.makedirs(extdir)
        #gswin32c -dNOPAUSE -r150 -sDEVICE=jpeg -dBATCH -sOutputFile=out-%d.jpg
        p = subprocess.Popen([GS_PROG, "-dNOPAUSE", "-r" + str(dpi), "-sDEVICE=jpeg", "-dBATCH", "-sOutputFile=" + fname, filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out, err
    except:
        print("ERROR")
    return None, None
    
def main(options, args):
    """ Main Entry Point
    """
    rootdir = args[1]

    if not options.resume:
        # For each PDF files in folder and sub-folders
        for root, dirnames, filenames in os.walk(rootdir):
          for filename in fnmatch.filter(filenames, '*.pdf'):
              fname = os.path.join(root, filename)
              out, err = pdf_to_jpg(fname, options.jpgdir, options.dpi)
              print out, err
    
    # For each JPG files in folder and sub-folders
    for root, dirnames, filenames in os.walk(options.jpgdir):
      for filename in fnmatch.filter(filenames, '*.jpg'):
          fname = os.path.join(root, filename)
          out, err = jpg_to_text(options, fname, options.txtdir)
          print out, err
    
def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    os._exit(1)
    
if __name__ == "__main__":

    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    signal.signal(signal.SIGINT, signal_handler)
    
    print("{0!s} - r2 (2013/06/15)\n".format((os.path.basename(sys.argv[0]))))
    
    (options, args) = parse_command_line(sys.argv)

    if len(args) < 2:
        print("Please specify root directory of PDF input files (-h/--help for help)")
        sys.exit(-1)
        
    main(options, args)
