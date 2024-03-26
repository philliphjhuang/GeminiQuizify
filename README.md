# Gemini Quizify
The AI-Generated Quiz Tool project focuses on providing students and learners with accessible and effective means to reinforce their understanding of various topics. Leveraging AI technology, the tool dynamically generates quizzes based on user-provided documents, offering instant feedback and detailed explanations to facilitate deeper comprehension and retention of knowledge, ultimately enhancing the learning experience.

## Installation

1. Enable Google Cloud through this [Link](https://cloud.google.com/cloud-console?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-e-dr-1707554&utm_content=text-ad-none-any-DEV_c-CRE_665735422256-ADGP_Hybrid%20%7C%20BKWS%20-%20MIX%20%7C%20Txt-Management%20Tools-Cloud%20Console-KWID_43700077225654741-kwd-55675752867&utm_term=KW_google%20cloud%20console-ST_google%20cloud%20console&gad_source=1&gclid=Cj0KCQiArrCvBhCNARIsAOkAGcXO2_affz2IH9q_ps1LDwrdsOe43AmOiJps1j9UK_ri0mnBWRd9eA0aApkNEALw_wcB&gclsrc=aw.ds).
- Go to vertexAI and 'Enable All Recommended APIs'
- Go to 'IAM & Admin' and then 'Service Accounts'
- Create a service account and download the .json file.
- Run the following command in VSCode
  ```
  export GOOGLE_APPLICATION_CREDENTIALS = "/path/to/your/authentication-file.json"
  ```

2. Open VSCode and enter the following text:
   ```
   gcloud init
   ```

3. Create new or re-initialize your configuration, log in with your account, and create or choose your project.
   ![image](https://github.com/philliphjhuang/RadicalX/assets/30792325/6e345325-36fb-4ba8-b65a-82d2cb023294)

4. Install the packages in requirement.txt:
   ```
   pip install -r requirements.txt
   ```
5. In the command prompt, go to the directory that contains gemini_explorer.py and run the following command to launch the app:
   ```
   streamlit run task10.py
   ```
## Functions
Allows users to upload multiple PDFs, enter a topic, choose the number of questions, and generate a multiple-choice quiz based on the PDFs and the topic.
![image](https://github.com/philliphjhuang/GeminiQuizify/assets/30792325/001ddd74-2e66-44bd-b98b-a87cda062d0d)

After pressing submit, it generates question(s) and allows to user to choose answer choices, submit, and go to next/previous questions.

![image](https://github.com/philliphjhuang/GeminiQuizify/assets/30792325/a4b8602e-81e1-455c-b19a-e139f2be3055)

# Video demonstration
[Watch the video](https://www.loom.com/share/e36fc7013b0b4a138ffb630db3ed7cfe?sid=2d31deb6-960b-4b7a-ac35-c082e96ea4ae)

# Certificate
![image](https://github.com/philliphjhuang/GeminiQuizify/assets/30792325/12c1c88c-9ef9-47e6-ab77-0b5e207bfb9c)

## Contributers
- Phillip Huang
  - [Linkedin](https://www.linkedin.com/in/phillip-huang-449b64229/)
  - [Github](https://github.com/philliphjhuang)
- Radical AI for providing this experience on AI Engineering.
