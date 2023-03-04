from time import sleep





class DataFactory():
    def __init__(self):
        self.mock_data = {"cpu": 0.1, "memory": 0.2, "disk": 0.3, "network": 0.4}
        self.collection_progress = []


    def collect_data_framework(self):
               
        progress_level = 0
        
        for k,v in self.mock_data.items():
            print(k)
            progress_level += 100/len(self.mock_data) 
            self.collection_progress.append([k,progress_level])
            #sleep(2)
        return self.collection_progress

