#! python3

"""

    QR CODE GENERATOR
    bnhf
    
    v1: 09/06/24
    
"""

import pandas as pd
import segno, argparse, os


# TODO: Generate QR codes from csv file and save to directory
def generate_qr(csv_file, output_dir):
   try:
      df = pd.read_csv(csv_file, header=None)
      
      if len(df.columns) != 1:
      	raise ValueError("Incorrect Format: CSV file must contain exactly one column")
      
      print("\nGenerating QR Codes...\n")
      total_qrs = qr_success = qr_fail = 0
      results = []

      for index, row in df.iterrows():
      	total_qrs += 1
      	
      	data = row[df.columns[0]]
      	img_path = os.path.join(output_dir, f"{data}.png")
      	
      	# check duplicate entries
      	if os.path.exists(img_path):
           status = "FAILED: Duplicate file exists"
      	   qr_fail += 1
      	   results.append({"data": data, "status": status})
      	   print(f"{data} - {status}")
      	   continue
      	
      	try:
           # create qr
      	   qr = segno.make_qr(data)
      	   qr.save(img_path, scale=10)
      	   status = "SUCCESS"
      	   qr_success += 1
      		
      	except Exception as e:
      	   status = "FAILED: Invalid characters"
      	   qr_fail += 1
      	
      	results.append({"data": data, "status": status})
      	print(f"{data} - {status}")
      

      # TODO: Create a csv log file
      log_path = os.path.join(output_dir, "logs.csv")
      results_df = pd.DataFrame(results)
      results_df.to_csv(log_path, index=False)
      
      print(f"\n{total_qrs} entries found")
      print(f"{qr_success} QR codes created successfully")
      print(f"{qr_fail} QR codes failed")
      
   except ValueError as e:
      print(f"\n\t{e}")
      exit(1) 
		
if __name__ == "__main__":
      """
      parser = argparse.ArgumentParser(description="Generate QR codes from a CSV file.")
      parser.add_argument('csv_file', type=str, help='Path to the input CSV file.')
      parser.add_argument('output_dir', type=str, help='Directory to save QR codes.')
      
      args = parser.parse_args()
      
      csv_file = args.csv_file
      output_dir = args.output_dir
      """

      params = sys.argv

      if len(params) > 1:
         csv_file = params[0]
         output_dir = params[1]
         #address = ' '.join(params[1:])
      
      # TODO: Create output directory if it doesn't exist
      if not os.path.exists(output_dir):
          os.makedirs(output_dir)
      
      generate_qr(csv_file, output_dir)

