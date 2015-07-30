"""
##################################################################
launch FTP putfile with a reusable form GUI class;
see getfilegui for more
##################################################################
"""

from tkinter import mainloop
import putfile
import getfilegui


class FtpPutfileForm(getfilegui.FtpForm):
    title = "FtpPutfileGui"
    mode = "Upload"

    def do_transfer(self, filename, servername, remotedir, userinfo):
        putfile.putfile(
            filename, servername, remotedir, userinfo, verbose=False)

if __name__ == "__main__":
    FtpPutfileForm()
    mainloop()
