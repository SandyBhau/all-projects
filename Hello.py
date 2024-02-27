# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hi My name is Sandesh Bharitkar",
        page_icon="👋",
    )

    st.write("# This are demo project")

    st.sidebar.success("Select a above demo projects.")

    st.markdown(
        """
        **👈 Select a project demo from the sidebar** to see some examples!
        ### Current Demo Project - 
        - QnA Chatbot using Meta Hugging Face [ChatBot](https://all-projects-sandesh.streamlit.app/llama2_QnA_Chatbot)
        - Monkey Pox Prediction [Predictor](https://all-projects-sandesh.streamlit.app/Monkey_Pox_Predictor)
        - Free Translator to English Language [Translator](https://all-projects-sandesh.streamlit.app/Translator)
        ### Please check out my profile?
        - [Linkedin](https://www.linkedin.com/in/sandesh-bharitkar/)
        - [GitHub](https://github.com/SandyBhau)
        - [HackerRank](https://www.hackerrank.com/profile/sandeshbharitka1)
    """
    )


if __name__ == "__main__":
    run()
