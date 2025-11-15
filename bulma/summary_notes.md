# Bulma CSS Framework

## 1. Introduction to Bulma

-   Bulma is a modern, open-source CSS framework based on Flexbox.
-   Provides responsive, mobile-first components.
-   Pure CSS --- no JavaScript included.

## 2. Installation

### CDN

``` html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
```

### NPM

    npm install bulma

### Via Sass

``` scss
@import "bulma/bulma";
```

## 3. Core Concepts

### Flexbox-Based Layout

-   Most Bulma components use Flexbox for alignment, distribution, and
    spacing.

### Responsive Design

-   Built-in breakpoints: mobile, tablet, desktop, widescreen, fullhd.

### Modifiers

-   Colors: `.is-primary`, `.is-info`, `.is-warning`, `.is-danger`
-   Sizes: `.is-small`, `.is-medium`, `.is-large`
-   States: `.is-loading`, `.is-active`, `.is-focused`

## 4. Layout Components

### Container

``` html
<div class="container">
  Content…
</div>
```

### Section & Hero

``` html
<section class="section">...</section>

<section class="hero is-primary">
  <div class="hero-body">...</div>
</section>
```

### Columns (Grid System)

``` html
<div class="columns">
  <div class="column">1</div>
  <div class="column">2</div>
</div>
```

### Level

``` html
<nav class="level">
  <div class="level-left">...</div>
  <div class="level-right">...</div>
</nav>
```

### Media Object

``` html
<article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img src="img.png">
    </p>
  </figure>
  <div class="media-content">...</div>
</article>
```

### Tiles

``` html
<div class="tile is-ancestor">
  <div class="tile is-parent">
    <article class="tile is-child box">...</article>
  </div>
</div>
```

## 5. Elements

### Buttons

``` html
<button class="button is-primary">Save</button>
```

### Title / Subtitle

``` html
<h1 class="title">Heading</h1>
<h2 class="subtitle">Subheading</h2>
```

### Box

``` html
<div class="box">This is a box.</div>
```

### Tags

``` html
<span class="tag is-warning">Tag</span>
```

### Notification

``` html
<div class="notification is-info">Info message</div>
```

### Progress Bars

``` html
<progress class="progress is-success" value="60" max="100">60%</progress>
```

### Table

``` html
<table class="table is-striped is-hoverable">...</table>
```

### Content

``` html
<div class="content">
  <h1>Title</h1>
  <p>Paragraph text…</p>
</div>
```

## 6. Form Controls

### Basic Inputs

Includes input, textarea, select, checkbox, radio, file input.

### Example

``` html
<div class="field">
  <label class="label">Name</label>
  <div class="control">
    <input class="input" type="text" placeholder="Enter your name">
  </div>
</div>
```

### Addons

``` html
<div class="field has-addons">
  <p class="control">
    <input class="input" type="text" placeholder="Search">
  </p>
  <p class="control">
    <a class="button is-info">Go</a>
  </p>
</div>
```

### Icons in Inputs

``` html
<div class="control has-icons-left">
  <input class="input" type="email">
  <span class="icon is-left"><i class="fas fa-envelope"></i></span>
</div>
```

### Horizontal Forms

``` html
<div class="field is-horizontal">...</div>
```

### Validation

-   `is-success`, `is-danger`

## 7. Components

### Navbar

``` html
<nav class="navbar">
  <div class="navbar-brand"></div>
</nav>
```

### Card

``` html
<div class="card">
  <div class="card-content">...</div>
</div>
```

### Modal

``` html
<div class="modal is-active">...</div>
```

### Dropdown

``` html
<div class="dropdown is-active">
  <div class="dropdown-menu">...</div>
</div>
```

### Breadcrumb

``` html
<nav class="breadcrumb">
  <ul>
    <li><a>Home</a></li>
    <li class="is-active"><a>Docs</a></li>
  </ul>
</nav>
```

### Menu

``` html
<aside class="menu">
  <ul class="menu-list">
    <li><a>Dashboard</a></li>
  </ul>
</aside>
```

### Message

``` html
<article class="message is-info">
  <div class="message-header">Info</div>
  <div class="message-body">Message content…</div>
</article>
```

### Pagination

``` html
<nav class="pagination">...</nav>
```

### Tabs

``` html
<div class="tabs">...</div>
```

### Panel

``` html
<nav class="panel">...</nav>
```

## 8. Utilities & Helpers

-   Spacing helpers: `m-1`, `p-2`, `mt-3`, etc.\
-   Text helpers: `.has-text-centered`, `.has-text-weight-bold`\
-   Display helpers: `.is-flex`, `.is-inline`, `.is-hidden-mobile`\
-   Flexbox helpers: `.is-justify-content-center`,
    `.is-align-items-flex-start`\
-   Color helpers: `.has-background-primary`, `.has-text-danger`

## 9. Customization (Sass)

``` scss
$primary: #4a65f6;
@import "bulma/bulma";
```

## 10. Best Practices

-   Use modifiers to maintain consistency.
-   Avoid overusing helper classes.
-   Prefer Sass customization.

## 11. Additional Resources

-   https://bulma.io
-   https://bulma.io/documentation
