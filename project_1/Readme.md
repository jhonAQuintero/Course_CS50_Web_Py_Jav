# WIKI

## Background
Design a **Wikipedia-like** online encyclopedia.

[Wikipedia](https://www.wikipedia.org/) is a free online encyclopedia that consists of a number of encyclopedia entries on various topics.

Each encyclopedia entry can be viewed by visiting that entry’s page. Visiting https://en.wikipedia.org/wiki/HTML, for example, shows the Wikipedia entry for HTML. Notice that the name of the requested page (HTML) is specified in the route /wiki/HTML. Recognize too, that the page’s content must just be HTML that your browser renders.

In practice, it would start to get tedious if every page on Wikipedia had to be written in HTML. Instead, it can be helpful to store encyclopedia entries using a lighter-weight human-friendly markup language. Wikipedia happens to use a markup language called [Wikitext](https://en.wikipedia.org/wiki/Help:Wikitext), but for this project we’ll store encyclopedia entries using a markup language called Markdown.

Read through [GitHub’s Markdown guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) to get an understanding for how Markdown’s syntax works. Pay attention in particular to what Markdown syntax looks like for headings, bold text, links, and lists.

By having one Markdown file represent each encyclopedia entry, we can make our entries more human-friendly to write and edit. When a user views our encyclopedia entry, though, we’ll need to convert that Markdown into HTML before displaying it to the user.

## Getting Started

Download the distribution code from https://cdn.cs50.net/web/2020/spring/projects/1/wiki.zip and unzip it.

## Understanding

In the distribution code is a Django project called `wiki` that contains a single app called `encyclopedia`.

First, open up `encyclopedia/urls.py`, where the URL configuration for this app is defined. Notice that we’ve started you with a single default route that is associated with the `views.index` function.

Next, look at `encyclopedia/util.py`. You won’t need to change anything in this file, but notice that there are three functions that may prove useful for interacting with encyclopedia entries. `list_entries` returns a list of the names of all encyclopedia entries currently saved. save_entry will save a new encyclopedia entry, given its title and some Markdown content. `get_entry` will retrieve an encyclopedia entry by its title, returning its Markdown contents if the entry exists or None if the entry does not exist. Any of the views you write may use these functions to interact with encyclopedia entries.

Each encyclopedia entry will be saved as a Markdown file inside of the `entries/` directory. If you check there now, you’ll see we’ve pre-created a few sample entries. You’re welcome to add more!
