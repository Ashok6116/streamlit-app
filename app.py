import streamlit as st
import pickle as pkl
import numpy as np

#st.title("Car Prediction")
a=pkl.load(open('r_model.pkl','rb'))
st.title("Car Price Prediction App")
st.write('Predict the selling price of a used car based on key features like year, kilometers driven, fuel type, transmission, and ownership history.')

st.image("D:\car_projects\imgs\img7.png")
inputs = []

        #Kms Driven
        #min=101
        #max=5500000
sl1 = st.slider("Kms Driven",min_value=100,max_value=500000)
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
        #sl = st.slider("Torque value",min_value=1.0,max_value=800.0)
        #val7=sl
        #inputs.append(val7)

        
bt=['Convertibles','Coupe','Hatchback','Hybrids','MUV','Minivans','Pickup Trucks','SUV','Sedan','Wagon']
b = st.selectbox('Body Type', bt) 
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

        #models=['Audi','BMW','Chevrolet','Citroen','Datsun','Fiat','Ford','Hindustan Motors','Honda','Hyundai','Isuzu',
        #'Jaguar','Jeep','Kia','Land Rover','Lexus','MG','Mahindra','Mahindra Renault','Mahindra Ssangyong','Maruti','Mercedes-Benz',
        #'Mini','Mitsubishi','Nissan','Porsche','Renault','Skoda','Tata','Toyota','Volkswagen','Volvo']
        #sb = st.selectbox('Car models', models) 
        #for m in models:
        #    if sb==m:
        #        inputs.append(True)
        #    else:
        #        inputs.append(False)

    
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
    
