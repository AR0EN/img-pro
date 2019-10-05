#############################################################################
##
## Copyright (c) 2019 Le Huy Hoang <lehoang318@gmail.com>
## 
## This file is inherited from PyQt5: pyuic.py.
##
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#############################################################################

import sys
import optparse

from PyQt5 import QtCore

from PyQt5.uic.driver import Driver

class PyUiCompiler:
    Version = "Python User Interface Compiler %s for Qt version %s" % (QtCore.PYQT_VERSION_STR, QtCore.QT_VERSION_STR)
    def __init__(self):
        self.parser = optparse.OptionParser(usage="pyuic5 [options] <ui-file>",
                version=PyUiCompiler.Version)
        self.parser.add_option("-p", "--preview", dest="preview", action="store_true",
                default=False,
                help="show a preview of the UI instead of generating code")
        self.parser.add_option("-o", "--output", dest="output", default="-", metavar="FILE",
                help="write generated code to FILE instead of stdout")
        self.parser.add_option("-x", "--execute", dest="execute", action="store_true",
                default=False,
                help="generate extra code to test and display the class")
        self.parser.add_option("-d", "--debug", dest="debug", action="store_true",
                default=False, help="show debug output")
        self.parser.add_option("-i", "--indent", dest="indent", action="store", type="int",
                default=4, metavar="N",
                help="set indent width to N spaces, tab if N is 0 [default: 4]")
        
        g = optparse.OptionGroup(self.parser, title="Code generation options")
        g.add_option("--import-from", dest="import_from", metavar="PACKAGE",
                help="generate imports in the style 'from PACKAGE import ...'")
        g.add_option("--from-imports", dest="from_imports", action="store_true",
                default=False, help="the equivalent of '--import-from=.'")
        g.add_option("--resource-suffix", dest="resource_suffix", action="store",
                type="string", default="_rc", metavar="SUFFIX",
                help="append SUFFIX to the basename of resource files [default: _rc]")
        self.parser.add_option_group(g)

    def generate(self, argumentList):
        # Format: [<ui file path>, <option 1>, <argument 1>, ...]
        opts, args = self.parser.parse_args(argumentList)

        driver = Driver(opts, args[0])
        exit_status = 1
        
        try:
            exit_status = driver.invoke()
            
        except IOError as e:
            driver.on_IOError(e)
            
        except SyntaxError as e:
            driver.on_SyntaxError(e)
            
        except NoSuchClassError as e:
            driver.on_NoSuchClassError(e)
            
        except NoSuchWidgetError as e:
            driver.on_NoSuchWidgetError(e)
            
        except Exception as e:
            driver.on_Exception(e)
