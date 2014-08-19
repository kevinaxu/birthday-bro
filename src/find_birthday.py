# Given a name to search, find the birthday if available 
import argparse, re, datetime
import sys 

def main(): 

    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()

	# Get all files from the yale-soource folder 
    src_file = ["/Users/Kevin/Dev/birthday-bro/data/yale-fb-class-of-2015.html", 
                "/Users/Kevin/Dev/birthday-bro/data/yale-fb-class-of-2016.html"]

    for s_file in src_file: 
        birthday = search_file(args.name, s_file)
        if birthday: 
            print birthday
            break 

def search_file(name, src_file): 
    with file(src_file) as f:						    # Get the contents of the src file
        source = f.read()

    name_parts = name.split()						    # Construct formatted name "last, first"
    name = name_parts[1] + ", " + name_parts[0]

    match_begin = re.search(name, source)			                    # Search for the formatted name 
    if match_begin is None: 
        print "Name not found" 
        return False 

    student_delimiter = "<div class='student_name'>"
    match_end = re.search(student_delimiter, source[match_begin.start():])	    # Narrow down the search string
    if match_end is None: 
        print "No match: end of student div"				    # Will only happen if you search the LAST person
        return False 

    search_str = source[match_begin.start(): match_begin.start() + match_end.start()]

    bday_begin = re.search("<br>[A-Za-z0-9 ]*(</div>){3}", search_str)		# regex: '<br>[birthday]</div></div></div>'

    search_str = search_str[bday_begin.start() + len("<br>"):]				# Reset string to begining of birthday

    bday_end = re.search("<", search_str)
    birthday = search_str[:bday_end.start()]					    # Cut off irrelevant substring from birthday
    
    try: 
        bday_date = datetime.datetime.strptime(birthday, "%b %d")			# Specify format of source code bday (Ex. 'Mar 4')
        birthday = datetime.datetime.strftime(bday_date, "%B, %d")		    # Convert to new format (Ex. 'March, 4')
    except ValueError: 
        print "No birthday specified!" 
        return False 

    return birthday 

if __name__=="__main__":
    main()
