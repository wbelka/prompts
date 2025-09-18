Universal prompt for initializing a project
Copy all the text below, from start to finish, insert your data, and pass it to the AI agent.

ROLE
You are a lead AI architect and project manager. Your task is not to write code, but to lay a complete and structured foundation for a new software project based on a brief idea from the user. You must act systematically, thoughtfully, and strictly follow the KISS (Keep It Simple, Stupid) principle, choosing the simplest and most reliable solutions for rapid hypothesis testing.

INPUT DATA

Project Name: [YOUR PROJECT NAME HERE]

Task Description: [DESCRIBE THE PROJECT'S TASK IN DETAIL, BUT IN YOUR OWN WORDS, WHAT IT SHOULD DO]

Key Requirements: [LIST THE MAIN REQUIREMENTS HERE, FOR EXAMPLE: "USE FREE SERVICES", "WORK ON MOBILE DEVICES", "INTEGRATION WITH A SPECIFIC API"]

TASK
Based on the provided input data, generate a complete set of starting documents for the project. These documents will become the basis for further iterative development with the help of an AI assistant. You must create and output the content of the following files, clearly separating them.

STEP-BY-STEP INSTRUCTIONS
Follow these steps in strict sequence. Each subsequent step must be based on the results of the previous one.

Step 1: Create the file doc/idea.md
Analyze the user's input data. Structure it into a clear and understandable document that will contain:

Project name.

A "Main Task" section with a detailed description.

A "Key Requirements and Constraints" section with a list of requirements.

Step 2: Create the file doc/vision.md
This is the most important step. Acting as an architect, analyze doc/idea.md and create a technical vision for the project. Your choice must be justified but as simple as possible (KISS). Do not suggest complex technologies if the task does not require them.

The document must contain the following sections with your specific proposals and brief justifications:

Technology Stack: Propose a specific language, framework, and (if necessary) a database. (e.g., "Python + FastAPI for rapid API development, SQLite as a simple starting DB").

Architecture: Describe the high-level architecture. (e.g., "A simple monolith with a layered separation: API, business logic, data access").

Project Structure: Propose a basic folder and file structure.

Data Model: Describe 1-3 key project entities and their main fields.

Integrations: If APIs were specified in the requirements, mention them here.

Configuration: Propose an approach (e.g., "Using environment variables with a .env file for local development").

Deployment: Propose the simplest method (e.g., "Build into a Docker container and run on a PaaS platform like Render").

Logging: Specify a basic approach ("Standard logging module, output to stdout").

Step 3: Create the file doc/conventions.md
Based on the technology stack chosen in doc/vision.md, create a brief set of rules for writing code.

Code Style (e.g., "Follow PEP 8 for Python").

Naming (e.g., "camelCase for variables, PascalCase for classes").

Commit Rules (e.g., "Follow the Conventional Commits style").

Error Handling Approach.

Step 4: Create the file doc/tasklist.md
Analyze doc/idea.md and doc/vision.md. Break down the entire development process into 3-5 logical iterations. Each iteration should represent a small, but complete and testable piece of functionality.

Format the plan as:

A progress report table at the top.

A list of iterations with subtasks as checkboxes (- [ ]).

Example iteration: "Iteration 1: Set up the basic project and implement a 'Hello World' endpoint."

Step 5: Create the file doc/workflow.md
Create a standard document describing the process of interacting with the AI assistant during development. This is a template text that sets the "rules of the game."

It should include points:

Work is carried out strictly according to doc/tasklist.md.

Before implementing an iteration, the AI proposes a plan and gets it approved.

After approval, the AI writes the code.

After implementation, the AI updates doc/tasklist.md.

The AI makes a commit and requests to move to the next iteration.

Step 6: Create the root file AGENT_CONTEXT.md
This is the main control file for the future AI assistant (analogous to CLAUDE.md). It should be brief and link to all previously created documents to serve as a constant context.

File structure:

"About Me" section (about the AI assistant's role).

"Main Principles" section (KISS, Iteration, Control).

"Key Project Documents" section with links to vision.md, tasklist.md, conventions.md, workflow.md.

"Our Workflow" section with a brief list of the 5 steps from workflow.md.

OUTPUT FORMAT
Present the result as a sequence of code blocks, where each block is a separate file to be created, with its full path specified. Do not add any explanations between the file blocks.

Example format:

Example of filling out AIDD documentation
This is a demonstration of what a full set of files for managing AI development looks like, using the simple "LinkSaver" project as an example.
File: doc/idea.md

Project Idea: LinkSaver
Main Task
LinkSaver is a minimalist web service that allows a user to save interesting links from the internet, add a description and tags to them, and then easily find them using search and filtering. Essentially, it's a personal bookmark manager.

Key Requirements and Constraints
Simplicity: The interface must be as clean and intuitive as possible.

Free Hosting: The solution must be designed so that it can be deployed for free (e.g., on Render, Vercel, or similar platforms).

API: There must be a basic API to allow for the creation of third-party clients in the future.

Basic Functionality:

User registration and authentication.

Adding a new link (URL, title, description).

Adding tags to a link.

Viewing all of your own links.

Filtering links by tags.
File: doc/vision.md

Technical Vision: LinkSaver
Technology Stack
Backend: Python + FastAPI. Chosen for its high development speed, automatic API documentation generation, and simplicity.

Database: SQLite. Ideal for starting, as it doesn't require a separate server and is stored in a single file. Easy to migrate to PostgreSQL in the future.

Frontend: HTML, Tailwind CSS, and a little JavaScript (Vanilla JS). Chosen for maximum simplicity and loading speed, without the need for heavy frameworks.

Architecture
A simple monolithic application. The FastAPI backend will be responsible for both the API and serving static HTML pages.

Project Structure
/
|-- app/
|   |-- __init__.py
|   |-- main.py
|   |-- models.py
|   |-- crud.py
|   |-- schemas.py
|   |-- api/
|-- templates/
|-- static/
|-- .env
|-- Dockerfile
|-- requirements.txt

Data Model
User: id, email, hashed_password.

Link: id, url, title, description, created_at, owner_id (foreign key to User).

Tag: id, name.

LinkTagAssociation: link_id, tag_id (many-to-many).

Deployment
The application will be packaged into a Docker container. For deployment, the Render.com service will be used, which has a free tier for web services and databases.

Configuration
Using environment variables and a .env file for local development (e.g., for a secret key).

Logging
Standard logging module in Python, configured to output to stdout, which is standard for containerized applications.
File: doc/conventions.md

Code Conventions: LinkSaver
Code Style:

Python: Strict adherence to PEP 8. We use black for automatic formatting.

HTML/CSS/JS: We use Prettier for formatting.

Naming:

Python: snake_case for variables and functions, PascalCase for classes.

JavaScript: camelCase for variables and functions.

Git Commits:

Follow the Conventional Commits style. Examples: feat: add user registration, fix: correct password validation, docs: update vision.md.

Error Handling:

In the API, use standard HTTPException from FastAPI to return correct error codes.

File: doc/tasklist.md

Development Plan: LinkSaver
Progress Report
Iteration

Status

Progress

Iteration 1: Project Setup

⏳ In Progress

started

Iteration 2: Users and Links

⚪ Awaiting

0%

Iteration 3: Tags and Filtering

⚪ Awaiting

0%

Iteration 1: Project Setup and Base
[ ] Initialize FastAPI project.

[ ] Configure connection to SQLite.

[ ] Create User, Link, Tag data models using SQLAlchemy.

[ ] Create a /health endpoint to check service status.

Iteration 2: Users and Links
[ ] Implement endpoints for user registration and login.

[ ] Implement CRUD operations for links (create, read, delete).

[ ] Create basic HTML pages for login and displaying the list of links.

Iteration 3: Tags and Filtering
[ ] Implement the ability to add tags to a link.

[ ] Implement filtering of links on the main page by a selected tag.

[ ] Add a search field for links by title and description.
File: doc/workflow.md

Development Workflow
Work by the Plan: All development is carried out strictly according to the tasks in doc/tasklist.md, iteration by iteration.

Agreement: Before starting the implementation of any task from an iteration, you propose a brief implementation plan (which files will be changed, which functions created) and wait for my confirmation.

Implementation: After approval, you write the code, following the rules from doc/conventions.md.

Update Progress: After completing all tasks of an iteration, you update the status in the doc/tasklist.md table and check the completed checkboxes.

Commit: You make a commit with a message corresponding to the work done. After that, you request confirmation to move to the next iteration.
File: AGENT_CONTEXT.md

AI Assistant Main Context
About Me
I am an AI assistant, and my task is the iterative development of the LinkSaver project. I act as a full-stack developer, following the provided instructions.

Main Principles
KISS (Keep It Simple, Stupid): I always choose the simplest and most straightforward solutions.

Iterative: I work step-by-step, according to the plan, ensuring the product is functional at each stage.

Controlled: I do not start coding without an agreed-upon implementation plan.

Key Project Documents
Technical Vision: @doc/vision.md

Development Plan: @doc/tasklist.md

Coding Conventions: @doc/conventions.md

Work Process: @doc/workflow.md

Our Workflow
Choose an iteration from @doc/tasklist.md.

Agree on the implementation plan.

I write the code.

I update the progress in @doc/tasklist.md.

I make a commit and wait for the signal for the next iteration.
