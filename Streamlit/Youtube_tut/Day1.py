import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World!")
st.title("What is this?")

st.header("This is the header")
a="a \n \n"*15
st.write(a)
st.divider()

example_code="""
import streamlit as st
st.write("hello world")
"""
st.code(example_code,language="python")
st.divider()
imglist=[r"media\215.jpg",r"media\14046.jpg"]
st.image(imglist,caption=["Good Tokyo","Tokyo Tower"])

dict={
    "Name":["sathish","kumar","Athi","Who"],
    "Height":[175,180,182,165],
}
df=pd.DataFrame(dict)

st.table(df)
st.subheader("Interactable Dataframe")
st.dataframe(df)

newdata=st.data_editor(df)

st.subheader("New data here")
st.dataframe(newdata)

st.subheader("Metric section:")
st.metric(label="Average Height",value=df["Height"].mean())

ndf=pd.DataFrame(
    data=np.random.randn(100,2),
    columns=["lat","lon"]
)
st.divider()
st.area_chart(ndf)
st.divider()
st.bar_chart(ndf)
st.divider()
st.scatter_chart(ndf)


mdf=pd.DataFrame(
    data=np.random.randn(100,2)/[1,2]+[12,78],
    columns=["lat","lon"]
)
st.map(data=mdf)