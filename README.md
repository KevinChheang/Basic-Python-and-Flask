# Basic Python and Flask

**A simple calculator with Flask, which uses URL query parameters to get the numbers to calculate with.**

**Flask app that responds to 4 different routes. Each route does a math operation with two numbers, a and b, which will be passed in as URL GET-style query parameters.**
- /add
  - Adds a and b and returns result as the body.
- /sub
  - Same, subtracting b from a.
- /mult
  - Same, multiplying a and b.
- /div
  - Same, dividing a by b.

**You can also use a single route/view function that can deal with 4 different kinds of URLs using a route parameter:**
- /math/add
- /math/sub
- /math/mult
- /math/div
