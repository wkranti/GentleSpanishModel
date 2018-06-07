import argparse
import sys
import json
import csv

def main(argv):
#Standard argument Parser
   parser = argparse.ArgumentParser(description='Converting CSV to JSON')

   parser.add_argument('-i','--csvfile', type=str, help='Input csv file')
   parser.add_argument('-o','--output', type=str ,help='Output JSON file')

   args = parser.parse_args()
   input_file = args.csvfile
   output = args.output
   csv_read( input_file , output )
#Reading CSV file
def csv_read(file , output ):
        csv_rows = []
        with open( file ,"rU" ) as fr:
            reader = csv.DictReader(fr)
            title = reader.fieldnames

            for row in reader:

                csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
            json_writer(csv_rows , output )

#Writting JSON files
def json_writer(data , filejson ):
        with open(filejson, "w") as fw:

                fw.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))


if __name__=='__main__':
    main(sys.argv[1:])