audi={
                'Audi A3':1,
                'Audi A3 cabriolet':2,
                'Audi A4':3,
                'Audi A6':4,
                'Audi Q2':5,
                'Audi Q3':6,
                'Audi Q3 Sportback':7,
                'Audi Q5':8,
                'Audi Q7':9,
                'Audi S5 Sportback':10
}
bmw={
                'BMW 1 Series':11,
                'BMW 2 Series':12,
                'BMW 3 Series':13,
                'BMW 3 Series GT':14,
                'BMW 3 Series Gran Limousine':15,
                'BMW 5 Series':16,
                'BMW 6 Series':17,
                'BMW 7 Series':18,
                'BMW X1':19,
                'BMW X3':20,
                'BMW X4':21,
                'BMW X5':22,
                'BMW X7':23,
}
Chevrolet={
                'Chevrolet Aveo':24,
                'Chevrolet Aveo U-VA':25,
                'Chevrolet Beat':26,
                'Chevrolet Captiva':27,
                'Chevrolet Cruze':28,
                'Chevrolet Enjoy':29,
                'Chevrolet Optra':30,
                'Chevrolet Sail':31,
                'Chevrolet Spark':32,
                'Chevrolet Tavera':33,
                
}
Citroen={
                'Citroen C3':34,
                'Citroen C5 Aircross':35,
}
Datsun={
            'Datsun GO':36,
            'Datsun GO Plus':37,
            'Datsun RediGO':38,
}
Fiat={
            'Fiat Abarth Avventura':39,
            'Fiat Avventura':40,
            'Fiat Grande Punto':41,
            'Fiat Linea':42,
            'Fiat Palio':43,
            'Fiat Punto':44,
            'Fiat Punto Abarth':45,
            'Fiat Punto EVO':46,
            'Fiat Punto Pure':47,
}
Ford={
            'Ford Aspire':48,
            'Ford Ecosport':49,
            'Ford Endeavour':50,
            'Ford Fiesta':51,
            'Ford Fiesta Classic':52,
            'Ford Figo':53,
            'Ford Freestyle':54,
            'Ford Ikon':55,
            'Ford Mondeo':56,
}
Hindustan={
            'Hindustan Motors Contessa':57,
            'Ambassador':0,
}
Honda={
            'Honda Amaze':58,
            'Honda BR-V':59,
            'Honda Brio':60,
            'Honda CR-V':61,
            'Honda City':62,
            'Honda City Hybrid':63,
            'Honda Civic':64,
            'Honda Jazz':65,
            'Honda Mobilio':66,
            'Honda New Accord':67,
            'Honda WR-V':68,
}
Hyundai={
            'Hyundai Accent':69,
                'Hyundai Alcazar':70,
                'Hyundai Aura':71,
                'Hyundai Creta':72,
                'Hyundai EON':73,
                'Hyundai Elantra':74,
                'Hyundai Getz':75,
                'Hyundai Grand i10':76,
                'Hyundai Grand i10 Nios':77,
                'Hyundai Kona':78,
                'Hyundai Santa Fe':79,
                'Hyundai Santro':80,
                'Hyundai Santro Xing':81,
                'Hyundai Sonata':82,
                'Hyundai Tucson':83,
                'Hyundai Venue':84,
                'Hyundai Verna':85,
                'Hyundai Xcent':86,
                'Hyundai Xcent Prime':87,
                'Hyundai i10':88,
                'Hyundai i20':89,
                'Hyundai i20 Active':90,
                'Hyundai i20 N Line':91,
}
Isuzu={
            'Isuzu D-Max':92,
            'Isuzu MU 7':93,
            'Isuzu MU-X':94,
}
Jaguar={
            'Jaguar F-Pace':95,
                'Jaguar F-TYPE':96,
                'Jaguar XE':97,
                'Jaguar XF':98,
                'Jaguar XJ':99,
}
Jeep={
                'Jeep Compass':100,
                'Jeep Compass Trailhawk':101,
                'Jeep Meridian':102,
                'Jeep Wrangler':103,
}
Kia={
            'Kia Carens':104,
                'Kia Carnival':105,
                'Kia Seltos':106,
                'Kia Sonet':107,
}
Land_Rover={
                'Land Rover Defender':108,
                'Land Rover Discovery':109,
                'Land Rover Discovery Sport':110,
                'Land Rover Freelander 2':111,
                'Land Rover Range Rover':112,
                'Land Rover Range Rover Evoque':113,
                'Land Rover Range Rover Sport':114,
                'Land Rover Range Rover Velar':115,
}
Lexus={
                'Lexus ES':116,
                'Lexus RX':117,
}
Mahindra={
                'Mahindra Alturas G4':124,
                'Mahindra Bolero':125,
                'Mahindra Bolero Camper':126,
                'Mahindra Bolero Neo':127,
                'Mahindra Bolero Pik Up Extra Long':128,
                'Mahindra Bolero Power Plus':129,
                'Mahindra E Verito':130,
                'Mahindra Jeep':131,
                'Mahindra KUV 100':132,
                'Mahindra KUV 100 NXT':133,
                'Mahindra Marazzo':134,
                'Mahindra Quanto':135,
                'Mahindra Renault Logan':136,
                'Mahindra Scorpio':137,
                'Mahindra Scorpio Classic':138,
                'Mahindra Scorpio N':139,
                'Mahindra Ssangyong Rexton':140,
                'Mahindra TUV 300':141,
                'Mahindra TUV 300 Plus':142,
                'Mahindra Thar':143,
                'Mahindra Verito':144,
                'Mahindra XUV300':145,
                'Mahindra XUV500':146,
                'Mahindra XUV700':147,
                'Mahindra Xylo':148,
                'Mahindra e2o Plus':149,
}
Maruti={
                'Maruti 1000':150,
                'Maruti 800':151,
                'Maruti A-Star':152,
                'Maruti Alto':153,
                'Maruti Alto 800':154,
                'Maruti Alto K10':155,
                'Maruti Baleno':156,
                'Maruti Baleno RS':157,
                'Maruti Brezza':158,
                'Maruti Celerio':159,
                'Maruti Celerio Tour 2018-2021':160,
                'Maruti Celerio X':161,
                'Maruti Ciaz':162,
                'Maruti Eeco':163,
                'Maruti Ertiga':164,
                'Maruti Ertiga Tour':165,
                'Maruti Esteem':166,
                'Maruti Estilo':167,
                'Maruti FRONX':168,
                'Maruti Grand Vitara':169,
                'Maruti Gypsy':170,
                'Maruti Ignis':171,
                'Maruti Jimny':172,
                'Maruti Omni':173,
                'Maruti Ritz':174,
                'Maruti S-Presso':175,
                'Maruti SX4':176,
                'Maruti SX4 S Cross':177,
                'Maruti Swift':178,
                'Maruti Swift Dzire':179,
                'Maruti Swift Dzire Tour':180,
                'Maruti Versa':181,
                'Maruti Vitara Brezza':182,
                'Maruti Wagon R':183,
                'Maruti Wagon R Stingray':184,
                'Maruti XL6':185,
                'Maruti Zen':186,
                'Maruti Zen Estilo':187,
}
Mercedes_Benz={
                'Mercedes-Benz A Class':188,
                'Mercedes-Benz A-Class Limousine':189,
                'Mercedes-Benz AMG A 35':190,
                'Mercedes-Benz AMG G 63':191,
                'Mercedes-Benz AMG GLA 35':192,
                'Mercedes-Benz AMG GT':193,
                'Mercedes-Benz B Class':194,
                'Mercedes-Benz C-Class':195,
                'Mercedes-Benz CLA':196,
                'Mercedes-Benz CLS-Class':197,
                'Mercedes-Benz E-Class':198,
                'Mercedes-Benz EQC':199,
                'Mercedes-Benz G':200,
                'Mercedes-Benz GL-Class':201,
                'Mercedes-Benz GLA':202,
                'Mercedes-Benz GLA Class':203,
                'Mercedes-Benz GLC':204,
                'Mercedes-Benz GLC Coupe':205,
                'Mercedes-Benz GLE':206,
                'Mercedes-Benz GLS':207,
                'Mercedes-Benz M-Class':208,
                'Mercedes-Benz S-Class':209,
                'Mercedes-Benz SLC':210,
}
MG={
                'MG Astor':118,
                'MG Comet EV':119,
                'MG Gloster':120,
                'MG Hector':121,
                'MG Hector Plus':122,
                'MG ZS EV':123,
}
Mini={
                'Mini 3 DOOR':211,
                'Mini 5 DOOR':212,
                'Mini Cooper':213,
                'Mini Cooper Clubman':214,
                'Mini Cooper Convertible':215,
                'Mini Cooper Countryman':216,
                'Mini Cooper SE':217,
}
Mitsubishi={
                'Mitsubishi Cedia':218,
                'Mitsubishi Lancer':219,
                'Mitsubishi Outlander':220,
                'Mitsubishi Pajero':221,
}
Nissan={
                'Nissan Kicks':222,
                'Nissan Magnite':223,
                'Nissan Micra':224,
                'Nissan Micra Active':225,
                'Nissan Sunny':226,
                'Nissan Terrano':227,
}
Porsche={
                'Porsche 911':228,
                'Porsche Cayenne':229,
                'Porsche Macan':230,
                'Porsche Panamera':231,
}
Renault={
                'Renault Captur':232,
                'Renault Duster':233,
                'Renault Fluence':234,
                'Renault KWID':235,
                'Renault Kiger':236,
                'Renault Lodgy':237,
                'Renault Pulse':238,
                'Renault Scala':239,
                'Renault Triber':240,
}
Skoda={
                'Skoda Fabia':241,
                'Skoda Kodiaq':242,
                'Skoda Kushaq':243,
                'Skoda Laura':244,
                'Skoda Octavia':245,
                'Skoda Rapid':246,
                'Skoda Slavia':247,
                'Skoda Superb':248,
                'Skoda Yeti':249,
}
Tata={
            'Tata Altroz':250,
                'Tata Aria':251,
                'Tata Bolt':252,
                'Tata Harrier':253,
                'Tata Hexa':254,
                'Tata Indica':255,
                'Tata Indica V2':256,
                'Tata Indigo':257,
                'Tata Indigo Marina':258,
                'Tata Manza':259,
                'Tata Nano':260,
                'Tata New Safari':261,
                'Tata Nexon':262,
                'Tata Nexon EV':263,
                'Tata Nexon EV Max':264,
                'Tata Nexon EV Prime':265,
                'Tata Punch':266,
                'Tata Safari Storme':267,
                'Tata Sumo':268,
                'Tata Sumo Victa':269,
                'Tata Tiago':270,
                'Tata Tiago NRG':271,
                'Tata Tigor':272,
                'Tata Tigor EV':273,
                'Tata Yodha Pickup':274,
                'Tata Zest':275,
}
Toyota={
            'Toyota Camry':276,
                'Toyota Corolla':277,
                'Toyota Corolla Altis':278,
                'Toyota Etios':279,
                'Toyota Etios Cross':280,
                'Toyota Etios Liva':281,
                'Toyota Fortuner':282,
                'Toyota Fortuner Legender':283,
                'Toyota Glanza':284,
                'Toyota Hyryder':285,
                'Toyota Innova':286,
                'Toyota Innova Crysta':287,
                'Toyota Land Cruiser 300':288,
                'Toyota Qualis':289,
                'Toyota Urban cruiser':290,
                'Toyota Vellfire':291,
                'Toyota Yaris':292,
}
Volkswagen={
                'Volkswagen Ameo':293,
                'Volkswagen CrossPolo':294,
                'Volkswagen Jetta':295,
                'Volkswagen Passat':296,
                'Volkswagen Polo':297,
                'Volkswagen T-Roc':298,
                'Volkswagen Taigun':299,
                'Volkswagen Tiguan':300,
                'Volkswagen Tiguan Allspace':301,
                'Volkswagen Vento':302,
                'Volkswagen Virtus':303,
}
Volvo={
                'Volvo S 80':304,
                'Volvo S60':305,
                'Volvo S60 Cross Country':306,
                'Volvo S90':307,
                'Volvo V40':308,
                'Volvo XC 90':309,
                'Volvo XC40':310,
                'Volvo XC60':311,
}
    

