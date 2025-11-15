# Bulma CSS Framework 
# Key Concepts

## 1. Introduction to Bulma

-   Bulma is a modern, open‑source CSS framework based on Flexbox.
-   Provides responsive, mobile‑first components.
-   Pure CSS --- no JavaScript included.

## 2. Installation

### CDN

``` html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
```

### NPM

    npm install bulma

### Import via Sass

``` scss
@import "bulma/bulma";
```

## 3. Core Concepts

### Flexbox-based Layout

-   Nearly all Bulma components rely on Flexbox for alignment and
    spacing.

### Responsive Design

-   Uses breakpoint helpers: mobile, tablet, desktop, widescreen,
    fullhd.

### Modifiers

-   `.is-primary`, `.is-info`, `.is-danger` for colors.
-   `.is-small`, `.is-medium`, `.is-large` for sizes.

## 4. Layout Components

### **Container**

Used to center page content.

``` html
<div class="container">
  Content…
</div>
```

### **Section & Hero**

Large content blocks.

``` html
<section class="section">...</section>
<section class="hero is-primary">
  <div class="hero-body">...</div>
</section>
```

### **Columns**

Powerful responsive grid system.

``` html
<div class="columns">
  <div class="column">1</div>
  <div class="column">2</div>
</div>
```

-   Supports variable column widths, offsets, gaps.

## 5. Elements

### **Buttons**

``` html
<button class="button is-primary">Save</button>
```

### **Title / Subtitle**

``` html
<h1 class="title">Heading</h1>
<h2 class="subtitle">Subheading</h2>
```

### **Tags**

``` html
<span class="tag is-warning">Tag</span>
```

### **Notification**

``` html
<div class="notification is-info">Info message</div>
```

## 6. Form Controls

Includes: - Input - Textarea - Select - Checkbox - Radio - File Upload

Example:

``` html
<div class="field">
  <label class="label">Name</label>
  <div class="control">
    <input class="input" type="text" placeholder="Enter your name">
  </div>
</div>
```

## 7. Components

### **Navbar**

Responsive navigation bar.

``` html
<nav class="navbar">
  <div class="navbar-brand">...</div>
</nav>
```

### **Card**

``` html
<div class="card">
  <div class="card-content">...</div>
</div>
```

### **Modal**

``` html
<div class="modal is-active">
  <div class="modal-background"></div>
  <div class="modal-content">...</div>
</div>
```

## 8. Utilities & Helpers

-   Spacing helpers: `m-1`, `p-2`, `mt-3`, etc.
-   Text helpers: `.has-text-centered`, `.has-text-weight-bold`
-   Display helpers: `.is-flex`, `.is-inline`, `.is-hidden-mobile`
-   Color helpers: `.has-background-primary`, `.has-text-danger`

## 9. Customization

-   Bulma is written in Sass.
-   Variables allow theme customization:

``` scss
$primary: #4a65f6;
@import "bulma/bulma";
```

## 10. Best Practices

-   Use modifiers to maintain consistency.
-   Combine helpers sparingly for clarity.
-   Leverage columns for responsive layout.
-   Customize via Sass instead of overriding CSS inline.

## 11. Additional Resources

-   Official site: bulma.io
-   Documentation: bulma.io/documentation
