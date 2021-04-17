# CLSID.list reducer for Juicy Potato
## INFO
This is a very basic script to reduce the CLSID.list contents provided by [ohpe with the Juicy Potato](https://github.com/ohpe/juicy-potato) exploit.

The lists we get usually have 300-500 CLSIDs and this could take quite a while. 

Since it isn't necessary to go through the whole list to find a usable CLSID for your privilege escalation activities, this script will choose every n<sup>th</sup> CLSID in the list and write it to a new file. 

It's a pretty "dumb" script, frankly. But it's saved me a lot of time.

## USAGE
<pre>
Usage: python reducer.py reduction-factor [input file] [output file]

Positional argument:
        reduction factor - The integer by which to reduce the list

Optional arguments:
        [input file] : Default is CLSID.list
        [output file] : Default is CLSID.list.new
