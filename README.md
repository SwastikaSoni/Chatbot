## Hosted Link

The chatbot is hosted at [https://chatbot-swastika.streamlit.app/](https://chatbot-swastika.streamlit.app/).

---
1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/SwastikaSoni/Chatbot
    ```

2. Navigate to the project directory:

    ```bash
    cd Chatbot
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    pip install .
    ```

### Configuration
Follow these steps to set up and run the chatbot application:

2. Add your IBM Watson API keys and project ID to the `.env` file:

    ```dotenv
    API_KEY=your_watson_api_key
    PROJECT_ID=your_watson_project_id
    ```

### Running the Application

Run the chatbot application using the following command in the terminal:

```bash
streamlit run main.py
```

The application will start and open in your default web browser. You can now interact with the chatbot by typing messages and receiving responses.
