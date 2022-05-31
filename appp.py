import streamlit as st
from joblib import dump, load
import numpy as np
import pandas as pd

#log_model = load('university_admission.joblib')

def main():
    st.title("Time Travel/Dilation Calculator")
    html_temp = """
    <div style="background-color:black ;padding:30px">
    </div>
    """

    Choice = st.radio("What do you wish to do?",('Necessary Velocity for Time Dilation', 'Calculate Time Dilation at any Velocity'))

    if Choice == 'Necessary Velocity for Time Dilation':
        a = st.slider('How many years of dilation?', 0, 100) #Time_Travel
        b = st.slider('Expendable time before the dilation (lesser the time, more the risk)', 0, 100) #Preferred_Duration
        if st.button('Calculate the Velocity'):
            output = round(((np.sqrt(1 - (1/((a/b)*(a/b)))))*100),3)
            st.success('Your velocity should be: {}% of the speed of light.'.format(output))

    else:
        c = st.slider('Enter Current Velocity (in m/sec)', 0, 299792458) #Current_Velocity
        if st.button('Calculate Time Dilation'):
            gamma = (1 / (np.sqrt(1-c*c)))
            gammar = round((1 / (np.sqrt(1-c*c))),3)
            monthz = round((12-(12/gamma)),3)
            st.success('The Time Dilation would be: {} times'.format(gammar))
            st.text("Or you will experience: {} lesser month(s).".format(monthz))



if __name__=='__main__':
    main()




