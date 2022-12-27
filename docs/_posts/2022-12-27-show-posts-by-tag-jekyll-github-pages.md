---
layout: post
title:  "Show posts by tag on Jekyll site hosted with GitHub Pages"
tags: jekyll
render_with_liquid: false
---
As the number of posts on this site have grown,
I thought it might be useful to be able to view all
the posts with a certain tag e.g. [jekyll](/tag/jekyll).
This capability does not come out of the box 
with Minima, the theme I am using,
however it can be added with a little custom development. 

P.s. I assume the steps should work 
even if you are not using Minima, albeit with minor adjustments
e.g. the CSS classes I use are Minima specific.

The guide below is an extension of the work by
[Long Qian](https://longqian.me/2017/02/09/github-jekyll-tag/) and
[Jason E. Miller](http://www.jasonemiller.org/2020/12/23/tagging-posts-in-jekyll-minima.html).
All the steps are listed here for completeness i.e.
even those that are unchanged from the original guides.
The major ideas are the same with the following adaptations:

1. Parts of the code are refactored for better understandability.
2. Steps are added to automate generation of tag pages at deploy time. Since Jekyll sites compile into static resources (e.g. HTML/CSS), pages for each tag must be pre-built. Maintaining pages manually would be tedious as tags might change frequently, therefore we generate these pages at deploy time using GitHub Actions.

#### Display tag with hyperlink

Let's say we want to display tags on each of our posts.
We need to customize our post layout.
To be able to customize the post layout,
we need to create a copy
of [`/_layouts/post.html`](https://github.com/jekyll/minima/blob/master/_layouts/post.html) into our local 
repository.

Next we add the following snippet where we want the tags to show,
e.g. below date and author.

```
{%- if page.tags.size > 0 -%}
    {% for tag in page.tags %}
        <a href="/tag/{{ page.tag }}"><code>{{ page.tag }}</code></a>&nbsp;
    {% endfor %}
{%- endif -%}
```

Deploy this change to verify the tag appears as expected.
You can modify the styling as you like.
Note that for now the hyperlink will not work as we have not generated
the pages under `tag/` directory.

#### Add a layout to show posts by tag

Create `_layouts/posts-by-tag.html` with the following content.

```
---
layout: default
---
<div class="post">
    <h1>Tag: {{ page.tag }}</h1>
    {% assign posts = site.posts | where_exp:"post","post.tags contains page.tag"  %}
    <ul class="post-list">
        {%- for post in posts -%}
        <li>
            <span class="post-meta">{{ post.date | date: site.minima.date_format }}</span>
            <h3>
                <a class="post-link" href="{{ post.url | relative_url }}">
                    {{ post.title | escape }}
                </a>
            </h3>
        </li>
        {%- endfor -%}
    </ul>
</div>
```

#### Generate tag pages

Tag pages are generated using the layout created in the previous step.
Add the following `tag-page.template` to your repository.

```
---
layout: posts-by-tag
title: "Tag: {tag}"
tag: {tag}
robots: noindex
---
```

This template will be used to generate `tag/{tag}.md`
for each of the tags used in our site.

Next, we add the Python script `tag-pages-generator.py` 
to our repository which generates
a page for each tag under `tag/` directory, e.g. `tag/jekyll.md`.
Download the source from [here](https://github.com/lamak-qaizar/lamak-qaizar.github.io/blob/master/docs/tag-pages-generator.py).

The [original Python script](https://github.com/qian256/qian256.github.io/blob/master/tag_generator.py)
used to delete existing pages under
`tag/` directory since the directory was expected
to be checked in to the repository after executing the script.
We will generate `tag/` directory and its contents
as part of the build pipeline so this step was unnecessary
and has been removed from the updated script.

#### Generate tag pages as part of pipeline

Here we'll add a custom build step to generate tag pages
using the generator in the previous step as part of our deployment pipeline.
Jekyll sites on GitHub Pages are deployed using GitHub Actions,
however the default workflow is not modifiable,
i.e. we cannot add a custom build step.

To have a modifiable workflow,
we first need to change the following setting of our repository.

1. Settings > Pages > Build and deployment
2. Set 'Source' to `GitHub Actions`

This will generate `.github/workflows/jekyll-gh-pages.yml`.
Since my Jekyll sources are not at root, but under `/docs`,
I had to change the Source property of `actions/jekyll-build-pages` step
from `./` to `./docs/`. All the other settings worked as default for me.

Run the pipeline to test before proceeding.

Now add the following steps after `actions/checkout`:

```yaml
  - name: setup python
    uses: actions/setup-python@v4
    with:
      python-version: 3.8
  - name: execute py script
    run: (cd docs && python tag-pages-generator.py)
```

Note that I am `cd`ing into `/docs` before running the python script
(putting the command in parentheses `(...)` launches a sub-process so that
the change-directory command only has temporary effect).
If your Jekyll sources are at root, simply put `run: python tag-pages-generator.py`.

For a full `.github/workflows/jekyll-gh-pages.yml`,
you may reference it from the 
[source](https://github.com/lamak-qaizar/lamak-qaizar.github.io/blob/master/.github/workflows/jekyll-gh-pages.yml)
of this site.

#### And that's it!

Run the pipeline to test that everything works fine.
Thank you to
[Long Qian](https://longqian.me/) and
[Jason E. Miller](http://www.jasonemiller.org/)


