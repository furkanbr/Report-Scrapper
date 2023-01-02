import pprint
import numpy
import pytesseract
import re
import numpy as np

# Tesseract image to string method have some configs for text layout on image
# https://stackoverflow.com/questions/44619077/pytesseract-ocr-multiple-config-options


def safe_execute(exception, default, function, *args):
    try:
        return function(*args)
    except exception:
        return default


class Name:
    def __init__(self):
        self.image = None
        pass

    def work(self, image):
        self.image = image
        cropped_image = self.image.crop((245*5, 220*5, 995*5, 257*5))  # (left, upper, right, lower)
        text = pytesseract.image_to_string(cropped_image, lang='tur').strip()
        return text


class ID:
    def __init__(self):
        self.image = None
        pass

    def work(self, image):
        self.image = image
        cropped_image = self.image.crop((1137*5, 220*5, 1687*5, 255*5))  # (left, upper, right, lower)
        text = pytesseract.image_to_string(cropped_image, lang='eng').strip()
        return text


class Date:
    def __init__(self):
        self.image = None
        pass

    def work(self, image):
        self.image = image
        cropped_image = self.image.crop((41*5, 138*5, 331*5, 178*5))  # (left, upper, right, lower)
        text = pytesseract.image_to_string(cropped_image, lang='eng').strip()
        return text


class Time:
    def __init__(self):
        self.image = None
        pass

    def work(self, image):
        self.image = image
        cropped_image = self.image.crop((1394*5, 140*5, 1689*5, 176*5))  # (left, upper, right, lower)
        text = pytesseract.image_to_string(cropped_image, lang='eng', config='--psm 6').strip()
        return text


class HR:
    def __init__(self):
        self.image = None
        pass

    def work(self, image):
        self.image = image
        cropped_image = self.image.crop((25*5, 583*5, 575*5, 826*5))  # (left, upper, right, lower)
        cropped_image.save('out.jpg', 'JPEG')
        text = pytesseract.image_to_string(cropped_image, lang='eng', config='--psm 4')
        text = text.replace("- ", ": ")
        data = re.split(': |\n', text)
        data = list(filter(None, data))
        print(data)
        if len(data) == 16:
            return_data = {
                "Minimum HR-4 Intervals": data[1],
                "Maximum HR-4 Intervals": data[3],
                "Average HR-24 Hours": data[5],
                "Minimum HR-Hourly": data[7],
                "Maximum HR-Hourly": data[9],
                "Analyzed Beats": data[11],
                "Analyzed Minutes": data[13],
                "ECG Monitoring Period": data[15]
            }
        else:
            return_data = {
                "Minimum HR-4 Intervals": np.nan,
                "Maximum HR-4 Intervals": np.nan,
                "Average HR-24 Hours": np.nan,
                "Minimum HR-Hourly": np.nan,
                "Maximum HR-Hourly": np.nan,
                "Analyzed Beats": np.nan,
                "Analyzed Minutes": np.nan,
                "ECG Monitoring Period": np.nan,
            }

        return return_data


class VenECT:
    def __init__(self):
        self.image = None
        pass

    def work(self, image):
        self.image = image
        cropped_image = self.image.crop((582*5, 581*5, 1140*5, 825*5))  # (left, upper, right, lower)
        cropped_image.save('out.jpg', 'JPEG')
        text = pytesseract.image_to_string(cropped_image, lang='eng', config='--psm 6')
        text = text.replace("- ", ": ")
        data = re.split(': |\n', text)
        data = list(filter(None, data))
        print(data)
        if len(data) == 16:
            return_data = {
                "VE Total": data[1],
                "V-Pair Total": data[3],
                "V-Run Total": data[5],
                "Longest V-Run": data[7],
                "Maximum HR V-Run": data[9],
                "Minimum HR V-Run": data[11],
                "VE's per 1000/per Hour": data[13],
                "Ventricular R on T": data[15]
            }
        else:
            return_data = {
                "VE Total": np.nan,
                "V-Pair Total": np.nan,
                "V-Run Total": np.nan,
                "Longest V-Run": np.nan,
                "Maximum HR V-Run": np.nan,
                "Minimum HR V-Run": np.nan,
                "VE's per 1000/per Hour": np.nan,
                "Ventricular R on T": np.nan,
            }
        return return_data


