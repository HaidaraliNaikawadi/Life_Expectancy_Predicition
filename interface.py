from flask import Flask,request,jsonify,render_template
import config
from utils import Life_Expectancy

app=Flask(__name__)

@app.route('/life_expectancy')

def home():
    return render_template('Life_Expectancy.html')
    #return jsonify({'Result':'Successful'})

@app.route('/predict_expectancy',methods=['GET','POST'])
def life_expectancy():
    if request.method=='GET':
        data=request.args.get
        Country=data('Country')
        Year=float(data('Year'))
        Status=data('Status')
        Adult_Mortality=float(data('Adult_Mortality'))
        infant_deaths=float(data('infant_deaths'))
        Alcohol=float(data('Alcohol'))
        percentage_expenditure=float(data('percentage_expenditure'))
        Hepatitis_B=float(data('Hepatitis_B'))
        Measles=float(data('Measles'))
        BMI=float(data('BMI'))
        under_five_deaths=float(data('under_five_deaths'))
        Polio=float(data(Polio))
        Total_expenditure=float(data('Total_expenditure'))
        Diphtheria=float(data('Diphtheria'))
        HIV_AIDS=float(data('HIV_AIDS'))
        GDP=float(data('GDP'))
        Population=float(data('Population'))
        thinness__1_19_years=float(data('thinness__1_19_years'))
        thinness_5_9_years=float(data('thinness_5_9_years'))
        Income_composition_of_resources=float(data('Income_composition_of_resources'))
        Schooling=float(data('Schooling'))

        obj=Life_Expectancy(Year,Status,Adult_Mortality,infant_deaths,Alcohol, 
                 percentage_expenditure,Hepatitis_B,Measles,BMI,under_five_deaths,Polio,Total_expenditure,
                Diphtheria,HIV_AIDS,GDP,Population,thinness__1_19_years,thinness_5_9_years,
                Income_composition_of_resources,Schooling)
        
        pred_life=obj.pred_expectancy()
        return render_template('Life_Expectancy.html',prediction=pred_life)
        #return jsonify({'Result':f'Life Expectance is {pred_life}'})

    elif request.method=='POST':
        data=request.form
        Country=data['Country']
        Year=float(data['Year'])
        Status=data['Status']
        Adult_Mortality=float(data['Adult_Mortality'])
        infant_deaths=float(data['infant_deaths'])
        Alcohol=float(data['Alcohol'])
        percentage_expenditure=float(data['percentage_expenditure'])
        Hepatitis_B=float(data['Hepatitis_B'])
        Measles=float(data['Measles'])
        BMI=float(data['BMI'])
        under_five_deaths=float(data['under_five_deaths'])
        Polio=float(data['Polio'])
        Total_expenditure=float(data['Total_expenditure'])
        Diphtheria=float(data['Diphtheria'])
        HIV_AIDS=float(data['HIV_AIDS'])
        GDP=float(data['GDP'])
        Population=float(data['Population'])
        thinness__1_19_years=float(data['thinness__1_19_years'])
        thinness_5_9_years=float(data['thinness_5_9_years'])
        Income_composition_of_resources=float(data['Income_composition_of_resources'])
        Schooling=float(data['Schooling'])

        obj=Life_Expectancy(Year,Status,Adult_Mortality,infant_deaths,Alcohol, 
                 percentage_expenditure,Hepatitis_B,Measles,BMI,under_five_deaths,Polio,Total_expenditure,
                Diphtheria,HIV_AIDS,GDP,Population,thinness__1_19_years,thinness_5_9_years,
                Income_composition_of_resources,Schooling)
        
        pred_life=obj.pred_expectancy()
        return render_template('Life_Expectancy.html',prediction=pred_life)
        #return jsonify({'Result':f'Life Expectance is {pred_life}'})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)

