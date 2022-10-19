from faker import Faker

from django.http import HttpResponse
from mongo_blog.models import Entry, Blog


def create_in_mongo(request):
    faker = Faker()
    saved = Entry(
        blogs=[Blog(name=faker.word(),
                    text=faker.paragraph(nb_sentences=5))],
        headline="some random category"
    ).save()

    return HttpResponse(f"Done: {saved}")


def all_entries(request):
    blogs_timestamps = list(Entry.objects.values_list('timestamp'))

    print(blogs_timestamps)

    return HttpResponse(f"| ".join([timestamp.strftime("%m-%d-%Y %H:%M:%S") for
                                    timestamp in blogs_timestamps]))
