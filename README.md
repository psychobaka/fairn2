Fair'n<sup>2</sup>
==================
This is a program I'm writing to track finances amongst myself and my housemates.  Could expand it to a website.

Status
------
Framework done.  Working out the software design in the Wiki.  Feel free to check it out!

License
-------
GNU GPL v3 (http://www.gnu.org/licenses/#GPL)

Installation
------------
### Required libraries:
 - peewee
   - https://pypi.python.org/pypi/peewee
 - PyMySQL
   - https://pypi.python.org/pypi/PyMySQL
 - Python 3.5 or equivalent
 - PyMongo 3.1rc0 or equivalent
 - MySQL Server 5.7 or equivalent

### Optional libraries:
 - Sphinx for generating API documentation (untested!).

### Installation procedure:
1. Install required libraries.
2. Use "Forward Engineer..." on "user/default/mysqlmodel.mwb" in MySQL Workbench
   to create databases "fairn2init".
3. Create additional schemas "fairn2qa" (for testing), "fairn2dev" (if you want
   to do dev work), and "fairn2" (production server) using data from
   "fairn2init". I haven't found a great way to do this, but so far a working
   option is to:
   1. Click "Server=>Data Export".
   2. Check the "fairn2init" schema.
   3. Select "Dump Structure and Data" in the combo box under the "Schema
      Objects" selection table.
   4. Export in the script style of your choice.
   5. Click "Server=>Data Import".
   6. In the wizard, load the script you just exported.
   7. For each of the schemas specified above:
      1. Click the "New..." button
      2. Type in the name of the schema you are creating.
      3. Click the "Start Import" button in the bottom right.
      
I don't yet have an update procedure.  Perhaps in the future.  :)  The tricky
part is the autonum IDs don't travel well.  The only idea I have right now is to
edit the exported script and strip out the "id" values from the table
insertions.

Usage
-----

### To run Fair'n<sup>2</sup>:
Lean back in your chair and imagine what this software would be like.  That's
what I do.  ^_~

### To run tests:
Unit tests may run by executing "runtests.py".
