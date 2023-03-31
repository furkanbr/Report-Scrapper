# PDF Report Processing Script

This script is designed to process a set of PDF reports, extract specific information from them, and store the extracted data in a CSV file. It also moves the processed PDF files to an output folder and appends the first page of each PDF to a new output PDF file. The script uses various custom classes to perform the extraction tasks and relies on external libraries such as pdf2image, PyPDF2, and pandas.

## How the script works

1. Import necessary libraries and modules.
2. Set the maximum number of image pixels to avoid errors when processing large images.
3. Get a list of all PDF files in the input directory.
4. Create an empty PDF object to store the appended first pages of the processed PDFs.
5. Define a function `append_pdf()` that reads a PDF file, extracts the first page, and adds it to the output PDF object.
6. Create instances of custom classes for extracting specific information from the PDFs, such as Name, ID, Date, Time, PaceMaker, HR, VenECT, HRVar, STSegAn, SupEct, Pauses, and Conclusions.
7. Initialize an empty pandas DataFrame to store the extracted data.
8. Iterate over the list of PDF files in the input directory:
   a. Convert the first page of the PDF to an image.
   b. Save the image as a JPEG file.
   c. Extract the required information from the image using the custom class instances.
   d. Create a dictionary containing the extracted data.
   e. Convert the dictionary to a pandas DataFrame and append it to the output DataFrame.
   f. Move the processed PDF file to the output folder and rename it with the extracted ID, Name, and Date.
   g. Call the `append_pdf()` function to append the first page of the processed PDF to the output PDF object.
   h. Calculate the time taken to process the PDF and estimate the remaining time to process all PDFs.
9. Print the first 10 rows of the output DataFrame and its shape.
10. Save the output DataFrame as a CSV file.

## Usage

To use this script, you need to have the required libraries installed and the input PDF files placed in the "input" directory. The script will process the PDFs, extract the required information, and store it in a CSV file named "output.csv". The processed PDF files will be moved to the "output" directory, and the appended first pages will be saved as a new PDF file named "output.pdf".
