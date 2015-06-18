### About the authors

<div class="row">
{% for a in site.data.authors %}
  {% assign author = a[1] %}
  <div class="col-sm-4" id="author-#{{a[0]}}">

    <h4 class="name">{{ author.name }}</h4>
    <div class="description">{{ author.description | markdownify }}</div>
  </div>
{% endfor %}
</div>
