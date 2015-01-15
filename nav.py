



import re

def get_url(line):

    rawstr = r"""\((.*)\)"""
    
    # method 1: using a compile object
    compile_obj = re.compile(rawstr)
    match_obj = compile_obj.search(line)

    # method 2: using search function (w/ external flags)
    #match_obj = re.search(rawstr, line)

    # method 3: using search function (w/ embedded flags)
    #match_obj = re.search(embedded_rawstr, line)

    # Retrieve group(s) from match_obj
    
    if match_obj != None:
        all_groups = match_obj.groups()

        # Retrieve group(s) by index
        url = match_obj.group(1)
        
        return url
        
    else:
        
        return None

def main():
    
    url_array = []
    
    with open("README.md", "r") as fh:
        
        md = fh.read()
        
        lines =  md.split("\n")
        
        for line in lines:
            
            url = get_url(line)
            
            if url != None:

                url_array.append(url)
                
    i = 0
    last = len(url_array)
    for url in url_array:
        i = i +1
        print(i, last, url)
            
            
if __name__ == "__main__":

    main()