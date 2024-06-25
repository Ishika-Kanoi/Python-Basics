# -*- coding: utf-8 -*-
"""
Here we will be importing the module we created in mymodule

we can see that my_func()
which was created in MyModule can now be called
and returns a message as well. 

"""
#import MyModule
#from MyModule import my_func

#my_func()

from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import my_sub_script

some_main_script.report_main()

my_sub_script.sub_report()

