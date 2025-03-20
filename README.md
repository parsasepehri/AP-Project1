# Instagram CLI Clone

## Overview
This project is a **Python-based command-line application** that simulates core functionalities of Instagram, enabling users to create accounts, interact with posts and stories, chat with others, and manage their profiles.

## Features
- **User Authentication**: Sign up, log in, and manage user sessions.
- **Home Feed**:
  - View posts from followed users.
  - Like, comment, and save posts.
  - Watch and like stories.
- **Search & Explore**:
  - Search for users and view their profiles.
  - Follow/unfollow users.
- **Messaging**:
  - Send direct messages and create group chats.
- **Profile Management**:
  - Edit user details and privacy settings.
  - View personal posts and saved posts.
  - Manage followers and blocked users.
- **Extras**:
  - Custom CLI display with `rich` library for better UI.
  - Structured code with error handling and PEP 8 compliance.

## Prerequisites
Ensure you have **Python 3.11 or later** installed. Set up a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install dependencies:
```sh
pip install -r requirements.txt
```

## Installation & Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Instagram-CLI.git
   cd Instagram-CLI
   ```
2. **Run the main script:**
   ```sh
   python main.py
   ```
3. Follow on-screen instructions to register or log in.

## Contribution Guide
- **Follow coding standards**: Use PEP 8, add docstrings, and use type hints.
- **Branching strategy**:
  - `main`: Stable version of the project.
  - `develop`: Active development branch where features are merged.
  - `feature/feature-name`: New features should be developed in separate feature branches.
  - `bugfix/fix-description`: For fixing bugs found in the project.
  - `hotfix/urgent-fix`: For critical issues that need immediate attention.
- **Regular commits**: Maintain a structured commit history.
- **Pull Requests**: Ensure all changes are reviewed before merging into `develop` or `main`.

## License
This project is licensed under [MIT License](LICENSE).

## Contact
For inquiries, open an issue or contact [your_email@example.com].

