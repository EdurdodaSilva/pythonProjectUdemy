from django.test import TestCase
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self):
        return super().setUp()

    @staticmethod
    def make_category(name='Category'):
        return Category.objects.create(name=name)

    @staticmethod
    def make_author(
            first_name='Eduardo',
            last_name='Da Silva',
            username='Eduardosilva',
            password='Not2020#',
            email='<eduardo@gmail.com>'
            ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_recipe(
            self,
            category_data=None,
            author_data=None,
            title='Recipe title',
            description='Recipe description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Pessoas',
            preparation_steps='preparation steps',
            preparation_steps_is_html=False,
            is_published=True,
            cover_image=False
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            cover_image=cover_image

        )