r=st.radio(
label='Choose an option:',
options=['Audi','BMW','Citroen','Datsun','Fiat','Ford','Hindustan','Honda','Hyundai','Isuzu','Jaguar','Jeep','Kia','Lexus','Mahindra','Maruti','Mercedes_Benz',
         'MG','Mini','Mitsubishi','Nissan','Porsche','Renault','Skoda','Tata','Toyota','Volkswagen','Volvo'],
horizontal=True
)
if r=='Audi':
    sb3 = st.selectbox('Audi', audi)
    if sb3:
        val7=audi[sb3]
    inputs.append(val7)
if r=='BMW':
    sb3 = st.selectbox('BMW', bmw)
    if sb3:
        val7=bmw[sb3]
    inputs.append(val7)
if r=='Citroen':
    sb3 = st.selectbox('Citroen', Chevrolet)
    if sb3:
        val7=Chevrolet[sb3]
    inputs.append(val7)
if r=='Datsun':
    sb3 = st.selectbox('Datsun', Datsun)
    if sb3:
        val7=Datsun[sb3]
    inputs.append(val7)
if r=='Fiat':
    sb3 = st.selectbox('Fiat', Fiat)
    if sb3:
        val7=Fiat[sb3]
    inputs.append(val7)
if r=='Ford':
    sb3 = st.selectbox('Ford', Ford)
    if sb3:
        val7=Ford[sb3]
    inputs.append(val7)
