import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import tempfile


st.set_page_config(page_title="Automated EDA Tool", layout="centered")

st.title("📊 Automated EDA Tool")
st.markdown("Upload your CSV or JSON file and generate a full EDA report using Pandas Profiling, by Utk_rsh")


uploaded_file = st.file_uploader("Choose a file", type=["csv", "json"])

if uploaded_file is not None:
    try:
       
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_json(uploaded_file)

        st.success("✅ File uploaded successfully!")
        st.write("🔍 Preview of your data:")
        st.dataframe(df.head())

       
        if st.button("Generate EDA Report"):
            with st.spinner("⏳ Generating Report... please wait..."):
                
                profile = ProfileReport(df, title="EDA Report", explorative=True)

                
                with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp_file:
                    profile.to_file(tmp_file.name)
                    st.success("✅ Report generated successfully!")

                   
                    with open(tmp_file.name, "rb") as f:
                        st.download_button(
                            label="📎 Download EDA Report",
                            data=f,
                            file_name="EDA_Report.html",
                            mime="text/html"
                        )
    except Exception as e:
        st.error(f"❌ Error: {e}")
else:
    st.info("📂 Please upload a CSV or JSON file to begin.")
