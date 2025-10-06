I am actually new here, and you should know that, 

---------------------------------------------------

Jinja sintax can't commented using HTML comment, so it's better to remove the code.
Btw this code purpose is to call component inside components/* directory

{% from "components/card.html" import card %}

That code should be place inside index.html, just like this

{% extends "base.html" %}
{% from "components/card.html" import card %}

---------------------------------------------------