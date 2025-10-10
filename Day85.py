import argparse
import requests

# def download_file(url, name): 
#   if name is None:
#     name = url.split('/')[-1]



# #---------------Code to Download File---------------


#   with requests.get(url, stream=True) as r:
#       r.raise_for_status()
#       with open(name, 'wb') as f:
#           for chunk in r.iter_content(chunk_size=8192): 
#               f.write(chunk)
#   return name
# #---------------------------------------------------



# #Initialize Argparser
# parser = argparse.ArgumentParser()

# #Take Url of file to download
# parser.add_argument("url", help="Url of the file to download")

# #Take Name of file to save which is of type Str and Default is None
# parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)

# # Parse the arguments
# args = parser.parse_args()

# # Use the arguments in your code
# download_file(args.url, args.output)


def capitalizeYourName(name):
    print(f"Your Name is {name.upper()}")


parser = argparse.ArgumentParser()
parser.add_argument("name" , help="Enter Your Name")
args = parser.parse_args()
capitalizeYourName(args.name)

#Run Like python >> Day85.py binod << in powershell
#Output : Your Name is BINOD

