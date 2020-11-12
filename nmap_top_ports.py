import argparse
import collections
import os


def pretty_print(ports, port_type, number_of_ports_to_print):
    print('*' * 20 + port_type + '*' * 20)
    print("{0:^20}{1:^20}{2:^20}".format("Protocol", "Port Number", "Frequency"))
    counter = 0
    for k, v in ports.items():
        for port in v:
            print("{0:^20}{1:^20}{2:^20}".format(port["port_name"], port["port_number"], port["port_frequency"]))
            if counter >= number_of_ports_to_print:
                return
            counter += 1


def main(number_of_ports_to_print, use_local_path):

    if use_local_path:
        nmap_services_path = r"nmap-services"
    else:
        if os.name == "nt":
            nmap_services_path = r"C:\Program Files (x86)\Nmap\nmap-services"
        else:
            nmap_services_path = r"/usr/share/nmap/nmap-services"

    tcp_ports = {}
    udp_ports = {}

    with open(nmap_services_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith("#"):
            continue
        line = line.strip()
        port_line = line.split("\t")
        port_name = port_line[0]
        port_number = port_line[1]
        port_frequency = port_line[2]
        port_type = port_number.split('/')[1]
        if port_type == "tcp":
            if port_frequency in tcp_ports:
                tcp_ports[port_frequency].append({"port_name": port_name, "port_number": port_number, "port_frequency": port_frequency})
            else:
                tcp_ports[port_frequency] = []
                tcp_ports[port_frequency].append({"port_name": port_name, "port_number": port_number, "port_frequency": port_frequency})
        elif port_type == "udp":
            if port_frequency in udp_ports:
                udp_ports[port_frequency].append({"port_name": port_name, "port_number": port_number, "port_frequency": port_frequency})
            else:
                udp_ports[port_frequency] = []
                udp_ports[port_frequency].append({"port_name": port_name, "port_number": port_number, "port_frequency": port_frequency})

    tcp_ports = collections.OrderedDict(sorted(tcp_ports.items(), reverse=True))
    udp_ports = collections.OrderedDict(sorted(udp_ports.items(), reverse=True))
    pretty_print(tcp_ports, "TCP", number_of_ports_to_print)
    pretty_print(udp_ports, "UDP", number_of_ports_to_print)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-localpath", "-p", default=False, help="If set, nmap-services file should be in the same path as this script. Otherwise using the default installation path")
    parser.add_argument("-top", "-t", default="100", help="The number of most common ports to print. For example '-t 1000' to print the 1000 most common ports. Default is 100")
    args = parser.parse_args()

    number_of_ports_to_print = int(args.top)
    use_local_path = args.localpath
    main(number_of_ports_to_print, use_local_path)
