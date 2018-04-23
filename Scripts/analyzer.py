
from scapy.all import *
import json
import sys


def main(json_name):
	hostnames = reader(json_name)
	d = {}
	#hostnames = ["www.falundafa.org","www.yahoo.com"]
	for hostname in hostnames:
		d[hostname] = {}
		ans = dns_req(hostname)
		if len(ans)<1:
			d[hostname]["blocked"] = False
			d[hostname]["ipid"] = -1
			d[hostname]["ttl"] = -1
		else:
			d[hostname]["blocked"] = True
			ipid = ans[len(ans)-1][1][IP].id
			ttl = ans[len(ans)-1][1][IP].ttl
			d[hostname]["ttl"] = ttl
			d[hostname]["ipid"] = ipid
		print(d)



def dns_req(url):
	ans,unans = sr(IP(dst="218.62.26.196")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=url)),verbose=0,multi=1,timeout=5)
	return ans

def reader(file_name):
	with open(file_name) as f:
		return json.load(f)

if __name__ == "__main__":
	main()
