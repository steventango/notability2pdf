import os
import shutil
import zipfile

if not os.path.exists("in"):
  os.makedirs("in")
  print('Add *.note files to in/ folder')
if not os.path.exists("out"):
  os.makedirs("out")
if not os.path.exists("temp"):
  os.makedirs("temp")

directory = os.fsencode("in")

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".note"):
         with zipfile.ZipFile(f"in/{filename}","r") as zip_ref:
          directory = f"temp/{filename[slice(-5)].strip()}"
          try:
            zip_ref.extractall(directory)
          except:
            print(f"Failed extracting: {directory}")
            continue

          folder_name = next(os.walk(directory))[1][0]
          print(f'Extracted: {folder_name}')
          pdf_folder_path = f"temp/{folder_name}/{folder_name}/PDFs"
          pdfs = os.listdir(pdf_folder_path)
          if len(pdfs) > 1:
            for (i, pdf) in enumerate(pdfs):
              shutil.move(f"{pdf_folder_path}/{pdf}", f"out/{folder_name} ({i}).pdf")
          else:
            pdf = pdfs[0]
            shutil.move(f"{pdf_folder_path}/{pdf}", f"out/{folder_name}.pdf")

shutil.rmtree("temp")
