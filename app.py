import streamlit as st
import pandas as pd
import joblib

def parse_numeric(s):
    try:
        return float(str(s).replace(',', '').strip())
    except:
        return 0

# Load the model
@st.cache_resource
def load_model():
    return joblib.load('rf_politician_model_pipeline.pkl')

# Main Streamlit app
def main():
    st.title(" Political Candidate Win Predictor")

    st.markdown("### Enter Candidate Details:")

    party = st.selectbox("Party", ["--Select party name--","BJP", "INC", "AAP", "SP", "BSP", "Independent", "Other"])
    education = st.selectbox("Education Level", ["--Select qualification details--",
        "10th Pass", "12th Pass", "Graduate", "Graduate Professional",
        "Post Graduate", "Doctorate", "Illiterate", "Others"
    ])
    gender = st.selectbox("Gender", ['',"MALE", "FEMALE", "OTHER"])
    category = st.selectbox("Category", ['',"GENERAL", "OBC", "SC", "ST", "Other"])

    criminal_cases = st.number_input("Number of Criminal Cases", min_value=0)
    age = st.number_input("Age", min_value=25, max_value=100, value=35)
    total_votes = st.number_input("Total Votes", min_value=0)
    total_electors = st.number_input("Total Electors (in lakhs)", min_value=0.0)

    assets = st.text_input("Assets (e.g., 13,46,593)", value="0")
    liabilities = st.text_input("Liabilities (e.g., 7,36,605)", value="0")

    
    if st.button("Predict Outcome"):
        if "Select" in party or "Select" in education or "Select" in gender or "Select" in category:
            st.error(" Please fill in all candidate details before predicting.")
            
        else:
            model = load_model()
            input_data = {
            'PARTY': party,
            'EDUCATION': education,
            'GENDER': gender,
            'CATEGORY': category,
            'CRIMINAL CASES': criminal_cases,
            'AGE': age,
            'TOTAL VOTES': total_votes,
            'TOTAL ELECTORS': total_electors,
            'ASSETS': parse_numeric(assets),
            'LIABILITIES': parse_numeric(liabilities)
        }

        input_df = pd.DataFrame([input_data])
        st.session_state['input_df'] = input_df  

        prediction = model.predict(input_df)[0]
        result = " WIN" if prediction == 1 else " NOT WIN"
        st.success(f"The candidate is predicted to: **{result}**")


    if st.checkbox("Show Candidate Input Data"):
        if 'input_df' in st.session_state:
            st.markdown("#### Candidate Data Preview:")
            st.dataframe(st.session_state['input_df'])
        else:
            st.warning("Please predict first to view the input data.")


if __name__ == "__main__":
    main()
