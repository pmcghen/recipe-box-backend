# The Recipe Box

![Heroku](https://heroku-badge.herokuapp.com/?app=pmcg-recipe-box)

**A basic CMS for storing recipes, written in Django.**

This is my first Django project, and it's a constant work in progress as I continue to learn. The front end is [available here](https://github.com/pmcghen/recipe-box), and you can see it in action at [pmcghen.github.io/recipe-box/](https://pmcghen.github.io/recipe-box/).

## Getting started

First thing's first, initialize and activate a virtualenv...

```
virtualenv env
source env/bin/activate
```

Install the dependencies...

```
pip install -r requirements.txt
```

And you're ready to run the server.

```
python manage.py runserver
```

### Cloudinary integration

Images are uploaded to [Cloudinary](https://cloudinary.com/), so you'll want to set up an account there. You'll need to put your cloud name, API key, and secret in your `.env` file using the keys `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, and `CLOUDINARY_API_SECRET`. See `env.example` for the list of environment variables used in this project.

## Available endpoints

### `/recipes/`

Returns all recipes. The expected response will look like this:

```json
[
  {
    "id": 1,
    "name": "Bacon Jam",
    "slug": "bacon-jam",
    "ingredients": "1lb bacon\r\n1/4c diced shallot\r\n3/4c diced onion\r\n1 heaping tsp Calabrian chilis\r\n1/3c apple cider vinegar\r\n1/2c beer (Necromancer Night Light)\r\n3 cloves garlic\r\n2T molasses",
    "activeTime": 20,
    "inactiveTime": null,
    "directions": "Coarsely chop bacon and cook in a Dutch oven until crispy. Drain on paper towel lined plate. Pour off all but about 1T of the bacon fat. Caramelize onions in the bacon fat. Add garlic and cook until fragrant. Add vinegar, molasses, and beer. Bring to a boil for 2-3 minutes. Turn heat down to a simmer and reintroduce the bacon. Simmer until liquid has evaporated, about 60 minutes. Pulse in food processor to desired consistency",
    "notes": "",
    "isFeatured": true,
    "rating": 5
  },
  {
    "id": 2,
    "name": "Pizza Dough",
    "slug": "pizza-dough",
    "ingredients": "72% water\r\n20% starter\r\n2% salt\r\n1% sugar",
    "activeTime": null,
    "inactiveTime": null,
    "directions": "Mix all ingredients until smooth and elastic.",
    "notes": "Works best with a 2-3 day cold ferment",
    "isFeatured": false,
    "rating": 5
  }
]
```

### `/search/`

Expects a `POST` request with a JSON object in the `body`.


```json
{
    "query": "pizza"
}
```

Returns an array of `recipe` objects that match the search query.

```json
{
    "id": 2,
    "name": "Pizza Dough",
    "slug": "pizza-dough",
    "ingredients": "72% water\r\n20% starter\r\n2% salt\r\n1% sugar",
    "activeTime": null,
    "inactiveTime": null,
    "directions": "Mix all ingredients until smooth and elastic.",
    "notes": "Works best with a 2-3 day cold ferment",
    "isFeatured": false,
    "rating": 5
}
```
