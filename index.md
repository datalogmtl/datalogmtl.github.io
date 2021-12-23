---
layout: page
title: MATHAI4ED
subtitle: "Math AI for Education: Bridging the Gap Between Research and Smart Education"
# venue: "NeurIPS Workshop 2021, December 13, 2021"
use-site-title: true
---
<div class="venue" style="font-size: 27px; display: block; font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 300; color: #404040; text-align: center;">
  (NeurIPS 2021 Workshop: <a href="https://neurips.cc/virtual/2021/workshop/21828" target="_blank">Website</a>)
</div>



<div class="sharethis-inline-share-buttons"></div>
<meta name="thumbnail" content="./img/neurips-logo-new.jpg" />


# Overview

Mathematical reasoning is a unique aspect of human intelligence and a fundamental building block for scientific and intellectual pursuits. However, learning mathematics is often a challenging human endeavorthat relies on expert instructors to create, teach and evaluate mathematical material.  From an educational perspective, AI systems that aid in this process offer increased inclusion and accessibility, efficiency, and understanding of mathematics.  Moreover, building systems capable of understanding, creating, and using mathematics offers a unique setting for studying reasoning in AI. This workshop will investigate the *intersection* of mathematics education and AI, including applications to:
- **Teaching**: Intelligent tutoring systems that effectively assist students in math learning.
- **Evaluation**: AI-assisted grading systems like Gradescope and personalized testing platforms like IXL.
- **Assisting**: Symbolic mathematics tools such as Mathematica and Maple in advanced math education.

These applications require key advances in artificial intelligence and machine learning areas such as:
- **Interpretability**: Opening up the “black box” and providing explainable and interpretable AI.
- **Reasoning**: Informal and formal reasoning agents that can communicate and interact with humans.
- **Core methods**: Multimodal and neuro-symbolic approaches in mathematical domains.

Enabling these applications requires not only innovations in math AI research, but also a better understand-ing of the challenges in real-world education scenarios.  Hence, we will bring together a group of experts from a diverse set of backgrounds, institutions, and disciplines to drive progress on these and other real-world education scenarios, and to discuss the promise and challenge of integrating mathematical AI into education. Discussion topics include but are not limited to:
- **Accessibility**: How can AI most effectively aid mathematical education for a diversity of backgrounds?
- **Applications**: Which near- and long-term applications of AI in math education are most impactful?
- **Approaches**: Which research advances are necessary for enabling these applications?
- **Looking forward**: What is the future of mathematical education and research?

<!-- | ------------- |:-------------:|
| **Submission** | October 09, 2020 (midnight Pacific Time) |
| **Notification** | October 30, 2020 |
| **Submission link**| [https://cmt3.research.microsoft.com/KR2ML2020](https://cmt3.research.microsoft.com/KR2ML2020) -->

<!--* Thank you Amazon for sponsoring a best paper award!
* The 3 best papers will be presented in talks at the workshop! 
* <a href="schedule">The schedule is online now!</a> 
* <a href="papers">List of accepted papers available!</a> -->
<!--* **NEW** Updates to existing submissions possible until October 12 (11:59pm Pacific Time) <br>New submissions close on October 09 (11:59pm Pacific Time)-->


<hr>

# Speakers & Panelists
<div class="container" style="margin-top: 20px;margin-bottom: 0px;">
  <div class="row">
    {% for p in site.data.speakers %}
    {% if forloop.index<=5 %}
    {% capture id %}{{ p[0] }}{% endcapture %}
    {% include profile.html p=p %}
    {% endif %}
    {% endfor %}
  </div>
  <div class="row">
    {% for p in site.data.speakers %}
    {% capture id %}{{ p[0] }}{% endcapture %}
    {% if forloop.index>5 and forloop.index<=10%}
    {% include profile.html p=p %}
    {% endif %}
    {% endfor %}
  </div>
  <div class="row">
    {% for p in site.data.speakers %}
    {% capture id %}{{ p[0] }}{% endcapture %}
    {% if forloop.index>10%}
    {% include profile.html p=p %}
    {% endif %}
    {% endfor %}
  </div>
<a href="speakers">More Info</a>
</div>

<hr>

# Organizers

<!-- prettier-ignore -->
<div class="container" style="margin-top: 25px;margin-bottom: 40px;">
  <div class="row">
    {% for p in site.data.organizers %}
    {% if forloop.index<=3 %}
    {% capture id %}{{ p[0] }}{% endcapture %}
    {% include profile.html p=p %}
    {% endif %}
    {% endfor %}
  </div>
  <div class="row">
    {% for p in site.data.organizers %}
    {% capture id %}{{ p[0] }}{% endcapture %}
    {% if forloop.index>3 and forloop.index<=6%}
    {% include profile.html p=p %}
    {% endif %}
    {% endfor %}
  </div>
</div>
<hr>

# Program Committee
<div class="container">
  <ul class="list-group list-group-flush">
    {% for p in site.data.pc.people %}
      <li class="list-group-item col-xs-6 col-sm-4 col-md-3">{{ p }}</li>
    {% endfor %}
  </ul>
</div>
<hr>

<!-- prettier-ignore -->
# Related Venues

<div class="container" style="margin-bottom: 10px;"></div>

- [ICLR'21 workshop on The Role of Mathematical Reasoning in General Artificial Intelligence](https://mathai-iclr.github.io/cfp/)
- [NeurIPS'20 Workshop on KR2ML - Knowledge Representation & Reasoning Meets Machine Learning](https://kr2ml.github.io/2020)
- [NeurIPS'20 workshop on Advances and Opportunities: Machine Learning for Education](https://www.ml4ed.org/)
- [ICML'20 workshop on Bridge  Between Perception and Reasoning: Graph Neural Networks & Beyond](https://logicalreasoninggnn.github.io)


<div class="container" style="margin-bottom: 10px;"></div>

<hr>

Contact: <mathai4ed.neurips2021@gmail.com>.
