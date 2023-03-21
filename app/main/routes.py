"""Main routes for the application"""
from app.main import bp
from flask import render_template

data = [
    {
    'id': 1,
    'name': 'Sweet Naija',
    'members': [
        {
            'title': 'Fufu & Egusi Soup',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHW8DjQGvutI881akQiYVXrhrm1brwsvHxmUzhlVGr&s',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue.',
            'ingredients': 'Red Oil, Egusi, Onions, Peppers, Salt ...',
            'price': 200
        },
        {
            'title': 'Jollof Rice',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOvR88uKa8xYIJocAcyxnMahJtX1dwRnfF5w&usqp=CAU',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue.',
            'ingredients': 'Vegetable Oil, Tomatoes, Peppers, Salt, Rice',
            'price': 250
        },
        {
            'title': 'Eba & Okra Soup',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWVeEt1q4mLhOdxrOU9koUHexhMAHf1ZUPigRyc6SGnA&s',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue.',
            'ingredients': 'Red Oil, Okra, Onion, Pepper, Cray fish, Garri',
            'price': 300
        },
        {
            'title': 'Fufu & Groundnut soup',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHW8DjQGvutI881akQiYVXrhrm1brwsvHxmUzhlVGr&s',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue.',
            'ingredients': 'Red Oil, groundnut, dried okra',
            'price': 200
        },
    ]
},
{
    'id': 2,
    'name': 'Fresh & Natural',
    'members': [
        {
            'title': 'Fufu & Egusi Soup',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHW8DjQGvutI881akQiYVXrhrm1brwsvHxmUzhlVGr&s',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue.',
            'ingredients': 'Red Oil, Egusi, Onions, Peppers, Salt ...',
            'price': 200
        },
        {
            'title': 'Jollof Rice',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOvR88uKa8xYIJocAcyxnMahJtX1dwRnfF5w&usqp=CAU',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue.',
            'ingredients': 'Vegetable Oil, Tomatoes, Peppers, Salt, Rice',
            'price': 250
        },
        {
            'title': 'Eba & Okra Soup',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWVeEt1q4mLhOdxrOU9koUHexhMAHf1ZUPigRyc6SGnA&s',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue.',
            'ingredients': 'Red Oil, Okra, Onion, Pepper, Cray fish, Garri',
            'price': 300
        },
        {
            'title': 'Fufu & Groundnut soup',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHW8DjQGvutI881akQiYVXrhrm1brwsvHxmUzhlVGr&s',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue.',
            'ingredients': 'Red Oil, groundnut, dried okra',
            'price': 200
        },
    ]
},
{
    'id': 3,
    'name': 'Super Foods',
    'members': [
        {
            'title': 'Fufu & Egusi Soup',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHW8DjQGvutI881akQiYVXrhrm1brwsvHxmUzhlVGr&s',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue.',
            'ingredients': 'Red Oil, Egusi, Onions, Peppers, Salt ...',
            'price': 200
        },
        {
            'title': 'Jollof Rice',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOvR88uKa8xYIJocAcyxnMahJtX1dwRnfF5w&usqp=CAU',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue.',
            'ingredients': 'Vegetable Oil, Tomatoes, Peppers, Salt, Rice',
            'price': 250
        },
        {
            'title': 'Eba & Okra Soup',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWVeEt1q4mLhOdxrOU9koUHexhMAHf1ZUPigRyc6SGnA&s',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue.',
            'ingredients': 'Red Oil, Okra, Onion, Pepper, Cray fish, Garri',
            'price': 300
        },
        {
            'title': 'Fufu & Groundnut soup',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHW8DjQGvutI881akQiYVXrhrm1brwsvHxmUzhlVGr&s',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eu ultrices vitae auctor eu augue.',
            'ingredients': 'Red Oil, groundnut, dried okra',
            'price': 200
        },
    ]
}
]

@bp.route('/')
@bp.route('/home/')
def index():
    """Home page"""
    return render_template('home.html', categories=data)

@bp.route('/about/')
def about():
    """About page"""
    return render_template('about.html')
