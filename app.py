import streamlit as st
import pickle
import numpy as np
import pandas as pd

def find_fueltype(fueltype):
	dic = {
		"CNG": 0,
		"CNG + CNG": 1,
		"Diesel": 2,
		"Hybrid": 3,
		"LPG": 4,
		"Petrol": 5,
		"Petrol + CNG": 6
	}

	return dic.get(fueltype)

def find_owner(owner):
	dic = {
		"First": 0,
		"Second": 1,
		"Third": 2,
		"UnRegistered Car": 3
	}

	return dic.get(owner)

def find_transmission(transmission):
	dic = {
		"Automatic": 0,
		"Manual": 1
	}

	return dic.get(transmission)

def find_sellertype(sellertype):
	dic = {
		"Commercial Registration": 0,
		"Corporate": 1,
		"Individual": 2
	}

	return dic.get(sellertype)

def find_drivetrain(drivetrain):
	dic = {
		"AWD": 0,
		"FWD": 1,
		"RWD": 2
	}

	return dic.get(drivetrain)

fueltypes = ["CNG", "CNG + CNG", "Diesel", "Hybrid", "LPG", "Petrol", "Petrol + CNG"]
owners = ["First", "Second", "Third", "UnRegistered Car"]
transmissions = ["Automatic", "Manual"]
sellertypes = ["Commercial Registration", "Corporate", "Individual"]
drivetrains = ["AWD", "FWD", "RWD"]

model = pickle.load(open("RFcar.pkl", "rb"))

st.title("Car Price Prediction")
year = st.number_input("Year")
kilometer = st.number_input("Kilometer")
fueltype = st.selectbox("Fuel Type", fueltypes)
transmission = st.selectbox("Transmission", transmissions)
owner = st.selectbox("Owner", owners)
sellertype = st.selectbox("Seller Type", sellertypes)
engine = st.number_input("Engine")
maxpower = st.number_input("Max Power")
maxtorque = st.number_input("Max Torque")
drivetrain = st.selectbox("Drivetrain", drivetrains)
length = st.number_input("Length")
width = st.number_input("Width")
height= st.number_input("Height")
seating_capacity = st.number_input("Seating Capacity")
fueltank_capacity = st.number_input("Fuel Tank Capacity")

if st.button("Predict"):
	fueltype = find_fueltype(fueltype)
	owner = find_owner(owner)
	transmission = find_transmission(transmission)
	sellertype = find_sellertype(sellertype)
	drivetrain = find_drivetrain(drivetrain)

	test = np.array([[year, kilometer, fueltype, transmission, owner, sellertype, engine, maxpower, maxtorque, drivetrain, length, width, height, seating_capacity, fueltank_capacity]])
	res = model.predict(test).item()
	print(res)
	st.success("Predicted Price: " + str(res))
