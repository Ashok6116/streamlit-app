import streamlit as st
import pickle as pkl
import numpy as np

#st.title("Car Prediction")
a=pkl.load(open('opes.pkl','rb'))
with st.sidebar:
    st.sidebar.title("Prediction")

    with st.form("car_input_form"):
        st.image("imgs/img7.png")
        inputs = []

        #Kms Driven
        #min=101
        #max=5500000
        sl1 = st.slider("Kms Driven",min_value=100,max_value=2000)
        val3=sl1
        inputs.append(val3)

        #year of manifacture
        #min-1985
        #max-2023
        year=[2015, 2018, 2014, 2020, 2017, 2021, 2019, 2022, 2016, 2011, 2009,
        2013, 2010, 2008, 2006, 2012, 2005, 2007, 2023, 1998, 2004, 2003,
        2001, 2002, 2000, 1985, 1997, 1999]
        sb = st.selectbox('Model Year', year) 
        val4=sb
        inputs.append(val4)

        #mileage
        #min-7.08
        #max-356.09
        sl = st.slider("Mileage",min_value=10.0,max_value=300.00)
        val5=sl
        inputs.append(val5)

        #Torque value
        #min-4.8
        #max-850.0
        sl = st.slider("Torque value",min_value=1.0,max_value=800.0)
        val7=sl
        inputs.append(val7)

        
        bt=['Convertibles','Coupe','Hatchback','Hybrids','MUV','Minivans','Pickup Trucks','SUV','Sedan','Wagon']
        sb = st.selectbox('Body Type', bt) 
        for i in bt:
            if sb==i:
                inputs.append(1)
            else:
                inputs.append(0)

        #Insurance Validity_Comprehensive
        #Insurance Validity_Third Party
        
        insur=['Comprehensive','Third Party']
        sb = st.selectbox('Insurance', insur) 
        for ins in insur:
            if sb==ins:
                inputs.append(True)
            else:
                inputs.append(False)

        models=['Audi','BMW','Chevrolet','Citroen','Datsun','Fiat','Ford','Hindustan Motors','Honda','Hyundai','Isuzu',
        'Jaguar','Jeep','Kia','Land Rover','Lexus','MG','Mahindra','Mahindra Renault','Mahindra Ssangyong','Maruti','Mercedes-Benz',
        'Mini','Mitsubishi','Nissan','Porsche','Renault','Skoda','Tata','Toyota','Volkswagen','Volvo']
        sb = st.selectbox('Car models', models) 
        for m in models:
            if sb==m:
                inputs.append(True)
            else:
                inputs.append(False)

    
        fuel=['CNG','Diesel','Electric','LPG','Petrol']
        sb = st.selectbox('Fuel_type', fuel) 
        for m in fuel:
            if sb==m:
                inputs.append(True)
            else:
                inputs.append(False)

        Trans=['Automatic','Manual']
        sb = st.selectbox('Transmission', Trans) 
        for t in Trans:
            if sb==t:
                inputs.append(1)
            else:
                inputs.append(0)

        ower=[1,2,3,4,5]
        sb = st.selectbox('Owers', ower) 
        for o in ower:
            if sb==o:
                inputs.append(1)
            else:
                inputs.append(0)

        city=['bangalore','chennai','delhi','hyderabad','jaipur','kolkata']
        sb = st.selectbox('City', city) 
        for c in city:
            if sb==c:
                inputs.append(True)
            else:
                inputs.append(False)

        submitted = st.form_submit_button("Predict")

        
st.title("Car Price Prediction App")
st.write('Predict the selling price of a used car based on key features like year, kilometers driven, fuel type, transmission, and ownership history.')
    
with st.container(border=True):
    st.image("imgs/img8.jpg")
    if submitted:
        input_array = np.array([inputs])
        prediction = a.predict(input_array)
        #st.write(input_array)
        #st.write(f"Predicted Price: ₹{prediction[0]:,.0f}")
        if prediction < 100000:
            st.write(f"{prediction} (less than 1 Lakh)")
        else:
            lakhs_value = prediction / 100000
            st.write(f"Predicted Price: ₹{lakhs_value[0]:,.2f} Lakh")# Formats to two decimal places
        