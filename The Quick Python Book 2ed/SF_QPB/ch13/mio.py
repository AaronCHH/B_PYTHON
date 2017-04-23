"""mio: module, (contains functions CaptureOutput, RestoreOutput, PrintFile, and ClearFile )"""
import sys
_fileObject = None

def CaptureOutput(file="captureFile.txt"):
    """CaptureOutput(file='captureFile.txt'): redirect the standard output to 'file'."""
    global _fileObject
    print "output will be sent to file: %s" % (file)
    print "restore to normal  by calling 'mio.RestoreOutput()'"
    _fileObject= open(file, 'w')
    sys.stdout = _fileObject

def RestoreOutput():
    """RestoreOutput(): restore the standard output back to the default (also closes the capture file)"""
    global _fileObject
    sys.stdout = sys.__stdout__
    _fileObject.close()
    print "standard output has been restored back to normal"

def PrintFile(file="captureFile.txt"):
    """PrintFile(file="captureFile.txt"): print the given file to the standard output"""
    f = open(file,'r')
    print f.read()
    
def ClearFile(file="captureFile.txt"):
    """ClearFile(file="captureFile.txt"): clears the contents of the given file"""
    f = open(file,'w')
    f.close()