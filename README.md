# NmapMostCommonPorts
Print the most common ports used by Nmap default scans.\
Nmap uses the 'nmap-services' file which arrives when you install Nmap, to list the most common ports used in scans. They are chosen by the frequency attribute in that file.\
On a default scan the 1000 most common ports are used. If '-F' flag is used (fast scan), then this number is reduced to 100 (https://nmap.org/book/man-port-specification.html).\
\
![alt text](https://raw.githubusercontent.com/agentzex/NmapMostCommonPorts/master/Capture.PNG)
