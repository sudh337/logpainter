import re


def logParserIP(line):
    try:
        ip = re.findall('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', line)[0]
        return ip
    except:
        return None


def logParserPort(line):
    try:
        port_no = re.findall('DPT=(.+) WINDOW', line)[0]
        return port_no
    except IndexError:
        pass
    try:
        port_no = re.findall('DPT=(.+) LEN', line)[0]
        return port_no
    except IndexError:
        return None


def logParserDT(line):
    try:
        dt = re.findall('(.+)dlinkrouter', line)[0]
        return dt
    except:
        return None


def logParserProtocol(line):
    try:
        protocol = re.findall('PROTO=(\S+)', line)[0]
        return protocol
    except:
        return None
