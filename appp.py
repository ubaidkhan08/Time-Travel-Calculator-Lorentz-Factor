import streamlit as st
import numpy as np
import pandas as pd

def main():
    st.title("Time Travel/Dilation Calculator")
    html_temp = """
    <div style="background-color:black ;padding:30px">
    </div>
    """

    #Choice = st.radio("What do you wish to do?",('Necessary Velocity for Time Dilation', 'Calculate Time Dilation at any Velocity'))
    
    #if st.button('Necessary Velocity for Time Dilation'):
    #if Choice == 'Necessary Velocity for Time Dilation':
    
    st.subheader('Necessary Velocity for Time Dilation Calculation')
    a = st.slider('How many years of dilation?', 0.0, 1000.0) #Time_Travel
    b = st.slider('Expendable time in Years before the dilation (lesser the time, more the risk)', 0.0, 100.0) #Preferred_Duration
    if a<b:
        st.text("Dilation can not be in negative, yet, genius!")
       
    if st.button('Calculate the Velocity'):
        output = round(((np.sqrt(1 - (1/((a/b)*(a/b)))))*100),3)
        st.success('Your velocity should be: {}% of the speed of light.'.format(output))
    
    st.text("\n")
    st.text("\n")
    st.subheader('Calculate Time Dilation at any Velocity')
     #if st.button('Calculate Time Dilation at any Velocity'):
     #if Choice == 'Calculate Time Dilation at any Velocity':
    d = st.slider('Enter Current Velocity (% of speed of light)', 0.000, 100.000) #Current_Velocity
    c = d/100
    if st.button('Calculate Time Dilation'):
        gamma = (1 / (np.sqrt(1-c*c)))
        gammar = round((1 / (np.sqrt(1-c*c))),3)
        monthz = round((12-(12/gamma)),3)
        st.success('The Time Dilation would be: {} times'.format(gammar))
        st.text("Or you will experience: {} lesser month(s) if travelled for 1 year at this speed.".format(monthz))
        st.text("Or you will fast forward in time by: {} month(s).".format(monthz))
    
    if st.button('Calculate Time Dilation') && d==100:
        st.text("Time will come to a stop completely. Infinite Dilation!")
        
if __name__=='__main__':
    main()





