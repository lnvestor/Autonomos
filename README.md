# Autonomos

![Screenshot 2024-09-10 at 5 31 17 PM](https://github.com/user-attachments/assets/91233f32-5e77-4f3a-80c9-09fc15f2c728)


# 🚀 Celigo Automation Tool

![Celigo Automation](https://placeholder-image-url.com/celigo-automation.png)

## 📚 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

## 🌟 Overview

The Celigo Automation Tool is a powerful Python script designed to streamline and automate various tasks related to Celigo integrations. It provides functionality for extracting integration data, generating screenshots, creating AI-powered descriptions, and producing comprehensive documentation.

## 🎯 Features

- 🔐 Secure login with 2FA support
- 📦 Integration extraction
- 📸 Automated screenshot capture
- 🧠 AI-powered description generation
- 📄 Comprehensive documentation creation
- 🧹 Easy cleanup of generated files

## 🛠 Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: This project requires Python 3.7 or higher. If you don't have Python installed, follow these steps:

  1. Visit the [official Python website](https://www.python.org/downloads/)
  2. Download the latest version for your operating system
  3. Run the installer and follow the installation wizard
  4. Make sure to check the box that says "Add Python to PATH" during installation

- **pip**: pip is the package installer for Python. It usually comes pre-installed with Python. To check if you have pip installed:

  ```
  pip --version
  ```

  If pip is not recognized, you may need to install it separately. Follow the instructions [here](https://pip.pypa.io/en/stable/installation/).

## ⚙️ Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/celigo-automation.git
   ```

2. Navigate to the project directory:
   ```
   cd celigo-automation
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

   If you encounter any issues, try using `pip3` instead of `pip`:
   ```
   pip3 install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root directory
   - Add your Cohere API key:
     ```
     COHERE_API_KEY=your_api_key_here
     ```

## 🚀 Usage

Run the main script:

```
python AppV7.4.py
```

If you're using Python 3 specifically, you might need to use:

```
python3 AppV7.4.py
```

Follow the on-screen prompts to:
1. Log in to your Celigo account
2. Select a project and environment
3. Choose from the available automation options

### 📋 Menu Options

1. 🚀 Automate All (Recommended)
2. 📦 Extract Your Integration
3. 📸 Generate Screenshots
4. 🧠 Generate AI Descriptions
5. 📄 Generate O&M
6. 🧹 Clean All Generated Files
7. 🚪 Exit

## 📁 Project Structure

```
celigo-automation/
│
├── AppV7.4.py            # Main application script
├── AiProcessing.py       # AI processing module
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
│
└── CeligoAI/
    ├── DocumentResources/  # Generated resources
    └── extracted/          # Extracted integration data
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/your-username/celigo-automation/issues).

To contribute to Celigo Automation Tool, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 👤 Author

**Your Name**
- Github: [@Investor](https://github.com/investor)
- LinkedIn: [@IDriss Talainte](https://www.linkedin.com/in/driss-talainte/)

---

🌟 If you find this project helpful, please give it a star on GitHub!
