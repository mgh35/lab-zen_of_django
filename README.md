# Lab: Zen of Django

What is the zen of Django?

## Introduction

The point of this lab is to try to find the zen of Django. Particularly, as I am starting to work with Django I find myself fighting against the machine rather than being able to take advantage of it. I hope to explore a central use-case to discover where the power of the platform lies.

The major hurdles I find getting into the platform are:

- Active Record Pattern ORM. It is a confusing model for the unitiate. Particularly when used to analytics-type query, things like the inability express queries outside the model is frustrating.
- Very heavy framework. If you find yourself trying to do something against its grain, it is an uphill battle that the framework will win.
- Auth. The focus on object IDs is confusing when approached from a different context.
- Configuration over code. Even harder with an untyped language.

Many of these sound like a problem of approaching this without having previously built many CRUD-type apps. (Or possibly, without having understood that other problems were in fact CRUD-type problems.)

So building this little app is intended to give a sense of developing in Django going with its grain. The natural place to start is the sort of thing along the lines for which Django was created. To that end, the idea is to build out a blog site.

## App Spec

This app is a simple blog site. Users should be able to:

- View public posts and comments.
- ~~Publish comments to posts with public comments enabled.~~
- Create an account, log in, log out.
- Publish posts, with selectable visibility, when logged in.
- Publish comments on posts ~~with restricted comments enabled~~ when authorized.
- ~~Follow other users.~~

## Outcome

The lab was stopped shy of the full spec. The exploratory goals were largely achieved. So it's not clear what the remaining pieces would have added. And one of the key findings was that the route taken on the app, as a DRF API but without a frontend app, was a bad one. The remaining pieces would have been relatively expensive to implement.

## Take-aways

Strengths of Django:

- Quick to get a CRUD app up and running.
- Lots of plugins to extend the app.
- The admin interface could be very handy for cases where the users can tolerate a limited UX.
- Easy database setup and migrations.
- The DRF interactive API pages are very nice.
- django_filters API are nice

Challenges:
- Once you get past a CRUD app, you quickly lose all of the abstractions. They are very much built to the use-case and not easily usable elsewhere.
- The ORM is also very tied to a CRUD app. Not having the ability to JOIN tables, for example, makes it very hard to use in other use-cases.
- It seems to require a relatively high level of familiarity with it's layers and abstractions to use it. And the same again for DRF.
- Security is a challenge. There are lots of powerful features available, but it's incredibly easy to misconfigure something (through a typo, for example) and never know.
- The Django Template views run off different enough abstractions to DRF there there seems to be little reuse. Evolving an app from one to the other, for example, would be a relativley heavy lift.

Not sure I found the zen of Django. It seems to be a tool that offers a strong abstraction for CRUD apps. I can see it making development of that sort of app quite quick for someone quite familiar with Django. It does seem that those advantages quickly fade relative to lighter but more pluggable libraries as you move away from that core use-case.

Maybe the zen of Django is in finding how to make problems fit that core use-case.
