#!/usr/bin/env python3
__author__ = 'Administrator'
import os


class Delete(object):
    """Delete Methods For File Objects"""

    def __init__(self, file):
        self.file = file

    def interactive(self):
        """interactive deletion mode"""

        input1 = input('Do you readlly want to delete %s [N]/Y' % self.file)
        if input1.upper():
            print("DELETING: %s" % self.file)
            status = os.remove(self.file)
        else:
            print('Skipping: %s' % self.file)
        return

    def dryrun(self):
        """simulation mode for deletion"""
        print('Dry Run: %s [NOT DELETED]' % self.file)
        return

    def delete(self):
        """Performs a delete on a file, with additional conditions"""

        print("DELETING: %s" % self.file)
        try:
            status = os.remove(self.file)
        except Exception as err:
            print(err)
            return status


if __name__ == "__main__":
    from find_dupes import finddupes
    dupes = finddupes('.')
    for dupe in dupes:
        delete = Delete(dupe)
        # delete.dryrun()
        delete.delete()
        # delete.interactive()
