from django import template
from ..models import Subject
<<<<<<< HEAD
=======

>>>>>>> First commit
register = template.Library()


@register.filter
def index( indexable, i):
<<<<<<< HEAD
    print(indexable[i])
    return indexable[i]


@register.filter
def get_subject(subject_Id ):
    obj = Subject.object.get(subject=subject_Id)
    return obj.name
=======
    try:
        return indexable[i]
    except:
        return 0


@register.filter
def get_subject(subject_Id):
    obj = Subject.object.get(subject=subject_Id)
    return obj.name


@register.filter
def times(number):
    return range(1,number)
>>>>>>> First commit
