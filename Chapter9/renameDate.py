import shutil
import os
import re


if __name__ == '__main__':

    # Create a regex that matched files with the American date format
    dataPattern = re.compile(r"""^(.*?)                  # all text before the dataPattern
                ((0|1)?\d)-                              # one or two digits for the month
                ((0|1|2|3)?\d)-                          # one or two digits for the day
                ((19|20)\d\d)                            # four digits for the year
                (.*?)$                                   # all text after the date
                """, re.VERBOSE)

    # TODO:Loop over the files in the working directory
    for amerFilename in os.listdir('.'):
        mo = dataPattern.search(amerFilename)

        if None == mo:
            continue

        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(7)

        # form the european-style filename
        euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + '-' + afterPart

        absWorkingDir = os.path.abspath('.')
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absWorkingDir, euroFilename)

        # rename the files
        print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
        shutil.move(amerFilename, euroFilename)
