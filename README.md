# NmapMostCommonPorts
Nmap uses the frequency attribute in the 'nmap-services' file which is downloaded when you install Nmap, to list the most common ports which will be used in scans.\
On a default scan the 1000 most common ports are used. If '-F' flag is used (quick scan), then this number is reduced to 100 (https://nmap.org/book/man-port-specification.html).
This tool will print the most common ports used by Nmap scans.\
To launch it just run it with Python3, you can set the number of most common ports to fetch with '-t' flag. For example '-t 1000' will fetch the 1000 most common ports. The default is 100.\
The tool will use the default installation path of 'nmap-services' file on Linux or Windows, but if you want you can also copy and place the file together with this script and use the '-p' flag in order to use the local path instead.

\
\
![alt text](https://raw.githubusercontent.com/agentzex/NmapMostCommonPorts/main/Capture.PNG)
