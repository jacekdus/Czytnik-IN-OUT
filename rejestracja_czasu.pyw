import csv
import time
import datetime
import os

# ----- REJESTRATOR -----
def rejestrator():
    main_path = "C:\\_CZAS_PRACY\\" + time.strftime("%Y-%m") + "\\"

    if(not os.path.isdir(main_path)):
        os.makedirs(main_path)

    file_name = main_path + str(datetime.date.today()) + ".csv"

    if(not os.path.isfile(file_name)):
        hours = time.localtime().tm_hour
        minutes = time.localtime().tm_min
        seconds = time.localtime().tm_sec
        open_time = ['{:0>2}:{:0>2}:{:0>2}'.format(hours, minutes, seconds)]
    else:
        try:
            with open(file_name, 'r', newline='') as csvfile:
                csvReader = csv.reader(csvfile, delimiter=';')
                open_time = csvReader.__next__()
        except:
            print("Error. Please close {}".format(file_name))

    while True:
        time.sleep(1)
        try:
            with open(file_name, 'w', newline='') as csvfile:
                csvWriter = csv.writer(csvfile, delimiter=';')
                hours = time.localtime().tm_hour
                minutes = time.localtime().tm_min
                seconds = time.localtime().tm_sec
                csvWriter.writerow(open_time)
                csvWriter.writerow(['{:0>2}:{:0>2}:{:0>2}'.format(hours, minutes, seconds)])
        except:
            print("Error. Please close {}".format(file_name))

# ----- PODLICZATOR -----
def podliczator():
    try:
        main_path = "C:\\_CZAS_PRACY\\"
        directory_list = os.listdir(main_path)
        for ele in directory_list:
            if '.' in ele:
                directory_list.remove(ele)
        for dir in directory_list:
            summary_file = main_path + dir + "_PODSUMOWANIE.csv"
            files_list = []
            days = []

            if summary_file in directory_list:
                os.remove(summary_file)

            days_list = os.listdir(main_path + dir)

            for file in days_list:
                if file.endswith(".csv"):
                    files_list.append(file)
                    try:
                        with open(main_path + dir + "\\" + file, 'r', newline='') as csvfile:
                            csvReader = csv.reader(csvfile, delimiter=';')
                            day = []
                            day.append(str(file).replace(".csv", ''))
                            day.append(csvReader.__next__()[0])
                            day.append(csvReader.__next__()[0])
                            days.append(day)
                    except:
                        print("Problem occurred")

            with open(summary_file, 'w', newline='') as csvfile:
                csvWriter = csv.writer(csvfile, delimiter=';')
                for data in days:
                    csvWriter.writerow(data)
    except:
        print("Error occurred.")

# ----- WYWOLANIE -----
podliczator()
rejestrator()