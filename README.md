1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/watson-chatbot.git
    git clone https://github.com/SwastikaSoni/Chatbot
    ```

2. Navigate to the project directory:

    ```bash
    cd watson-chatbot
    cd Chatbot
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    pip install .
    ```

### Configuration
@@ -43,16 +43,16 @@ Follow these steps to set up and run the chatbot application:
2. Add your IBM Watson API keys and project ID to the `.env` file:

    ```dotenv
    WATSON_API_KEY=your_watson_api_key
    WATSON_PROJECT_ID=your_watson_project_id
    API_KEY=your_watson_api_key
    project_id=your_watson_project_id
    ```

### Running the Application

Run the chatbot application using the following command:

```bash
streamlit run chatbot.py
streamlit run main.py
```

The application will start and open in your default web browser. You can now interact with the chatbot by typing messages and receiving responses.
