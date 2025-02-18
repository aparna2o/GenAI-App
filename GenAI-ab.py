
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "457170eb",
   "metadata": {},
   "source": [
    "### GenAI App - AI Code Reviewer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "acefbf07",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in d:\\anaconda\\lib\\site-packages (1.42.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (1.9.0)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (5.5.1)\n",
      "Requirement already satisfied: click<9,>=7.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: numpy<3,>=1.23 in d:\\anaconda\\lib\\site-packages (from streamlit) (1.24.3)\n",
      "Requirement already satisfied: packaging<25,>=20 in d:\\anaconda\\lib\\site-packages (from streamlit) (23.0)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (1.5.3)\n",
      "Requirement already satisfied: pillow<12,>=7.1.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (9.4.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in d:\\anaconda\\lib\\site-packages (from streamlit) (5.29.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (11.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in d:\\anaconda\\lib\\site-packages (from streamlit) (2.29.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (13.9.4)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in d:\\anaconda\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.4.0 in d:\\anaconda\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in d:\\anaconda\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in d:\\anaconda\\lib\\site-packages (from streamlit) (3.1.44)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in d:\\anaconda\\lib\\site-packages (from streamlit) (0.9.1)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in d:\\anaconda\\lib\\site-packages (from streamlit) (6.2)\n",
      "Requirement already satisfied: jinja2 in d:\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in d:\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.17.3)\n",
      "Requirement already satisfied: narwhals>=1.14.2 in d:\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (1.27.0)\n",
      "Requirement already satisfied: colorama in d:\\anaconda\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in d:\\anaconda\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
      "Requirement already satisfied: python-dateutil>=2.8.1 in d:\\anaconda\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in d:\\anaconda\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2022.7)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in d:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in d:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in d:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (1.26.16)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in d:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2023.5.7)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in d:\\anaconda\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in d:\\anaconda\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in d:\\anaconda\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in d:\\anaconda\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in d:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (22.1.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in d:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in d:\\anaconda\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: six>=1.5 in d:\\anaconda\\lib\\site-packages (from python-dateutil>=2.8.1->pandas<3,>=1.4.0->streamlit) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "36a8a93e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "\n",
    "\n",
    "import google.generativeai as genai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1013bb8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "f = open('key_file.txt')\n",
    "key = f.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0d4367c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "genai.configure(api_key=\"AIzaSyCZiEyEdvqFosIjk6MLhC76K-Ig-jWCcFU\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "976ba567",
   "metadata": {},
   "outputs": [],
   "source": [
    "system_prompt =\"\"\"you are helpful AI code reviewer.\n",
    "                  User will submit their code to you, you have to analyse it and create a code review containing the errors \n",
    "                  in the code and tell the user about the mistakes pointwise as bug report and also you should\n",
    "                  also generate corrected code as fixed code. Incase if the code contains no error tell\n",
    "                  user its perfect\"\"\"\n",
    "\n",
    "model = genai.GenerativeModel(model_name=\"models/gemini-2.0-flash-exp\",\n",
    "                             system_instruction=system_prompt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3d06730f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-02-17 17:50:01.414 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-17 17:50:02.773 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run D:\\Anaconda\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-02-17 17:50:02.774 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title(\"AN AI Code Reviewer\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0fa8d7ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-02-17 17:50:17.582 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-17 17:50:17.584 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-17 17:50:17.585 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-17 17:50:17.587 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-17 17:50:17.588 Session state does not function when running a script without `streamlit run`\n",
      "2025-02-17 17:50:17.590 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-17 17:50:17.591 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "user_prompt=st.text_area(\"Enter your python code here ...\",placeholder=\"Type your code here...\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0056d44e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-02-17 17:50:51.684 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-17 17:50:51.686 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-17 17:50:51.688 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-17 17:50:51.691 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-17 17:50:51.696 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "button_click = st.button(\"Generate\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "659dae2f",
   "metadata": {},
   "outputs": [],
   "source": [
    "if button_click ==True:\n",
    "\n",
    "    response=model.generate_content(user_prompt)\n",
    "    \n",
    "    st.write(response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a8598baa",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
