import streamlit as st


st.markdown("""
<style>
/* Target the specific button by its key-derived wrapper class */
div[class*="st-key-link-"] .stButton button {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    color: #1a73e8 !important;                 /* link blue */
    text-decoration: underline !important;      /* underline like a hyperlink */
    font-weight: normal !important;
    box-shadow: none !important;
}
div[class*="st-key-link-"] .stButton button:hover {
    color: #174ea6 !important;                  /* darker on hover */
    text-decoration: underline !important;
}
div[class*="st-key-link-"] .stButton button:focus {
    outline: none !important;
    box-shadow: none !important;
}
</style>
""", unsafe_allow_html=True)

def show(text: str):
    st.session_state.message = text


st.markdown(
    """
    <h1 style='text-align: center;'>
        <img src='https://docs.streamlit.io/logo.svg' style='height:50px; margin-right:10px;'>
        Streamlit
    </h1>
    <p style='text-align: center; color: #999;'> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A demo by Satish Karengula</p>
    """,
    unsafe_allow_html=True
)
st.caption("Important functions")
col1, col2, col3 = st.columns(3)
with col1:
    btn_text_elements = st.button("Text Elements")
    btn_status_elements = st.button("Status Elements")
    btn_input_widges = st.button("Input Widges")
with col2:
    btn_chat_elements = st.button("Chat Elements")
    btn_data_elements = st.button("Data Elements")
    btn_chart_elements = st.button("Chart Elements")
with col3:
    btn_media_elements = st.button("Media Elements")
    btn_layouts = st.button("Layouts")

# Function to split list into chunks of size n
def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# Mapping of string names to actual Streamlit functions
text_elements_map = {
    "title": st.title,
    "caption": st.caption,
    "header": st.header,
    "subheader": st.subheader,
    "markdown": st.markdown,
    "text": st.text,
    "write": st.write,
    "badge": st.badge,
    "code": st.code,
    "divider": st.divider,
    "echo": st.echo,
    "latex": st.latex,
    "help": st.help,
    "html": st.markdown  # HTML can be rendered via markdown with unsafe_allow_html=True
}

status_elements_map = {
    "success": st.success,
    "info": st.info,
    "warning": st.warning,
    "error": st.error,
    "exception": st.exception,
    "progress": st.progress,
    "spinner": st.spinner,
    "status": st.status,
    "toast": st.toast,
    "balloons": st.balloons,
    "snow": st.snow
}

input_widges_map = {
    "button": st.button,
    "text_input": st.text_input,
    "number_input": st.number_input,
    "date_input": st.date_input,
    "time_input": st.time_input,
    "color_picker": st.color_picker,
    "toggle": st.toggle,
    "checkbox": st.checkbox,
    "radio": st.radio,
    "selectbox": st.selectbox,
    "multiselect": st.multiselect,
    "select_slider": st.select_slider,
    "pills": st.pills,
    "segmented_control": st.segmented_control,
    "feedback": st.feedback
}

data_elements_map = {
    "dataframe": st.dataframe,
    "data_editor": st.data_editor,
    "table": st.table
}

chat_elements_map = {
    "chat_input": st.chat_input,
    "chat_message": st.chat_message,
    "write_stream": st.write_stream
}

chart_elements_map = {
    "line_chart": st.line_chart,
    "bar_chart": st.bar_chart,
    "scatter_chart": st.scatter_chart,
    "area_chart": st.area_chart,
}

media_elements_map ={
    "audio": st.audio,
    "image": st.image,
    "video": st.video
}

layouts_map = {
    "columns": st.columns,
    "container": st.container,
    "expander": st.expander,
    "popover": st.popover,
    "sidebar": st.sidebar,
    "tabs": st.tabs,
    "form": st.form,
}


if btn_text_elements:
    st.session_state.elements_map = text_elements_map
if btn_status_elements:
    st.session_state.elements_map = status_elements_map
if btn_input_widges:
    st.session_state.elements_map = input_widges_map
if btn_chat_elements:
    st.session_state.elements_map = chat_elements_map
if btn_chat_elements:
    st.session_state.elements_map = chat_elements_map
if btn_data_elements:
    st.session_state.elements_map = data_elements_map
if btn_chart_elements:
    st.session_state.elements_map = chart_elements_map
if btn_media_elements:
    st.session_state.elements_map = media_elements_map
if btn_layouts:
    st.session_state.elements_map = layouts_map

# show elements in each map
if "elements_map" in st.session_state:
    st.divider()
    for chunk in chunk_list(list(st.session_state.elements_map.keys()), 7):
        cols = st.columns(len(chunk))
        for col, element in zip(cols, chunk):
            if col.button(str(element), key=f"link-{element}"):
                st.session_state.clicked_element = element

# Show help for the clicked element
if "clicked_element" in st.session_state:
    st.divider()
    func = st.session_state.elements_map.get(st.session_state.clicked_element)
    if func:
        st.help(func)