class HRVar:
    def __init__(self):
        self.image = None
        pass

    def work(self, image):
        self.image = image
        cropped_image = self.image.crop((1140*5, 583*5, 1688*5, 825*5))  # (left, upper, right, lower)
        cropped_image.save('out.jpg', 'JPEG')
        text = pytesseract.image_to_string(cropped_image, lang='eng', config='--psm 6')
        text = text.replace("- ", ": ")
        data = re.split(': |\n', text)
        data = list(filter(None, data))
        print(data)
        if len(data) == 16:
            return_data = {
                "SDNN-24 Hour": data[1],
                "SDANN Index": data[3],
                "SDNN Index": data[5],
                "rMSSD": data[7],
                "pNN5O": data[9],
                "Spectral Power-24 Hour": data[11],
                "Min Spectral Power Hour": data[13],
                "Max Spectral Power Hour": data[15]
            }
        else:
            return_data = {
                "SDNN-24 Hour": np.nan,
                "SDANN Index": np.nan,
                "SDNN Index": np.nan,
                "rMSSD": np.nan,
                "pNN5O": np.nan,
                "Spectral Power-24 Hour": np.nan,
                "Min Spectral Power Hour": np.nan,
                "Max Spectral Power Hour": np.nan,
            }
        return return_data


class STSegAn:
    def __init__(self):
        self.image = None
        pass

    def work(self, image):
        self.image = image
        cropped_image = self.image.crop((25*5, 870*5, 577*5, 1123*5))  # (left, upper, right, lower)
        cropped_image.save('out.jpg', 'JPEG')
        text = pytesseract.image_to_string(cropped_image, lang='eng', config='--psm 6')
        text = text.replace("- ", ": ")
        data = re.split(': |\n', text)
        data = list(filter(None, data))
        print(data)
        if len(data) == 14:
            return_data = {
                "Total ST Minutes CH1": data[1],
                "Total ST Minutes CH2": data[3],
                "Total ST Minutes CH3": data[5],
                "Max Abs. ST Depression": data[7],
                "Max Abs. ST Elevation": data[9],
                "Max ST Episode": data[11],
                "Max HR In ST Episode": data[13]
            }
        else:
            return_data = {
                "Total ST Minutes CH1": np.nan,
                "Total ST Minutes CH2": np.nan,
                "Total ST Minutes CH3": np.nan,
                "Max Abs. ST Depression": np.nan,
                "Max Abs. ST Elevation": np.nan,
                "Max ST Episode": np.nan,
                "Max HR In ST Episode": np.nan,
            }
        return return_data


class SupEct:
    def __init__(self):
        self.image = None
        pass

    def work(self, image):
        self.image = image
        cropped_image = self.image.crop((582*5, 872*5, 1133*5, 1127*5))  # (left, upper, right, lower)
        cropped_image.save('out.jpg', 'JPEG')
        text = pytesseract.image_to_string(cropped_image, lang='eng', config='--psm 6')
        text = text.replace("- ", ": ")
        data = re.split(': |\n', text)
        data = list(filter(None, data))
        print(data)
        if len(data) == 16:
            return_data = {
                "SVE Total": data[1],
                "SVE Pair Total": data[3],
                "SV-Run Total": data[5],
                "Longest V-Run": data[7],
                "Maximum HR V-Run": data[9],
                "SVE's per 1000/per hour": data[11],
                "Total Aberrant Beats/Runs": data[13],
                "Atrial Fib/Flutter": data[15]
            }
        else:
            return_data = {
                "SVE Total": np.nan,
                "SVE Pair Total": np.nan,
                "SV-Run Total": np.nan,
                "Longest V-Run": np.nan,
                "Maximum HR V-Run": np.nan,
                "SVE's per 1000/per hour": np.nan,
                "Total Aberrant Beats/Runs": np.nan,
                "Atrial Fib/Flutter": np.nan,
            }
        return return_data