if r=='Hindustan':
    sb3 = st.selectbox('Hindustan', Hindustan)
    if sb3:
        val7=Hindustan[sb3]
    inputs.append(val7)
if r=='Honda':
    sb3 = st.selectbox('Honda', Honda)
    if sb3:
        val7=Honda[sb3]
    inputs.append(val7)
if r=='Hyundai':
    sb3 = st.selectbox('Hyundai', Hyundai)
    if sb3:
        val7=Hyundai[sb3]
    inputs.append(val7)
if r=='Isuzu':
    sb3 = st.selectbox('Isuzu', Isuzu)
    if sb3:
        val7=Isuzu[sb3]
    inputs.append(val7)
if r=='Jaguar':
    sb3 = st.selectbox('Jaguar', Jaguar)
    if sb3:
        val7=Jaguar[sb3]
    inputs.append(val7)
if r=='Jeep':
    sb3 = st.selectbox('Jeep', Jeep)
    if sb3:
        val7=Jeep[sb3]
    inputs.append(val7)
if r=='Kia':
    sb3 = st.selectbox('Kia', Kia)
    if sb3:
        val7=Kia[sb3]
    inputs.append(val7)
if r=='Lexus':
    sb3 = st.selectbox('Lexus', Lexus)
    if sb3:
        val7=Lexus[sb3]
    inputs.append(val7)
