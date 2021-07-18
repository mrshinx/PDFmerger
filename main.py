import PyPDF2
import os

in_folder = 'in/'
out_folder = 'out/'

if not os.path.exists(out_folder):
    os.makedirs(out_folder)
if not os.path.exists(in_folder):
    os.makedirs(in_folder)

merger = PyPDF2.PdfFileMerger()
for pdf in os.listdir(in_folder):
    merger.append(f'{in_folder}{pdf}')

merger.write(f'{out_folder}merged.pdf')
print("done")
