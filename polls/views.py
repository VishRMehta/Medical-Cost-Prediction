from django.shortcuts import render, redirect
import pandas as pd
import pickle

def index_func(request):
    res = None  # Initialize response variable
    if request.method == 'POST':
        name = request.POST.get('name')
        age = float(request.POST.get('age'))
        gender = int(request.POST.get('sex'))
        bmi = float(request.POST.get('bmi'))
        child = int(request.POST.get('child'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))

        if name:  # Check if name is not empty
            # Create a dataframe with user input
            df = pd.DataFrame({'age': [age], 'sex': [gender], 'bmi': [bmi],
                               'children': [child], 'smoker': [smoker], 'region': [region]})

            # Load the model and make prediction
            filename1 = 'MedicalCost.pickle'
            loaded_model = pickle.load(open(filename1, 'rb'))
            res = loaded_model.predict(df)
            print("Prediction result:", res)

        else:
            return redirect('homepage')  # Redirect if name is empty
    else:
        pass

    return render(request, "index.html", {'response': res})
