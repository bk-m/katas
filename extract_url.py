"""
from codewars.com
"""

# Write a function that when given a URL as a string,
# parses out just the domain name and returns it as a string.
# For example:
# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

import re

def domain_name(url):
    """
    takes a url as string, returns domain name
    """
    return re.search('(.*//)?(www\.)?(.*)(\.[a-z]{2,3})', url).group(3)

def main():
    """
    testing
    """
    print(domain_name("http://www.zombie-bites.com"))
    print(domain_name("http://github.com/carbonfive/raygun"))
    print(domain_name("https://www.cnet.com"))
    print(domain_name("google.com"))

if __name__ == '__main__':
    main()
