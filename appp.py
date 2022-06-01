import streamlit as st
import numpy as np
import pandas as pd

def main():
    st.title("Time Travel/Dilation Calculator")
    html_temp = """
    <div style="background-color:black ;padding:30px">
    </div>
    """
    st.text("\n")
  
    st.text("This calculator uses Lorentz Factor to express how much the measurements of time,\nlength, and other physical properties change for an object while that object\nis moving at higher relative velocities. It is generally denoted by γ, and is used in\nLorentz Transformation, Time Dilation, Length contraction, Relativistic mass,\nRelativistic momentum, etc!")
   
    st.text("\n")
    st.text("\n")
    st.text("\n")
  
    
    data = [[0,1,1.0],[0.050,1.001,0.999],[0.100,1.005,0.995],[0.150,1.011,0.989],[0.200,1.021,0.979],[0.250,1.033,0.968],[0.3,1.048,0.954],[0.4,1.091,0.916],[0.5,1.154,0.866],[0.6,1.25,0.800],[0.7,1.400,0.714],[0.8,1.66,0.602],[0.866,2,0.500],[0.9,2.29,0.436],[0.95,3.202,0.312],[0.99,7.089,0.141],[0.992,7.92,0.126],[0.995,10.0125,0.099],[0.998,15.81,0.0632],[0.9989,21.32,0.046],[0.999,22.366,0.044]]     
    df = pd.DataFrame(data, columns=['Ratio of v to c', 'Lorentz Factor','Reciprocal'])
    dff = df.set_index('Ratio of v to c')
    
    st.line_chart(data=dff, width=0, height=0, use_container_width=True)
    
    st.text("\n")
    st.text("\n")
    
    from PIL import Image
    image = Image.open('lorentz.svg')
    st.image(image, caption='The Lorentz factor has the Maclaurin series:')
    
    st.text("\n")
    st.text("\n")
    st.text("\n")
    
    st.subheader('Necessary Velocity for Time Dilation Calculation')
    st.text("\n")
    a = st.slider('How many years of dilation?', 0.0, 1000.0) #Time_Travel
    st.text("\n")
    b = st.slider('Expendable time in Years before the dilation (lesser the time, more the risk)', 0.0, 100.0) #Preferred_Duration
    if a<b:
        st.text("Dilation can not be in negative, yet, genius!")
       
    if st.button('Calculate the Velocity'):
        output = round(((np.sqrt(1 - (1/((a/b)*(a/b)))))*100),3)
        st.success('Your velocity should be: {}% of the speed of light.'.format(output))
    
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    
    st.subheader('Calculate Time Dilation at any Velocity')
    
    d = st.slider('Enter Current Velocity (% of speed of light)', 0.000, 100.000) #Current_Velocity
    c = d/100
    
    if st.button('Calculate Time Dilation'):
        if d==100:
            st.text("Time will come to a stop completely. Infinite Dilation!")
            
            
        gamma = (1 / (np.sqrt(1-c*c)))
        gammar = round((1 / (np.sqrt(1-c*c))),3)
        monthz = round((12-(12/gamma)),3)
        st.success('The Time Dilation would be: {} times'.format(gammar))
        st.text("Or you will experience: {} lesser month(s) if travelled for 1 year at this speed.".format(monthz))
        st.text("Or you will fast forward in time by: {} month(s).".format(monthz))
    
        st.text("\n")
        st.text("\n")
        st.text("\n")
        
        st.dataframe(data=df, width=900, height=500)
        
        
if __name__=='__main__':
    main()





