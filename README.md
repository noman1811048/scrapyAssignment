# Trip.com Scraper

This project is a web scraper built using Scrapy to gather property information from Trip.com. It stores the data into a PostgreSQL database using SQLAlchemy. The scraper automatically creates the necessary tables in the database, downloads images to a local directory, and stores references to these images in the database.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Clone the Repository](#clone-the-repository)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Configure Database Credentials](#configure-database-credentials)
  - [Ensure PostgreSQL is Running](#ensure-postgresql-is-running)
- [Running the Crawler](#running-the-crawler)
- [Project Structure](#project-structure)
- [License](#license)

## Features

1. **Scrapy Spider**: Utilizes Scrapy to scrape property data from Trip.com.
2. **PostgreSQL Storage**: Stores property data in a PostgreSQL database using SQLAlchemy.
3. **Automatic Table Creation**: Automatically creates database tables.
4. **Image Handling**: Downloads images to a local directory and stores file paths in the database.

## Prerequisites

- Python 3.x
- PostgreSQL installed and running
- Virtual environment (recommended)

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/noman1811048/scrapyAssignment
   cd scrapyAssignment

   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start a Scrapy Project:**

   ```bash
   scrapy startproject hotels_crawler
   cd hotels_crawler
   ```

5. **Configure Database Credentials:**

   Create a config.py file in the root directory and add your PostgreSQL credentials:

   ```python
   # config.py
   DB_USERNAME='your_username'
   DB_PASSWORD='your_password'
   DB_HOST='localhost'
   DB_PORT='PORT'
   DB_NAME='DATABASE'
   ```

6. **Ensure PostgreSQL is Running:**

   Make sure your PostgreSQL server is running and the specified database exists. You can create a database using:

   ```bash
   psql -U your_username
   CREATE DATABASE Database_name;
   ```

### Running the Application

To run the spider and scrape data, use the following command:

```bash
scrapy crawl hotel_crawler
```

## Project Structure

```
.
scrapyAssignment/
│
├── hotels_crawler/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   ├── models.py
│   ├── database.py
│   └── spiders/
│       └── hotels_crawler.py
├── images/                  # Directory where images are stored
├── config.py                # Python configuration file (optional)
├── requirements.txt         # List of project dependencies
└── README.md                # Project documentation


```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Key Points

- **Repository URL**: Make sure to replace `https://github.com/yourusername/trip-scraper.git` with the actual URL of your repository.
- **Environment Variables**: Explain how to use `.env` or `config.py` for database configuration, allowing users flexibility based on their preferences.
- **Scraping Ethics**: Highlight the importance of ethical web scraping practices to avoid legal issues.
- **Customization**: Users may need to update the spider's URL and CSS selectors to match the structure of Trip.com for specific data extraction needs.

This README file provides a comprehensive guide for setting up and running your Scrapy project, ensuring users have all the necessary information in one place.
