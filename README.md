# mini-ui-framework
A tiny UI framework in pure Python: components as element trees, HTML renderer, state, and click events. Includes a Counter demo. No JavaScript, standard library only.
## AI Usage Disclosure

I used an AI assistant (Claude by Anthropic) while working on this project.

**How AI was used:**
- To discuss and choose a simple architecture (Element tree, renderer, App with
  state, small HTTP server).
- To generate the first version of the code and the explanations of each file.
- To prepare interview-style questions for me to practice.

**What I did myself:**
- Set up the project, ran it, and tested the Counter (+ and - buttons).
- Read through every file and learned how the click flow works:
  click -> POST request -> handler -> set_state -> re-render -> redirect -> new page.
- Prepared to explain the design choices and limitations (full page reload,
  shared state) in my own words.

I chose a deliberately small design that I can fully understand and explain,
rather than a complex one.
