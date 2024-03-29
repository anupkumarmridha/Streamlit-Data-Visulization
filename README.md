# Streamlit-Data-Visulization
Problem statement:
In this problem, you’re provided with data of different states in JSON
format, you’ve to design a dashboard that has the following
functionalities.
1. On the first page, you have to show all state data.
Key of JSON data will be columns and row should be the
state's data. A sorting feature is to be implemented for the
columns. For exapmle if we click on sort button of any column
like area, population, per capita income, etc the state's data
should be get arranged in ascending or descending order.
2. There should be a feature to select and compare data of 2
states.
3. You have to make a search box in which you write the name
of any state, then all the info related to has to be appeared.
4. There should be feature to show state’s data in graphical
form like piechart, bar graph, etc.
Example: If we click in Population tab populutaion of every
state has to be presneted in any of graphical repersenation.

Instructions on how to set up and run a Streamlit app. The app requires a specific Python environment and a `requirements.txt` file to install the necessary dependencies.

## Prerequisites

Before running the Streamlit app, ensure you have the following prerequisites installed:

- [Python](https://www.python.org/) (version 3.6 or higher)
- [pip](https://pypi.org/project/pip/)
- [virtualenv](https://pypi.org/project/virtualenv/)

## Setup

1. Clone this repository to your local machine:

    ```bash
    git clone <https://github.com/anupkumarmridha/Streamlit-Data-Visulization.git>
    ```

2. Change your working directory to the project folder:

    ```bash
    cd <Streamlit-Data-Visulization>
    ```

3. Create a virtual environment to isolate the project's dependencies. If you don't have virtualenv installed, you can install it using pip:

    ```bash
    pip install virtualenv
    ```

4. Create a virtual environment:

    ```bash
    virtualenv venv
    ```

5. Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

6. Install the required dependencies from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Streamlit App

1. Once the virtual environment is activated and all dependencies are installed, you can run the Streamlit app using the following command:

    ```bash
    streamlit run app.py
    ```

2. This command will start the Streamlit development server, and you will see a message indicating the server is running. It should open a web browser window with your Streamlit app.

3. You can interact with the app through the web browser. To stop the Streamlit app, press `Ctrl+C` in the terminal where it's running.

## Customizing the Streamlit App

The Streamlit app in this repository is a placeholder. You can customize the app by editing the `app.py` file and modifying the content to suit your specific application or data visualization needs.

## Docker Setup

To run this Streamlit app in a Docker container, follow these steps:

1. Build the Docker image. Open a terminal in your project directory and run:

    ```bash
    docker build -t streamlit-app .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8501:8501 streamlit-app
    ```
    
## Additional Information

- Streamlit Documentation: [https://docs.streamlit.io/](https://docs.streamlit.io/)
- For more information on creating Streamlit apps, refer to the Streamlit [official documentation](https://docs.streamlit.io/).

Happy Streamlit app development!
