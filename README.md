# 🛠️ DevToolBox

<p align="center">
  <strong>A collection of simple, fast, privacy-friendly developer tools — all in one place.</strong>
</p>

<p align="center">
  <a href="https://github.com/mehulikhanra904-prog/devtoolbox-open-source">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?logo=github" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/React-18+-61DAFB?logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Vite-Fast-646CFF?logo=vite&logoColor=white" alt="Vite">
  <img src="https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-success" alt="Open Source">
</p>

---

## 📌 About DevToolBox

**DevToolBox** is an open-source web-based collection of useful developer utilities designed to make common development tasks faster and easier.

Instead of visiting different websites for different small tasks, developers can use a single toolbox containing utilities for:

- JSON formatting
- JSON minification
- Password generation
- Base64 encoding and decoding
- URL encoding and decoding
- Unix timestamp conversion
- And more tools planned through community contributions

The project is designed with a strong focus on:

- ⚡ Simplicity
- 🔒 Privacy
- 📱 Responsive design
- 🧩 Easy extensibility
- 🌐 Browser-based processing
- 🤝 Open-source collaboration

---

# ✨ Features

## 🔹 1. JSON Formatter

Format and beautify JSON data into an easy-to-read structure.

### Useful for:

- Debugging API responses
- Reading configuration files
- Working with REST APIs
- Understanding large JSON objects
- Cleaning unformatted JSON

### Example

Input:

