# CapacityAssistant
Software was designed and implemented on a raspberry pi 3b+

tl-dr: using capacitive touch, we are able to keep track of interactions with the two pieces of foil.

The folders 'max' and 'People' are shared between both py scripts.

'startcopy.py' keeps track of the amount of times each GPIO value has changed. Using this, we are able to wire two pieces of aluminum foil that connect to both GPIO seperatly. We are then able to keep track of the interactions with the two pieces aluminum foil. One piece of aluminum foil would simulate as walking in where the other would simulate walking out of the building, when stepped on. The max capacity is stored in 'max' and amount of people is stored in 'People'

'welcome.py' is used with CGI and Apache2. This website was hosted on the Raspberry Pi and displayed information on the status. Instead of a single html, we are able to make a static page somewhat dynamic. 'welcome.py' is executed every interval assigned in the script. During every executation, we are able to check 'max' and 'people' to then display and calculate how the html will be created for the instance of the interval.
