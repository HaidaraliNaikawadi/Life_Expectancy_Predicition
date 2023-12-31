import numpy as np
import pickle
import json
import config

class Life_Expectancy():
    def __init__(self,Year,Status,Adult_Mortality,infant_deaths,Alcohol, 
                 percentage_expenditure,Hepatitis_B,Measles,BMI,under_five_deaths,Polio,Total_expenditure,
                Diphtheria,HIV_AIDS,GDP,Population,thinness__1_19_years,thinness_5_9_years,
                Income_composition_of_resources,Schooling):
        self.Year=Year
        self.Status=Status
        self.Adult_Mortality=Adult_Mortality
        self.infant_deaths=infant_deaths
        self.Alcohol=Alcohol
        self.percentage_expenditure=percentage_expenditure
        self.Hepatitis_B=Hepatitis_B
        self.Measles=Measles
        self.BMI=BMI
        self.under_five_deaths=under_five_deaths
        self.Polio=Polio
        self.Total_expenditure=Total_expenditure
        self.Diphtheria=Diphtheria
        self.HIV_AIDS=HIV_AIDS
        self.GDP=GDP
        self.Population=Population
        self.thinness__1_19_years=thinness__1_19_years
        self.thinness_5_9_years=thinness_5_9_years
        self.Income_composition_of_resources=Income_composition_of_resources
        self.Schooling=Schooling

    def load_data(self):
        with open(config.json_file_path,'r') as f:
            self.json_data=json.load(f)

        with open(config.model_file_path,'rb') as f:
            self.model=pickle.load(f)

    def pred_expectancy(self):
        self.load_data()
        encoded_status=self.json_data['Status'][self.Status]
        test_array=np.array([self.Year, encoded_status, self.Adult_Mortality, self.infant_deaths, self.Alcohol, 
                             self.percentage_expenditure, self.Hepatitis_B, self.Measles, self.BMI, 
                             self.under_five_deaths, self.Polio, self.Total_expenditure, self.Diphtheria,
                            self.HIV_AIDS, self.GDP, self.Population, self.thinness__1_19_years, 
                            self.thinness_5_9_years, self.Income_composition_of_resources, self.Schooling],ndmin=2)
        
        pred_expectancy=np.around(self.model.predict(test_array),2)
        return pred_expectancy[0]

        