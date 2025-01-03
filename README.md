# Static Site Generator

This tool takes raw markdown files including links and images and converts them into a static website (a mix of HTML and CSS files). Static sites are useful for blogs or other content heavy website applications as they are fast, secure, and easy to host and set up. 

## Table of Contents

1. [Installation]
2. [Usage]
3. [Features]
4. [Contributing]
5. [License]
6. [Contact]

## Installation

To install, you simply need to clone the repository below using the provided commands in a Linux (or WSL) terminal. You will need to have git installed in your system to complete this task.

```bash
# Clone the repository
git clone https://github.com/github-username/repo-name.git

# Navigate into the project directory
cd repo-name
```

## Usage

To use this code you will need to make sure to add your raw markdown files to the content directory. These can be nested inside folders as page generation is handled recursively. 

After adding your content to the `content` directory you will also need to modify the paths in the code to match what you see in your terminal. You can check the path you are in using the `pwd` command.

The file paths that need to be modified can be found in the file named, `main.py`.

Path names that must be changed: 
- dir_path_content = "Path/to/Static-Site-Generator/content"
- template_path = "Path/to/Static-Site-Generator/template.html"
- dest_dir_path = "Path/to/Static-Site-Generator/public"
- stat_path = "Path/to/Static-Site-Generator/static"
- pub_path = "Path/to/Static-Site-Generator/public"

To start generating a site you can run the following command from the root of the project. 

```bash
# ./main.sh
```
## Features

- Converts raw Markdown files to HTML and then serves the HTML files as a static site. 
- The current iteration can handles most common markdown formatting options including code blocks, links, and images. 
- Things I would like to try adding in the future: 
	- **Markdown Support**: Allow users to write content in Markdown format, which your generator processes into HTML. This grants simple and efficient content creation.
	- **Template Engine**: Implement a templating system to separate content from style, enabling users to apply a consistent look across pages using templates.
	- **Content Management**: Add support for managing pages and posts, perhaps by organizing files in a manner that users can intuitively navigate and edit.
	- **Themes and Styling**: Enable customizable themes or styles, allowing users to easily switch and configure appearances without altering content.
	- **Live Preview**: Introduce a local server with auto-reload capabilities, letting users see changes in real-time as they edit content and design.
	- **Plugins and Extensions**: Offer a plugin architecture for users to extend functionalities, such as analytics, search, or SEO enhancements.
	- **Deployment Tools**: Integrate with hosting platforms or provide scripts for deploying sites easily and efficiently.
	- **Image Optimization**: Automatically optimize images upon generation, ensuring quicker load times on the web.
	- **RSS or Atom Feeds**: Generate feeds for content, like blog posts, so users can keep their audience updated through feed readers.