```json
{"name":"Mehuli","skills":["C++","JavaScript","React"]}

Formatted Output

{
  "name": "Mehuli",
  "skills": [
    "C++",
    "JavaScript",
    "React"
  ]
}
🔹 2. JSON Minifier

Convert formatted JSON into a compact version.

Useful for:
Reducing unnecessary whitespace
Preparing JSON for transmission
Working with APIs
Testing compact JSON data

Example:

{
  "name": "Mehuli",
  "role": "Developer"
}

becomes:

{"name":"Mehuli","role":"Developer"}
🔹 3. Password Generator

Generate random passwords directly in the browser.

Features
Adjustable password length
Supports lengths from 6 to 40 characters
Fast generation
No server-side password processing

Useful when creating:

Strong account passwords
Temporary credentials
Development/testing credentials
Random secret values

⚠️ Generated passwords should be stored securely when used for real accounts.

🔹 4. Base64 Encoder

Convert text into Base64 format.

Example:

Hello World

becomes a Base64 representation.

Useful for:

API development
Data transfer
Debugging
Encoding text
Working with web applications
🔹 5. Base64 Decoder

Decode Base64 data back into readable text.

Example:

SGVsbG8gV29ybGQ=

can be decoded back to:

Hello World
🔹 6. URL Encoder

Encode special characters so text can safely be used inside URLs.

For example:

hello world

can be converted into URL-safe encoded text.

Useful when working with:

Query parameters
REST APIs
Search URLs
Web applications
🔹 7. URL Decoder

Decode URL-encoded strings back into readable text.

Useful when debugging:

Query strings
API requests
Redirect URLs
Browser-generated URLs
🔹 8. Unix Timestamp Converter

Convert Unix timestamps into human-readable dates and times.

Unix timestamps represent time using the number of seconds elapsed since:

January 1, 1970 00:00:00 UTC

This tool is useful for:

API development
Backend development
Database debugging
Authentication systems
Logs
JWT-related development
🎨 UI Features
🌙 Dark / Light Mode

DevToolBox supports both:

☀️ Light Mode
🌙 Dark Mode

This makes the toolbox comfortable to use in different environments.

📱 Responsive Design

The interface is designed to work across:

💻 Desktop
💻 Laptop
📱 Mobile
📱 Tablet

The goal is to make developer utilities accessible even when working from a mobile device.

📋 Copy Buttons

Tools provide convenient copy functionality wherever applicable.

Instead of manually selecting generated output, users can copy results directly.

🔒 Privacy First

Privacy is an important part of DevToolBox.

Most operations are performed directly inside the user's browser.

DevToolBox aims to avoid:
❌ Unnecessary account creation
❌ Sending utility input to external servers
❌ Unnecessary data collection
❌ Tracking user input

For example, when formatting JSON, the JSON can be processed directly in the browser.

This makes DevToolBox suitable for working with development data that users may not want to upload to random online tools.

Always verify the implementation of a particular tool before processing highly sensitive information.

⚡ Why DevToolBox?

Developers frequently need small utilities during development.

For example:

Need to format JSON?
        ↓
Open a JSON formatter

Need Base64 decoding?
        ↓
Open another website

Need URL encoding?
        ↓
Open another website

Need a timestamp conversion?
        ↓
Search again

DevToolBox brings these common utilities together:

                 DEVTOOLBOX
                      │
        ┌─────────────┼─────────────┐
        │             │             │
       JSON          Encoding      Time
        │             │             │
   Formatter      Base64        Timestamp
   Minifier       URL Encode
                  URL Decode
        │
    Password
    Generator

The goal is to provide a single, clean developer workspace.

🧰 Current Tools
Tool	Status	Description
JSON Formatter	✅ Available	Beautify JSON
JSON Minifier	✅ Available	Minify JSON
Password Generator	✅ Available	Generate random passwords
Base64 Encoder	✅ Available	Encode text to Base64
Base64 Decoder	✅ Available	Decode Base64 text
URL Encoder	✅ Available	Encode URL text
URL Decoder	✅ Available	Decode URL text
Unix Timestamp Converter	✅ Available	Convert Unix timestamps
Dark / Light Mode	✅ Available	Switch UI themes
Responsive UI	✅ Available	Desktop and mobile friendly
Copy Actions	✅ Available	Quickly copy generated output
🛠️ Tech Stack

DevToolBox is built using modern frontend technologies.

Frontend
⚛️ React
⚡ Vite
🟨 JavaScript
🎨 CSS
Development Tools
Git
GitHub
VS Code
npm
Automation
GitHub Actions
📂 Project Structure
devtoolbox-open-source/
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── ...
│   │
│   ├── workflows/
│   │   └── ci.yml
│   │
│   └── pull_request_template.md
│
├── public/
│   └── ...
│
├── src/
│   ├── App.jsx
│   ├── App.css
│   └── ...
│
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── package.json
├── README.md
└── ...
🚀 Getting Started
1. Clone the repository
git clone https://github.com/mehulikhanra904-prog/devtoolbox-open-source.git
2. Navigate into the project
cd devtoolbox-open-source
3. Install dependencies
npm install
4. Start the development server
npm run dev

Vite will provide a local development URL.

Open that URL in your browser.

🧪 Build the Project

To create a production build:

npm run build
🔍 Lint the Project

Run:

npm run lint

This helps identify code-quality and JavaScript issues before submitting changes.

🤝 Contributing

DevToolBox is an open-source project and contributions are welcome.

You can contribute by:

🐛 Fixing bugs
✨ Adding new tools
🎨 Improving the UI
📱 Improving mobile responsiveness
⚡ Improving performance
🧪 Adding tests
📚 Improving documentation
🔧 Refactoring code
💡 Suggesting new features
📝 Contribution Workflow
Step 1 — Fork the repository

Create your own fork of the DevToolBox repository.

Step 2 — Clone your fork
git clone https://github.com/YOUR-USERNAME/devtoolbox-open-source.git
Step 3 — Create a new branch
git checkout -b feature/your-feature-name

For example:

git checkout -b feature/uuid-generator
Step 4 — Make your changes

Implement your feature or bug fix.

Step 5 — Test your changes

Run:

npm run build

and, if available:

npm run lint
Step 6 — Commit
git add .
git commit -m "feat: add your feature"
Step 7 — Push
git push origin feature/your-feature-name
Step 8 — Open a Pull Request

Create a Pull Request against the main DevToolBox repository.

Please describe:

What you changed
Why you changed it
How you tested it
Any screenshots if the UI was changed
🐛 Reporting Bugs

Found a bug?

Please create a GitHub Issue and include:

Description

Explain what went wrong.

Steps to reproduce
1. Open DevToolBox
2. Select the affected tool
3. Enter the input
4. Click the relevant button
5. Observe the problem
Expected behavior

Explain what should have happened.

Actual behavior

Explain what happened instead.

Environment

Include information such as:

Browser
Operating system
Device
Relevant console errors
💡 Feature Requests

Have an idea for a new developer utility?

Open a feature request and explain:

What the tool should do
Why developers would find it useful
Example input/output
Any UI suggestions
🗺️ Roadmap

DevToolBox is intended to grow through community contributions.

Potential future tools include:

🔐 Security & Authentication
UUID Generator
JWT Decoder
Hash Generator
Secure token generator
🎨 Developer Utilities
HEX ↔ RGB ↔ HSL Color Converter
Regex Tester
Markdown Previewer
HTML Formatter
CSS Formatter
📱 Developer Experience
Improved mobile sidebar
Better mobile navigation
Keyboard shortcuts
Improved accessibility
🔧 Web Utilities
QR Code Generator
Cron Expression Helper
HTTP utilities
Query-string utilities
🧪 Quality Improvements
Automated tests
More unit tests
Better error handling
Improved validation
Performance optimization

The roadmap is community-driven and individual features may change as the project evolves.

🌱 Good First Contributions

New contributors are welcome.

Some beginner-friendly contribution ideas include:

Improving documentation
Fixing UI spacing
Improving responsive design
Adding copy buttons
Improving error messages
Adding small utility functions
Adding tests
Improving accessibility
Fixing minor bugs

You don't need to be an expert to contribute.

🏷️ Suggested Issue Labels

The repository can use labels such as:

good first issue
help wanted
bug
enhancement
documentation
UI/UX
frontend
testing
performance

These labels make it easier for contributors to find suitable tasks.

🔄 Continuous Integration

DevToolBox uses GitHub Actions to help automatically check changes.

The CI workflow can verify that the project:

Installs correctly
Builds successfully
Passes configured checks

This helps prevent broken code from being merged.

📜 Code of Conduct

All contributors are expected to maintain a respectful and welcoming environment.

Please read:

CODE_OF_CONDUCT.md

before contributing.

📄 License

This project is open source and distributed under the license included in:

LICENSE

Please review the license before redistributing or reusing the project.

👩‍💻 Maintainer

Mehuli Khanra

GitHub:

https://github.com/mehulikhanra904-prog

Repository:

https://github.com/mehulikhanra904-prog/devtoolbox-open-source

⭐ Support the Project

If you find DevToolBox useful:

⭐ Star the repository

🍴 Fork the project

🐛 Report bugs

💡 Suggest features

🤝 Contribute through Pull Requests

📢 Share the project with other developers

Every contribution helps the project grow.

