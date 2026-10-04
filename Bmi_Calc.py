import streamlit as st 
from openai import OpenAI

st.title("AI-Powered BMI Analysis")
st.write("Calculate your BMI and get AI-generated insights")

NVIDIA_API_KEY=st.secrets["NVIDIA_API_KEY"]

client = OpenAI(
api_key=NVIDIA_API_KEY,
base_url="https://integrate.api.nvidia.com/v1"
)

name=st.text_input("Enter your name:")
wt=st.number_input("Enter your weight in kg:",min_value=1.0)
ht=st.number_input("Enter your height in cm:",min_value=1.0)

#Calculate the BMI
if st.button("Calculate BMI"):
   bmi = round(wt / (ht/100)**2,2)
   st.write(f"{name}, with your weight {wt} kg and height {ht} cm,your BMI is:{bmi}")

bmi = round(wt / (ht/100)**2,2)
if st.button("Get AI Analysis"):
   PROMPT=f"Act like an expert nutritionist, comment on the BMI with the following data: height as {ht}, weight as {wt}, and BMI as {bmi}. The user data is mainly from Indians. Give the analysis in a friendly tone and provide suggestions for a healthy lifestyle. Also, provide a diet plan for the user based on the BMI value in a table format. The diet plan should be for 7 days and should include breakfast, lunch, dinner, and snacks. Also, provide a list of exercises that the user can do to maintain a healthy lifestyle.The output shouldn't be more than 100 words."
   with st.status("Analyzing....."):
    response=client.chat.completions.create(
   model="z-ai/glm-5.3-flash",
   messages=[
     {"role": "user", "content": PROMPT}
]
)
   ai_response=response.choices[0].message.content
   st.subheader("AI Nutrition Analysis")
   st.write(ai_response)