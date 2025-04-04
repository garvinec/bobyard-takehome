from django.core.management.base import BaseCommand
from db.models import Comment


class Command(BaseCommand):
    help = 'Populate the database with the data given in the json file'

    def handle(self, *args, **kwargs):
        initial_data = [
            {
                "id": "1",
                "author": "Joe",
                "text": "As a solo dev who's taken up freelancing, Firebase and Supabase both work very well for the kinds of projects I do for clients. There's really nothing they can't do since they don't stop you from combining them with other solutions, and there's no reason to take on the extra headache of doing everything from scratch if you're working solo. Firebase is just GCP with an abstraction layer on top - there's nothing stopping you from spinning up a Node service using Cloud Run for long-running tasks that can't be deployed as cloud functions, for example. Same goes for Supabase, nothing stopping you from using AWS or other cloud services to supplement what you get for free with it.",
                "date": "2015-09-01T12:00:00Z",
                "likes": 101,
                "image": "https://yt3.googleusercontent.com/GsP5Yvc5jOSop4SJf_75wdOYaEbO-7ZyYhnARodAGRnEMh-OQjGPGzUz2ZtzsHPtqFyHGvmbEtI=s900-c-k-c0x00ffffff-no-rj"
            },
            {
                "id": "2",
                "author": "Jane",
                "text": "I'm pretty used to node+express and doing all the backend work by myself. Baas solutions are cool, unless you need mountains of custom logic. Then they will only slow you down. Coding your own backend and deploying it securely takes experience, but you'll never have that experience if you never try (;",
                "date": "2015-09-01T12:05:00Z",
                "likes": 56,
                "image": "https://miro.medium.com/v2/resize:fit:2000/1*HkM78Z1G5UKqQNCHwBHRfA.png"
            },
            {
                "id": "3",
                "author": "Smith",
                "text": "C#",
                "date": "2015-09-01T12:10:00Z",
                "likes": 66,
                "image": ""
            },
            {
                "id": "4",
                "author": "Marry",
                "text": "Node/express or Rust/Axum.",
                "date": "2015-09-01T12:15:00Z",
                "likes": 14,
                "image": ""
            },
            {
                "id": "5",
                "author": "Peter",
                "text": ". NET Core Web API / SQL Server. I was born by .NET and I'll die by it. Tools like NSwag and umijs-openapi plugin read the automatically generated Swagger UI from the API and generate typescript types and API fetch functions. Off the beaten path but works for me. All that being said supabase is pretty dope",
                "date": "2015-09-01T12:20:00Z",
                "likes": 38,
                "image": "https://learn.microsoft.com/en-us/aspnet/core/tutorials/web-api-help-pages-using-swagger/_static/custom-info-nswag.png?view=aspnetcore-7.0"
            },
            {
                "id": "6",
                "author": "John",
                "text": "If it’s going to be complicated, NestJs. If not, just Next/Remix with Supabase.",
                "date": "2015-09-01T12:25:00Z",
                "likes": 14,
                "image": ""
            },
            {
                "id": "7",
                "author": "Lily",
                "text": "Ruby on Railsss",
                "date": "2015-09-01T12:15:00Z",
                "likes": 14,
                "image": ""
            },
            {
                "id": "8",
                "author": "Tom",
                "text": "I'm a big fan of Hasura. It's a GraphQL engine that sits on top of Postgres. It's open source and you can run it yourself, but they also have a hosted version. It's really easy to get started with and you can do a lot with it. I've used it for a few projects and it's been great.",
                "date": "2015-09-01T12:30:00Z",
                "likes": 54,
                "image": "https://avatars.githubusercontent.com/u/13966722?s=200&v=4"
            },
            {
                "id": "9",
                "author": "Jack",
                "text": "Laravel is my go to. Extremely stable and robust release cycles, has been around for over 10 years now and it’s all refinement at this stage. It has almost everything baked in (auth, jobs, queues, commands, sessions, etc) and lots of first party modules (like payments).",
                "date": "2015-09-01T12:35:00Z",
                "likes": 25,
                "image": "https://laravel.com/img/logomark.min.svg"
            },
            {
                "id": "10",
                "author": "Rose",
                "text": "I love Ruby on Rails, and since discovering Inertia.js I can't imagine using anything else for the backend. ActiveRecord is so powerful, and Ruby is so expressive and fun to write in. I used to start projects with RoR and try to incorporate React with APIs or GraphQL, but would get tired of the context change. With Inertia, React is just the view layer in the monolith, it doesn't feel separate at all. I love working in this stack and will probably start all future projects heavier than a brochure page with it. If anybody uses React or Laravel, do yourself a favor and check out Inertia, it brings the whole stack together.",
                "date": "2015-09-01T12:40:00Z",
                "likes": 18,
                "image": "https://avatars.githubusercontent.com/u/5429470?s=200&v=4"
            },
            {
                "id": "11",
                "author": "David",
                "text": "Golang. I use that for work on the daily so it’s what’s easiest for me.",
                "date": "2015-09-01T12:45:00Z",
                "likes": 10,
                "image": "https://www.freecodecamp.org/news/content/images/2021/10/golang.png"
            },
            {
                "id": "12",
                "author": "Linda",
                "text": "Since you are going solo, saving time on setup/infra/devops make sense (and focus time on dev). For custom logic, Supabase actually let you write edge custom functions using Deno. It should cover a vast amount of requirements for having a custom backend.",
                "date": "2015-09-01T12:50:00Z",
                "likes": 9,
                "image": ""
            },
            {
                "id": "13",
                "author": "Mike",
                "text": "I used to use nextjs with supabase, but recently switched to nextjs with planetscale and clerky. both hosted on vercel. nothing against supabase btw, both stacks are great, just trying the https://create.t3.gg/ stack to learn some new things.",
                "date": "2015-09-01T12:55:00Z",
                "likes": 31,
                "image": ""
            },
            {
                "id": "14",
                "author": "Emily",
                "text": "Depends. I like to use a Python framework for ML-based projects (Django or FastAPI). For the easiest stack, I generally use Next/Supabase",
                "date": "2015-09-01T13:00:00Z",
                "likes": 8,
                "image": ""
            },
            {
                "id": "15",
                "author": "Bob",
                "text": "I've been using NestJs for the backend of a sass I've been building. I don't think I'll use it again on my next project. I've been itching to learn something else outside the JS ecosystem like Rails or Phoenix. Supabase looks cool too though for a solo dev.",
                "date": "2015-09-01T13:05:00Z",
                "likes": 7,
                "image": ""
            },
            {
                "id": "16",
                "author": "Sara",
                "text": "Sometimes .Net, sometimes Express, sometimes Next. Next can be good esp for smaller teams or solo devs since you can do backend/frontend all on server side, but it is fairly opinionated and has its own quirks.",
                "date": "2015-09-01T13:10:00Z",
                "likes": 6,
                "image": "https://cdn.sanity.io/images/3do82whm/next/4b1f008289a88f4438a1c983fb32cf1a636d9d0e-1000x667.png?w=720&h=480&fit=clip&auto=format"
            }
        ]

        for comment in initial_data:
            Comment.objects.create(
                author=comment["author"],
                text=comment["text"],
                date=comment["date"],
                likes=comment["likes"],
                image=comment["image"]
            )

        self.stdout.write(self.style.SUCCESS(
            'Database populated with sample data'))