if r=='Mahindra':
    sb3 = st.selectbox('Mahindra', Mahindra)
    if sb3:
        val7=Mahindra[sb3]
    inputs.append(val7)
if r=='Maruti':
    sb3 = st.selectbox('Maruti', Maruti)
    if sb3:
        val7=Maruti[sb3]
    inputs.append(val7)
if r=='Mercedes_Benz':
    sb3 = st.selectbox('Mercedes_Benz', Mercedes_Benz)
    if sb3:
        val7=Mercedes_Benz[sb3]
    inputs.append(val7)
if r=='MG':
    sb3 = st.selectbox('MG', MG)
    if sb3:
        val7=MG[sb3]
    inputs.append(val7)
if r=='Mini':
    sb3 = st.selectbox('Mini', Mini)
    if sb3:
        val7=Mini[sb3]
    inputs.append(val7)
if r=='Mitsubishi':
    sb3 = st.selectbox('Mitsubishi', Mitsubishi)
    if sb3:
        val7=Mitsubishi[sb3]
    inputs.append(val7)
if r=='Nissan':
    sb3 = st.selectbox('Nissan', Nissan)
    if sb3:
        val7=Nissan[sb3]
    inputs.append(val7)
if r=='Porsche':
    sb3 = st.selectbox('Porsche', Porsche)
    if sb3:
        val7=Porsche[sb3]
    inputs.append(val7)
if r=='Renault':
    sb3 = st.selectbox('Renault', Renault)
    if sb3:
        val7=Renault[sb3]
    inputs.append(val7)
if r=='Skoda':
    sb3 = st.selectbox('Skoda', Renault)
    if sb3:
        val7=Skoda[sb3]
    inputs.append(val7)
if r=='Tata':
    sb3 = st.selectbox('Tata', Tata)
    if sb3:
        val7=Tata[sb3]
    inputs.append(val7)
if r=='Toyota':
    sb3 = st.selectbox('Toyota', Toyota)
    if sb3:
        val7=Toyota[sb3]
    inputs.append(val7)
if r=='Volkswagen':
    sb3 = st.selectbox('Volkswagen', Volkswagen)
    if sb3:
        val7=Volkswagen[sb3]
    inputs.append(val7)
if r=='Volvo':
    sb3 = st.selectbox('Volvo', Volvo)
    if sb3:
        val7=Volvo[sb3]
    inputs.append(val7)


        
#st.title("Car Price Prediction App")

submitted = st.button("Predict")    
with st.container(border=True):
    st.image("D:\car_projects\imgs\img8.jpg")
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


