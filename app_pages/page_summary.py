import streamlit as st 
from PIL import Image

def project_summary_page():
    """
    Contents of summary page.
    """
    st.title("Summary")

    st.header("Introduction :cherries:")

    st.markdown("Farmy & Foods is a cherry plantation presented with a problem -"
                 " some of their cherry leaves contain **powdery mildew**."
                 " The current process involves manually inspecting every tree,"
                 " of which there are thousands, across multiple farms to visually"
                 " check if a given leaf is **healthy** or not. A compound is then"
                 " added to kill the fungus. This is incredibly time consuming and"
                 " ultimately not feasible in the long term, particularly if the "
                 " plantation is to expand.")
   
    image = Image.open("media/images/cherries.jpg")
    st.image(image, caption="Cherries on a cherry tree")

    st.info("White powdery patches can be found on young leaves especially during"
            " high humidity. Early detection is crucial. The eventual coverage of the"
            " cherry's surface with this fungal growth renders them unmarketable.")

    st.header("Solution :bulb:")

    st.markdown("Farmy & Foods' IT team have decided to pursue a solution which uses"
                " Machine Learning. A model will be trained using thousands of images"
                " depicting both healthy and powdery mildew containing cherry leaves"
                " to enable the prediction of whether a given cherry leaf is healthy"
                " or not. If successful, this could be extended to detecting pests for"
                " other crops and provide a practical solution to the problem that has"
                " been plaguing them.")

    st.header("Business Requirements")

    st.success("1. The client is interested in visualising the differences between"
               " healthy cherry leaves and those containing powdery mildew. (See"
               " the next page).\n 2. The client is interested in predicting whether"
               " a given cherr leaf is healthy or contains powdery mildew.")

    st.header("Additional Information")

    st.info("For more information on this project"
           " [check out the README.]"
           "(https://github.com/Hasmelash95/cherry-leaves-mildew-detection/blob/main/README.md)")