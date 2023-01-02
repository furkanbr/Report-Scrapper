import classes
import os
from pdf2image import convert_from_path, exceptions
import pandas as pd
from PIL import Image, ImageFilter

Image.MAX_IMAGE_PIXELS = 933120000

# Getting all reports from Input Directory.
# This will give us all files in input directory as a list object that we can iterate over it.
input_files = os.listdir('./input')


# Creating all objects in Classes, we will work over all this.
name = classes.Name()
id_number = classes.ID()
date = classes.Date()
date_time = classes.Time()
hr = classes.HR()
ven_ect = classes.VenECT()
hr_var = classes.HRVar()
st_seg_an = classes.STSegAn()
sup_ect = classes.SupEct()
pauses = classes.Pauses()
conclusions = classes.Conclusions()

output_dataframe = pd.DataFrame()

# Creating for loop to iterate over all reports in dictionary and giving cropped report parts as input to all objects.
for report in input_files:
    # Creating image file from first page of report pdf.
    print(report)
    try:
        report_image = convert_from_path(f'./input/{report}', last_page=1, grayscale=True, size=12000)[0]
        data_row = {
            "FileName": report,
            "Name": name.work(report_image),
            "ID": id_number.work(report_image),
            "Date": date.work(report_image),
            "Time": date_time.work(report_image),
            **(hr.work(report_image)),
            **(ven_ect.work(report_image)),
            **(hr_var.work(report_image)),
            **(st_seg_an.work(report_image)),
            **(sup_ect.work(report_image)),
            **(pauses.work(report_image)),
            **(conclusions.work(report_image))
        }

        df_dictionary = pd.DataFrame([data_row])
        print(df_dictionary)
        output_dataframe = pd.concat([output_dataframe, df_dictionary], ignore_index=True)
    except exceptions.PDFPageCountError:
        pass
print(output_dataframe.head(10))
print(output_dataframe.shape)
output_dataframe.to_csv("output.csv")
