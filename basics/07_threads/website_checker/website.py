
class Websites:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_list = [] # lista słowników
        self.report_list = []
        self.index = 0
        self.load_file(file_name)

    def load_file(self, file_name):
        fh = open(file_name, "r", encoding="utf-8")
        data_list = fh.readlines()

        for v in data_list:
            v = "https://" + v.strip()
            data = {"website" : v, "status_code" : -1}
            self.file_list.append(data)
            data["index"] = len(self.file_list) - 1
            # print(data)

    def get_next_website_to_check(self):
        if self.index >= len(self.file_list):
            return None
        data = self.file_list[self.index]
        self.index += 1
        return data

    def put_website_data(self, data):
        if "index" in data and "website" in data and "status_code" in data:
            self.report_list.append(data)
        else:
            print("Bad keys in report " + str(data))

    def save_report(self):
        fh = open("report.txt", "w")
        for el in self.report_list:
            fh.write(str(el["website"]) + " - " + str(el) + "\n")
        fh.close()