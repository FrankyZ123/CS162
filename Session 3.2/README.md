## Polymorphism


## Questions:
In this seminar, *not* all questions need to be answered. Question 1 *must* be
answered by everyone, but only one of questions 2 and 3 need to be answered.

Find out which question to answer by running
the following:
```bash
$ python3 utils/personal_exercises.py
```

Or try out the tkinter interface:
```bash
$ python3 tk_personal_exercise.py
```

Once you've entered your email address, you will find out whether to answer
question 2 or question 3 for this seminar.

### 1. A base object
Python provides certain functionality to all classes.


At the REPL, typing `type(x)` will show what type of variable `x` is, while `dir(x)` will reveal all the methods that x has.  Investigate the default behavior t.  Examine the behavior that python gives a using the following few lines of code:

```python
class BlankClass(object):
    '''This is a Blank class for CS162.'''
    pass

t = BlankClass()

class ClassWithAttr(object):
    x1 = 1
    x2 = 2

my_attr = ClassWithAttr()
my_attr.x3 = 3
```

Now find out about the following methods (answers):
 1. help(t)

```bash
Help on BlankClass in module __main__ object:

class BlankClass(builtins.object)
 |  This is a Blank class for CS162.
 |  
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 #list of attributes with structure
```

 2. type(t)

```bash
<class '__main__.BlankClass'> #type of object
```

 3. dir(t)

```bash
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__'] #object attributes
```

 4. hash(t)

```bash
284374193 #access to location on disk
```

 5. id(t)

```bash
4549987088 #location on disk
```

 6. hasattr(my_attr,'x3')

```bash
True #test if object has 'x3' in it
```

 7. getattr(my_attr,'x3')

```bash
3 #get value of attribute – returns what is stored at the python pointer
```

 8. delattr(my_attr,'x3')

```bash
#deletes attr
```

 9. vars(my_attr)

```bash
{} #no more vars :(
```

10. bool(t)

```bash
True #pointer is not empty, points to object (i.e. Null is not passed)
```

*Come to class able to give clear explanations of what is going on in each of
the above methods, and when one might use them.*

### 3. Graphics in Python
Most graphics in python is done using the bundled Tkinter package (https://docs.python.org/3.5/library/tkinter.html).  

Look at the source code for Tkinter here:
https://github.com/python/cpython/blob/3.5/Lib/tkinter/__init__.py
This is a really long file, so clearly you are not expected to
read every line.  But being able to identify the major classes from a large
file is very useful when starting to work on an existing project.

1. Build up a list of all the classes defined in the tkinter library, and all
the parent classes that it inherits from.

```text
Classname: {Classes Inherited From}
Event: {}
Variable: {}
StringVar: {Variable}
IntVar: {Variable}
DoubleVar: {Variable}
BooleanVar: {Variable}
Misc: {}
CallWrapper: {}
XView: {}
YView: {}
Wm: {}
Tk: {Misc, Wm}
Pack: {}
Place: {}
Grid: {}
BaseWidget: {Misc}
Widget: {BaseWidget, Pack, Place, Grid}
Toplevel: {BaseWidget, Wm}
Button: {Widget}
Canvas: {Widget, XView, YView}
Checkbutton: {Widget}
Entry: {Widget, XView}
Frame: {Widget}
Label: {Widget}
Listbox: {Widget, XView, YView}
Menu: {Widget}
Menubutton: {Widget}
Message: {Widget}
Radiobutton: {Widget}
Scale: {Widget}
Scrollbar: {Widget}
Text: {Widget, XView, YView}
_setit: {}
OptionMenu: {Menubutton}
Image: {}
PhotoImage: {Image}
BitmapImage: {Image}
Spinbox: {Widget, XView}
LabelFrame: {Widget}
PanedWindow: {Widget}
```

2. Now choose a class that inherits from widget and list all the methods that
one can call on that widget.

```text
STANDARD OPTIONS
    activebackground, activeforeground, anchor,
    background, bitmap, borderwidth, cursor,
    disabledforeground, font, foreground
    highlightbackground, highlightcolor,
    highlightthickness, image, justify,
    padx, pady, relief, repeatdelay,
    repeatinterval, takefocus, text,
    textvariable, underline, wraplength
```

3. Find a simple online tutorial on tkinter and build a simple graphical user
interface.  How much of the complexity of the library can be hidden from an
enduser?

```bash
cd "Session 3.2" && python3 frontend.py
```

*Come to class with your example code and be able to explain both the design behind the Tkinter library and how polymorphism helps build a flexible graphics library.*
