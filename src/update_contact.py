# Update an entry in contact_info file 
import argparse, re 

def main(): 
	parser = argparse.ArgumentParser()
	parser.add_argument("name")
	parser.add_argument("-b", help="Modify a person's birthday") 
	parser.add_argument("-n", help="Modify a person's phone number") 
	args = parser.parse_args()

	src_file = "/Users/Kevin/Dev/birthday-bro/data/contact_info.db" 
	with open(src_file) as f: 
		contents = f.readlines() 
		
	f = open(src_file, "w") 

	for line in contents: 
		str_parts = [x.strip(" ") for x in line.split(",")]					# Remove starting whitespace 
		str_parts = [x.rstrip() for x in str_parts]							# Remove trailing whitespace 

		if re.search(args.name, line): 
			if args.n:														# Modify phone number if specified 
				print "Modified phone number for " + args.name \
					+ " from " + str_parts[2] + " to " + args.n 
				str_parts[2] = args.n 
			if args.b:														# Modify birthday if specified 
				print "Modified birthday for " + args.name \
					+ " from " + str_parts[3] + " to " + args.b
				str_parts[3] = args.b 

		str_parts = ", ".join(str_parts)									# Rejoin the string 
		f.write(str_parts + "\n")

	f.close() 


	return True 


if __name__=="__main__": 
    main() 
