import os
import yaml
import requests
import subprocess, sys


# color and other
W  = '\033[0m'
P  = '\033[1;35m'
C  = '\033[1;36m'
R  = '\033[91m'
ht = 'https://'


# domains buy
gd = 'https://domains.google.com/express/search?searchTerm=' #google domains
un = 'https://uniregistry.com/buy-domains/' #uniregistry
god= 'https://id.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=' #godaddy
nc = 'https://www.namecheap.com/domains/registration/results/?domain=' #namecheap
hg = 'https://portal.hostgator.com/domain/purchase/registration/tegalsec/SNAPPY?search=' #hostgator
iw = 'https://iwantmyname.com/?domain=' #iwantmyname
dn = 'https://www.domainesia.com/domain/?domain=' #domainesia


def checker():
    print ("""
 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███╗   ██╗ █████╗ ███╗   ███╗███████╗
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝████╗  ██║██╔══██╗████╗ ████║██╔════╝
██║     ███████║█████╗  ██║     █████╔╝ ██╔██╗ ██║███████║██╔████╔██║█████╗  
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                           </> Tegal1337 </>                                                  
    """)
    user = input("Username: ")
    if user == '':
        exit()
    else:
        with open('websites.yml') as f:
            data = yaml.safe_load(f)
            links = data['sites']

        weblinks = ["{}{}".format(i,user) for i in links]

        for url in weblinks:
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
            if r.status_code == 200:
                print(C+'Unavailable for: '+W+'' + url)
            else:
                print(P+'Available for:   '+W+'' + url)

    with open("tlds.txt", "r") as ifile:
        for line in ifile:
            tld = line.rstrip("\n")

            ns = "nslookup "+user+"."+tld+" | grep -i \"Can't find\""
            nsl = subprocess.run(ns, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            x = user+'.'+tld
            xx = ht+user+'.'+tld

            if nsl.returncode == 0:
                print(P+'Available for:   '+W+''+xx)
                print(R+"             Google Domains: "+W+gd+x)
                # print(R+"             Uniregistry: "+W+un+x)
                # print(R+"             Godaddy: "+W+god+x)
                # print(R+"             Namecheap: "+W+nc+x)
                # print(R+"             Hostgator: "+W+hg+x)
                # print(R+"             Iwantmyname: "+W+iw+x)
                # print(R+"             Domainesia: "+W+dn+x)
            else:
                print(C+'Unavailable for: '+W+''+xx)

def banner():
    try:
        os.system('cls')
        raise ValueError('Error')
    except Exception:
        os.system('clear')
def main():
    checker()

banner()
main()