class Pauses:
    def __init__(self):
        self.image = None
        pass

    def work(self, image):
        self.image = image
        cropped_image = self.image.crop((1139*5, 872*5, 1688*5, 1127*5))  # (left, upper, right, lower)
        cropped_image.save('out.jpg', 'JPEG')
        text = pytesseract.image_to_string(cropped_image, lang='eng', config='--psm 6')
        text = text.replace("- ", ": ")
        data = re.split(': |\n', text)
        data = list(filter(None, data))
        print(data)
        if len(data) > 10:
            return_data = {
                "Pauses in Excess of 2.5 sec": data[1],
                "Max Pause": data[3],
                "Max QT": data[6],
                "Max QTc": data[8],
                "Time of Max QT": data[10],
                "BBB": data[11].split(" ")[1]
            }
            return return_data
        else:
            return_data = {
                "Pauses in Excess of 2.5 sec": numpy.nan,
                "Max Pause": numpy.nan,
                "Max QT": numpy.nan,
                "Max QTc": numpy.nan,
                "Time of Max QT": numpy.nan,
                "BBB": numpy.nan,
            }
            return return_data


class Conclusions:
    def __init__(self):
        self.image = None
        self.rhythm_type = None
        self.duration = None
        self.interval_rhythm = None
        self.atrial_run = None
        self.atrial_run_count = None

    def work(self, image):
        self.image = image
        cropped_image = self.image.crop((27*5, 1710*5, 1684*5, 2181*5))  # (left, upper, right, lower)
        text = pytesseract.image_to_string(cropped_image, lang='tur')

        # Finding Rhythm Type
        rhythm_pattern = r"temel\sritm\s([\w\s:]+)(?:\sritim|\sritmi|\solara)"
        rhythm_regex = re.compile(rhythm_pattern)

        rhythm_match = rhythm_regex.search(text)
        if rhythm_match:
            self.rhythm_type = rhythm_match.group(1)
            # self.rhythm_type = self.rhythm_type.split(" ")[:-1]
        else:
            self.rhythm_type = np.nan

        # Finding R-R Interval

        interval_pattern = r"R-R\s(?:ara|aral[ıi][gğ][ıi])\s(\d+)"
        interval_regex = re.compile(interval_pattern)

        interval_match = interval_regex.search(text)
        if interval_match:
            self.duration = interval_match.group(1)
        else:
            self.duration = np.nan

        # Find Interval-Rhythm Pattern

        interval_rhythm_pattern = r"(Aralikli|Aralıklı)\solarak\s([\w\s]+)\sizle"
        interval_rhythm_regex = re.compile(interval_rhythm_pattern)

        interval_rhythm_match = interval_rhythm_regex.search(text)
        if interval_rhythm_match:
            self.interval_rhythm = interval_rhythm_match.group(2)
        else:
            self.interval_rhythm = np.nan

        # Find Atrial-Run Attack

        pattern_izlenmi = r"izlenmi"
        pattern_izlenme = r"izlenme"
        regex_izlenmi = re.compile(pattern_izlenmi)
        regex_izlenme = re.compile(pattern_izlenme)

        for sentence in text.split("."):
            match_izlenmi = regex_izlenmi.search(sentence)
            match_izlenme = regex_izlenme.search(sentence)
            if match_izlenmi:
                self.atrial_run = True
            elif match_izlenme:
                self.atrial_run = False
            else:
                self.atrial_run = np.nan

        # Find Atrial-Run Count

        atrial_run_pattern = r"(\d+)\s?Atrial"
        atrial_run_regex = re.compile(atrial_run_pattern)

        atrial_run_match = atrial_run_regex.search(text)
        if atrial_run_match:
            self.atrial_run_count = atrial_run_match.group(1)
        else:
            self.atrial_run_count = np.nan

        return_data = {
            "Rhythm Type": self.rhythm_type,
            "R-R Interval": self.duration,
            "Interval Rhythm": self.interval_rhythm,
            "Atrial Run": self.atrial_run,
            "Atrial Run Count": self.atrial_run_count
        }

        return return_data





