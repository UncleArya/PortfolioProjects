from wtforms import (
    StringField,
    IntegerField,
    DecimalField,
    URLField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, NumberRange, URL, Length
from flask_wtf import FlaskForm


class AddGameForm(FlaskForm):
    """Form for adding new data in the Database"""

    title = StringField(
        label="Title", validators=[DataRequired()], render_kw={"class": "form-field"}
    )
    year = IntegerField(
        label="Year",
        validators=[DataRequired(), NumberRange(min=1960, max=2030)],
        render_kw={"class": "form-field"},
    )
    developer = StringField(
        label="Developer",
        validators=[DataRequired()],
        render_kw={"class": "form-field"},
    )
    genre = StringField(
        label="Genre", validators=[DataRequired()], render_kw={"class": "form-field"}
    )
    description = TextAreaField(
        label="Game Description",
        validators=[DataRequired(), Length(max=350)],
        render_kw={"class": "form-field", "rows": 10},
    )
    rating = DecimalField(
        label="My Rating",
        validators=[DataRequired(), NumberRange(min=0.0, max=10.0)],
        render_kw={"class": "form-field"},
    )
    review = TextAreaField(
        label="What I Love",
        validators=[DataRequired(), Length(max=350)],
        render_kw={"class": "form-field", "rows": 10},
    )
    cover_art = URLField(
        label="Cover Art URL",
        validators=[DataRequired(), URL()],
        render_kw={"class": "form-field"},
    )
    submit = SubmitField(label="Submit")


class EditGameForm(FlaskForm):
    """Form for editing existing data in the Database"""

    title = StringField(label="Title", render_kw={"class": "form-field"})
    year = IntegerField(label="Year", render_kw={"class": "form-field"})
    developer = StringField(label="Developer", render_kw={"class": "form-field"})
    genre = StringField(label="Genre", render_kw={"class": "form-field"})
    description = TextAreaField(
        label="Game Description",
        validators=[Length(max=350)],
        render_kw={"class": "form-field", "rows": 10},
    )
    rating = DecimalField(label="My Rating", render_kw={"class": "form-field"})
    review = TextAreaField(
        label="What I Love",
        validators=[Length(max=350)],
        render_kw={"class": "form-field", "rows": 10},
    )
    cover_art = URLField(label="Cover Art URL", render_kw={"class": "form-field"})
    submit = SubmitField(label="Submit")
